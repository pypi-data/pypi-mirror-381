"""Schema management utilities for the Neo4j service."""

from __future__ import annotations

import json
import re
from collections.abc import Iterable, Mapping
from dataclasses import dataclass
from enum import Enum
from typing import Any

from neo4j import READ_ACCESS, WRITE_ACCESS, Driver
from neo4j.exceptions import Neo4jError

from .neo4j_connection_pools import Neo4jConnectionPools


class SchemaMigrationError(RuntimeError):
    """Raised when a schema migration operation fails."""

    def __init__(self, message: str, *, executed: list[str] | None = None) -> None:
        super().__init__(message)
        self.executed = executed or []


class SchemaValidationError(RuntimeError):
    """Raised when schema validation detects inconsistencies."""

    def __init__(self, message: str, details: Mapping[str, Any]) -> None:
        super().__init__(message)
        self.details = dict(details)


class Neo4jEntityType(str, Enum):
    """Supported entity categories for schema operations."""

    NODE = "node"
    RELATIONSHIP = "relationship"

    @classmethod
    def from_value(cls, value: EntityTypeInput) -> Neo4jEntityType:
        """Normalise input into a supported entity type."""
        if isinstance(value, cls):
            return value
        normalized = value.lower().strip()
        if normalized in {"node", "nodes"}:
            return cls.NODE
        if normalized in {"relationship", "relationships", "rel", "edge", "edges"}:
            return cls.RELATIONSHIP
        msg = f"Unsupported entity type: {value}"
        raise ValueError(msg)


EntityTypeInput = str | Neo4jEntityType


@dataclass(frozen=True)
class EntityContext:
    """Resolved information about an entity involved in schema operations."""

    entity_type: Neo4jEntityType
    alias: str
    pattern: str

    @property
    def name_prefix(self) -> str:
        return "rel_" if self.entity_type is Neo4jEntityType.RELATIONSHIP else ""


@dataclass(frozen=True)
class MigrationPlan:
    """Cypher statements required to move between schema versions."""

    forward: tuple[str, ...]
    rollback: tuple[str, ...]

    @classmethod
    def from_queries(
        cls,
        forward: Iterable[str],
        rollback: Iterable[str] | None = None,
    ) -> MigrationPlan:
        forward_plan = tuple(
            query.strip() for query in forward if query and query.strip()
        )
        if not forward_plan:
            msg = "At least one Cypher statement is required for a migration"
            raise ValueError(msg)
        rollback_plan = tuple(
            query.strip() for query in rollback or [] if query and query.strip()
        )
        return cls(forward_plan, rollback_plan)

    def dry_run(self) -> list[str]:
        return list(self.forward)


class Neo4jSchemas:
    """Manage indexes, constraints, and schema validation."""

    def __init__(
        self,
        pool: Neo4jConnectionPools,
        *,
        database_name: str = "neo4j",
        initial_version: str | None = None,
    ) -> None:
        self.pool = pool
        self.database_name = database_name
        self.initial_version = initial_version
        self._migrations: dict[tuple[str, str], MigrationPlan] = {}

    VERSION_METADATA_LABEL = "__Neo4jSchemaVersion"
    VERSION_METADATA_KEY = "schema"

    def create_index(
        self,
        label: str,
        properties: Iterable[str],
        *,
        index_type: str = "btree",
        options: dict[str, Any] | None = None,
        entity_type: EntityTypeInput = Neo4jEntityType.NODE,
    ) -> str:
        """Create an index for the supplied label and properties."""
        props = self._coerce_properties(properties)
        normalized_type = index_type.lower()
        context = self._resolve_entity_context(label, entity_type)
        name = self._generate_index_name(
            label,
            props,
            normalized_type,
            context,
        )
        if normalized_type in {"btree", "range"}:
            clause = ", ".join(
                self._property_expression(context.alias, prop) for prop in props
            )
            query = (
                f"CREATE INDEX {name} IF NOT EXISTS FOR {context.pattern} ON ({clause})"
            )
        elif normalized_type == "text":
            self._require_property_count(props, 1, "text index")
            clause = self._property_expression(context.alias, props[0])
            query = f"CREATE TEXT INDEX {name} IF NOT EXISTS FOR {context.pattern} ON ({clause})"
        elif normalized_type == "point":
            self._require_property_count(props, 1, "point index")
            clause = self._property_expression(context.alias, props[0])
            query = f"CREATE POINT INDEX {name} IF NOT EXISTS FOR {context.pattern} ON ({clause})"
        elif normalized_type == "fulltext":
            clause = ", ".join(
                self._property_expression(context.alias, prop) for prop in props
            )
            query = (
                f"CREATE FULLTEXT INDEX {name} IF NOT EXISTS "
                f"FOR {context.pattern} ON EACH [{clause}]"
            )
        elif normalized_type == "vector":
            self._require_property_count(props, 1, "vector index")
            if context.entity_type is Neo4jEntityType.RELATIONSHIP:
                msg = "Vector indexes are only supported for nodes"
                raise ValueError(msg)
            clause = self._property_expression(context.alias, props[0])
            query = (
                f"CREATE VECTOR INDEX {name} IF NOT EXISTS "
                f"FOR {context.pattern} ON ({clause})"
            )
        else:
            msg = f"Unsupported index type: {index_type}"
            raise ValueError(msg)
        query += self._format_options(options)
        self._run_write(query)
        return query

    def create_constraint(
        self,
        label: str,
        properties: Iterable[str],
        *,
        constraint_type: str = "unique",
        entity_type: EntityTypeInput = Neo4jEntityType.NODE,
    ) -> str:
        """Create a constraint for the supplied label and properties."""
        props = self._coerce_properties(properties)
        normalized_type = constraint_type.lower()
        context = self._resolve_entity_context(label, entity_type)
        name = self._generate_constraint_name(
            label,
            props,
            normalized_type,
            context,
        )
        if normalized_type == "unique":
            if context.entity_type is not Neo4jEntityType.NODE:
                msg = "Unique constraints are only supported for nodes"
                raise ValueError(msg)
            self._require_property_count(props, 1, "unique constraint")
            clause = self._property_expression(context.alias, props[0])
            query = (
                f"CREATE CONSTRAINT {name} IF NOT EXISTS "
                f"FOR {context.pattern} REQUIRE {clause} IS UNIQUE"
            )
        elif normalized_type in {"node_key", "key"}:
            if context.entity_type is not Neo4jEntityType.NODE:
                msg = "Node key constraints are only supported for nodes"
                raise ValueError(msg)
            clause = ", ".join(
                self._property_expression(context.alias, prop) for prop in props
            )
            query = (
                f"CREATE CONSTRAINT {name} IF NOT EXISTS "
                f"FOR {context.pattern} REQUIRE ({clause}) IS NODE KEY"
            )
        elif normalized_type in {"exists", "existence", "not_null"}:
            self._require_property_count(props, 1, "existence constraint")
            clause = self._property_expression(context.alias, props[0])
            query = (
                f"CREATE CONSTRAINT {name} IF NOT EXISTS "
                f"FOR {context.pattern} REQUIRE {clause} IS NOT NULL"
            )
        else:
            msg = f"Unsupported constraint type: {constraint_type}"
            raise ValueError(msg)
        self._run_write(query)
        return query

    def register_migration(
        self,
        from_version: str,
        to_version: str,
        queries: Iterable[str],
        *,
        rollback: Iterable[str] | None = None,
    ) -> None:
        """Register migration Cypher statements between two versions."""
        key = (from_version, to_version)
        self._migrations[key] = MigrationPlan.from_queries(
            queries,
            rollback,
        )

    def migrate_schema(
        self,
        from_version: str,
        to_version: str,
        *,
        dry_run: bool = False,
        expected_schema: dict[str, list[dict[str, Any]]] | None = None,
    ) -> list[str]:
        """Execute registered migrations between two schema versions."""
        path = self._resolve_migration_path(from_version, to_version)
        if dry_run:
            statements: list[str] = []
            for _, _, plan in path:
                statements.extend(plan.dry_run())
            return statements

        current_version = self._get_current_version()
        if current_version is None:
            current_version = self.initial_version or from_version
        if current_version != from_version:
            msg = (
                "Current schema version "
                f"{current_version!r} does not match expected "
                f"{from_version!r}"
            )
            raise RuntimeError(msg)

        executed_statements: list[str] = []
        applied: list[tuple[str, str, MigrationPlan]] = []
        try:
            for source, target, plan in path:
                executed = self._apply_plan(plan)
                executed_statements.extend(executed)
                applied.append((source, target, plan))
                self._set_current_version(target)
        except Exception:
            failing_plan = path[len(applied)][2] if len(applied) < len(path) else None
            self._rollback_failed_migration(
                from_version,
                applied,
                failing_plan,
            )
            raise

        if expected_schema is not None:
            self.validate_schema(expected_schema, raise_on_mismatch=True)
        return executed_statements

    def get_schema(self) -> dict[str, list[dict[str, Any]]]:
        """Return the current database schema."""

        def operation(driver: Driver) -> dict[str, list[dict[str, Any]]]:
            with driver.session(
                database=self.database_name,
                default_access_mode=READ_ACCESS,
            ) as session:
                nodes = session.run(
                    "CALL db.schema.nodeTypeProperties()",
                ).data()
                relationships = session.run(
                    "CALL db.schema.relTypeProperties()",
                ).data()
            return {
                "nodes": nodes,
                "relationships": relationships,
            }

        try:
            return self.pool.execute_with_retry(operation)
        except RuntimeError as exc:  # pragma: no cover - fallback path
            if self._is_missing_schema_procedure(exc.__cause__):
                return self._schema_from_apoc()
            raise
        except Neo4jError as exc:  # pragma: no cover - fallback path
            if self._is_missing_schema_procedure(exc):
                return self._schema_from_apoc()
            raise

    def validate_schema(
        self,
        expected_schema: dict[str, list[dict[str, Any]]],
        *,
        raise_on_mismatch: bool = False,
    ) -> dict[str, Any]:
        """Compare the current schema to an expected definition."""
        actual = self.get_schema()
        expected_nodes = self._normalize_entries(expected_schema.get("nodes", []))
        expected_relationships = self._normalize_entries(
            expected_schema.get("relationships", []),
        )
        actual_nodes = self._normalize_entries(actual.get("nodes", []))
        actual_relationships = self._normalize_entries(
            actual.get("relationships", []),
        )

        missing_nodes = [json.loads(entry) for entry in expected_nodes - actual_nodes]
        unexpected_nodes = [
            json.loads(entry) for entry in actual_nodes - expected_nodes
        ]
        missing_relationships = [
            json.loads(entry) for entry in expected_relationships - actual_relationships
        ]
        unexpected_relationships = [
            json.loads(entry) for entry in actual_relationships - expected_relationships
        ]
        valid = not (
            missing_nodes
            or unexpected_nodes
            or missing_relationships
            or unexpected_relationships
        )
        result = {
            "valid": valid,
            "missing": {
                "nodes": missing_nodes,
                "relationships": missing_relationships,
            },
            "unexpected": {
                "nodes": unexpected_nodes,
                "relationships": unexpected_relationships,
            },
        }

        if raise_on_mismatch and not valid:
            raise SchemaValidationError(
                "Schema validation failed",
                result,
            )
        return result

    def _version_metadata_key(self) -> str:
        return f"{self.database_name}:{self.VERSION_METADATA_KEY}"

    def _get_current_version(self) -> str | None:
        def operation(driver: Driver) -> str | None:
            with driver.session(
                database=self.database_name,
                default_access_mode=READ_ACCESS,
            ) as session:
                result = session.run(
                    (
                        "MATCH (meta:"
                        + self.VERSION_METADATA_LABEL
                        + " {name: $name}) RETURN meta.version AS version"
                    ),
                    {"name": self._version_metadata_key()},
                )
                try:
                    record = result.single(strict=False)
                except TypeError:  # pragma: no cover - compatibility fallback
                    data = result.data()
                    record = data[0] if data else None
            if record:
                version = record.get("version")
                if version is not None:
                    return str(version)
            return None

        return self.pool.execute_with_retry(operation)

    def _set_current_version(self, version: str) -> None:
        def operation(driver: Driver) -> None:
            with driver.session(
                database=self.database_name,
                default_access_mode=WRITE_ACCESS,
            ) as session:
                session.run(
                    (
                        "MERGE (meta:"
                        + self.VERSION_METADATA_LABEL
                        + " {name: $name}) "
                        "SET meta.version = $version, "
                        "meta.updated_at = timestamp()"
                    ),
                    {
                        "name": self._version_metadata_key(),
                        "version": version,
                    },
                )

        self.pool.execute_with_retry(operation)

    def _apply_plan(self, plan: MigrationPlan) -> list[str]:
        def operation(driver: Driver) -> list[str]:
            executed: list[str] = []
            with driver.session(
                database=self.database_name,
                default_access_mode=WRITE_ACCESS,
            ) as session:
                for statement in plan.forward:
                    try:
                        session.run(statement)
                    except Exception as exc:  # pragma: no cover - driver errors
                        raise SchemaMigrationError(
                            "Failed to execute migration statement",
                            executed=executed,
                        ) from exc
                    executed.append(statement)
            return executed

        return self.pool.execute_with_retry(operation)

    def _rollback_failed_migration(
        self,
        from_version: str,
        applied: list[tuple[str, str, MigrationPlan]],
        failing_plan: MigrationPlan | None,
    ) -> None:
        rollback_plans: list[MigrationPlan] = []
        if failing_plan is not None:
            rollback_plans.append(failing_plan)
        for _, _, plan in reversed(applied):
            rollback_plans.append(plan)
        for plan in rollback_plans:
            self._execute_rollback(plan)
        try:
            self._set_current_version(from_version)
        except Exception:  # pragma: no cover - best effort reset
            pass

    def _execute_rollback(self, plan: MigrationPlan) -> None:
        if not plan.rollback:
            return

        def operation(driver: Driver) -> None:
            with driver.session(
                database=self.database_name,
                default_access_mode=WRITE_ACCESS,
            ) as session:
                for statement in reversed(plan.rollback):
                    session.run(statement)

        self.pool.execute_with_retry(operation)

    def _resolve_migration_path(
        self,
        from_version: str,
        to_version: str,
    ) -> list[tuple[str, str, MigrationPlan]]:
        if from_version == to_version:
            return []
        visited: set[str] = set()
        path = self._resolve_path_recursive(
            from_version,
            to_version,
            visited,
        )
        if path is None:
            msg = f"No migration path registered from {from_version} to {to_version}"
            raise KeyError(msg)
        return path

    def _resolve_path_recursive(
        self,
        current: str,
        target: str,
        visited: set[str],
    ) -> list[tuple[str, str, MigrationPlan]] | None:
        if current == target:
            return []
        direct = self._migrations.get((current, target))
        if direct:
            return [(current, target, direct)]
        visited.add(current)
        for (source, destination), plan in self._migrations.items():
            if source != current or destination in visited:
                continue
            branch = self._resolve_path_recursive(
                destination,
                target,
                visited | {destination},
            )
            if branch is not None:
                return [(current, destination, plan)] + branch
        return None

    def _schema_from_apoc(self) -> dict[str, list[dict[str, Any]]]:
        """Fetch schema definition using APOC meta schema."""

        def operation(driver: Driver) -> dict[str, list[dict[str, Any]]]:
            with driver.session(
                database=self.database_name,
                default_access_mode=READ_ACCESS,
            ) as session:
                record = session.run(
                    "CALL apoc.meta.schema() YIELD value RETURN value AS schema",
                ).single()
            schema = record.get("schema") if record else {}
            if isinstance(schema, dict):
                return self._convert_apoc_schema(schema)
            return {"nodes": [], "relationships": []}

        return self.pool.execute_with_retry(operation)

    def _convert_apoc_schema(
        self,
        schema: dict[str, Any],
    ) -> dict[str, list[dict[str, Any]]]:
        nodes: list[dict[str, Any]] = []
        apoc_nodes = schema.get("nodes", {})
        if isinstance(apoc_nodes, dict):
            for label, node_info in apoc_nodes.items():
                properties = {}
                if isinstance(node_info, dict):
                    properties = node_info.get("properties", {})
                if isinstance(properties, dict):
                    for prop, meta in properties.items():
                        property_types = self._extract_types(meta)
                        mandatory = self._extract_mandatory(meta)
                        nodes.append(
                            {
                                "nodeType": label,
                                "propertyName": prop,
                                "propertyTypes": property_types,
                                "mandatory": mandatory,
                            },
                        )

        relationships: list[dict[str, Any]] = []
        apoc_relationships = schema.get("relationships", {})
        if isinstance(apoc_relationships, dict):
            for rel_type, rel_info in apoc_relationships.items():
                properties = {}
                if isinstance(rel_info, dict):
                    properties = rel_info.get("properties", {})
                    start_labels = rel_info.get("startNodeLabels") or rel_info.get(
                        "startNodes",
                    )
                    end_labels = rel_info.get("endNodeLabels") or rel_info.get(
                        "endNodes",
                    )
                else:
                    start_labels = []
                    end_labels = []
                start = self._coerce_label_list(start_labels)
                end = self._coerce_label_list(end_labels)
                if isinstance(properties, dict) and properties:
                    for prop, meta in properties.items():
                        property_types = self._extract_types(meta)
                        mandatory = self._extract_mandatory(meta)
                        relationships.append(
                            {
                                "relationshipType": rel_type,
                                "propertyName": prop,
                                "propertyTypes": property_types,
                                "mandatory": mandatory,
                                "startNodeLabels": start,
                                "endNodeLabels": end,
                            },
                        )
                else:
                    relationships.append(
                        {
                            "relationshipType": rel_type,
                            "propertyName": None,
                            "propertyTypes": [],
                            "mandatory": False,
                            "startNodeLabels": start,
                            "endNodeLabels": end,
                        },
                    )

        return {
            "nodes": nodes,
            "relationships": relationships,
        }

    def _is_missing_schema_procedure(self, exc: BaseException | None) -> bool:
        if isinstance(exc, Neo4jError):
            return bool(exc.code and "Procedure.ProcedureNotFound" in exc.code)
        return False

    def _extract_types(self, meta: Mapping[str, object] | None) -> list[str]:
        if isinstance(meta, Mapping):
            raw_type = meta.get("type")
            if isinstance(raw_type, (list, tuple, set)):
                return [str(item) for item in raw_type]
            if raw_type is not None:
                return [str(raw_type)]
        return []

    def _extract_mandatory(self, meta: Mapping[str, object] | None) -> bool:
        if isinstance(meta, Mapping):
            for key in ("mandatory", "exists", "existence", "required"):
                value = meta.get(key)
                if isinstance(value, bool):
                    return value
        return False

    def _coerce_label_list(self, labels: object) -> list[str]:
        if isinstance(labels, (list, tuple, set)):
            return [str(label) for label in labels]
        if labels is None:
            return []
        return [str(labels)]

    def _normalize_entries(
        self,
        entries: list[dict[str, Any]],
    ) -> set[str]:
        normalized: set[str] = set()
        for entry in entries:
            serializable = self._to_serializable(entry)
            normalized.add(json.dumps(serializable, sort_keys=True))
        return normalized

    def _to_serializable(self, value: object) -> object:
        if isinstance(value, dict):
            return {key: self._to_serializable(val) for key, val in value.items()}
        if isinstance(value, (list, tuple)):
            return [self._to_serializable(item) for item in value]
        if isinstance(value, set):
            return [
                self._to_serializable(item)
                for item in sorted(value, key=lambda item: repr(item))
            ]
        return value

    def _run_write(
        self,
        query: str,
        parameters: dict[str, Any] | None = None,
    ) -> list[dict[str, Any]]:
        return self._run_query(
            query,
            parameters=parameters,
            access_mode=WRITE_ACCESS,
        )

    def _run_query(
        self,
        query: str,
        *,
        parameters: dict[str, Any] | None = None,
        access_mode: str,
    ) -> list[dict[str, Any]]:
        def operation(driver: Driver) -> list[dict[str, Any]]:
            with driver.session(
                database=self.database_name,
                default_access_mode=access_mode,
            ) as session:
                result = session.run(query, parameters or {})
                return result.data()

        return self.pool.execute_with_retry(operation)

    def _format_options(self, options: dict[str, Any] | None) -> str:
        if not options:
            return ""
        formatted = ", ".join(
            f"{key}: {self._format_option_value(value)}"
            for key, value in options.items()
        )
        return f" OPTIONS {{{formatted}}}"

    def _format_option_value(self, value: object) -> str:
        if isinstance(value, str):
            escaped = value.replace("'", "\\'")
            return f"'{escaped}'"
        if isinstance(value, bool):
            return "true" if value else "false"
        if isinstance(value, (int, float)):
            return str(value)
        if isinstance(value, dict):
            inner = ", ".join(
                f"{key}: {self._format_option_value(val)}" for key, val in value.items()
            )
            return f"{{{inner}}}"
        if isinstance(value, (list, tuple)):
            inner = ", ".join(self._format_option_value(item) for item in value)
            return f"[{inner}]"
        if isinstance(value, set):
            inner = ", ".join(
                self._format_option_value(item)
                for item in sorted(value, key=lambda item: repr(item))
            )
            return f"[{inner}]"
        msg = f"Unsupported option value type: {type(value).__name__}"
        raise TypeError(msg)

    def _coerce_properties(self, properties: Iterable[str]) -> list[str]:
        props = [prop for prop in properties if prop]
        if not props:
            msg = "At least one property must be supplied"
            raise ValueError(msg)
        return props

    def _require_property_count(
        self,
        props: list[str],
        expected: int,
        label: str,
    ) -> None:
        if len(props) != expected:
            msg = f"{label} requires exactly {expected} property"
            raise ValueError(msg)

    def _resolve_entity_context(
        self,
        label: str,
        entity_type: EntityTypeInput,
    ) -> EntityContext:
        normalized = Neo4jEntityType.from_value(entity_type)
        if normalized is Neo4jEntityType.NODE:
            return EntityContext(normalized, "n", f"(n:{label})")
        return EntityContext(normalized, "r", f"()-[r:{label}]-()")

    def _generate_index_name(
        self,
        label: str,
        properties: list[str],
        index_type: str,
        context: EntityContext,
    ) -> str:
        sanitized_label = self._sanitize_identifier(label.lower())
        sanitized_props = "_".join(
            self._sanitize_identifier(prop.lower()) for prop in properties
        )
        prefix = context.name_prefix
        return f"{prefix}{sanitized_label}_{sanitized_props}_{index_type}_idx"

    def _generate_constraint_name(
        self,
        label: str,
        properties: list[str],
        constraint_type: str,
        context: EntityContext,
    ) -> str:
        sanitized_label = self._sanitize_identifier(label.lower())
        sanitized_props = "_".join(
            self._sanitize_identifier(prop.lower()) for prop in properties
        )
        suffix = {
            "unique": "uniq",
            "node_key": "nodekey",
            "key": "nodekey",
            "exists": "exists",
            "existence": "exists",
            "not_null": "exists",
        }.get(constraint_type, constraint_type)
        prefix = context.name_prefix
        return f"{prefix}{sanitized_label}_{sanitized_props}_{suffix}_constraint"

    def _sanitize_identifier(self, value: str) -> str:
        return re.sub(r"[^0-9a-zA-Z_]+", "_", value)

    def _property_expression(self, alias: str, property_name: str) -> str:
        escaped = property_name.replace("`", "``")
        return f"{alias}.`{escaped}`"
