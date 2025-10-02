from __future__ import annotations

from collections import OrderedDict
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field


@dataclass
class QueryPlanCache:
    """LRU cache for storing query plans by query signature."""

    max_size: int = 128
    _store: OrderedDict[
        tuple[str, tuple[tuple[str, object], ...]],
        object,
    ] = field(default_factory=OrderedDict)

    def __post_init__(self) -> None:
        if not isinstance(self.max_size, int) or self.max_size <= 0:
            msg = "max_size must be a positive integer"
            raise ValueError(msg)

    def make_key(
        self,
        query: str,
        parameters: Mapping[str, object],
    ) -> tuple[str, tuple[tuple[str, object], ...]]:
        frozen = tuple(
            sorted(
                (
                    name,
                    self._freeze_value(value),
                )
                for name, value in parameters.items()
            ),
        )
        return query, frozen

    def get(
        self,
        key: tuple[str, tuple[tuple[str, object], ...]],
    ) -> object | None:
        if key not in self._store:
            return None
        self._store.move_to_end(key)
        return self._store[key]

    def set(
        self,
        key: tuple[str, tuple[tuple[str, object], ...]],
        plan: object,
    ) -> None:
        self._store[key] = plan
        self._store.move_to_end(key)
        if len(self._store) > self.max_size:
            self._store.popitem(last=False)

    def _freeze_value(self, value: object) -> object:
        if isinstance(value, Mapping):
            return tuple(
                sorted(
                    (
                        str(key),
                        self._freeze_value(item),
                    )
                    for key, item in value.items()
                ),
            )
        if isinstance(value, (list, tuple, set, frozenset)):
            return tuple(self._freeze_value(item) for item in value)
        if isinstance(value, (str, int, float, bool)) or value is None:
            return value
        return repr(value)


class Neo4jQueryBuilders:
    """Fluent builder for constructing parameterised Cypher queries."""

    def __init__(
        self,
        *,
        plan_cache: QueryPlanCache | None = None,
        max_cache_size: int = 128,
    ) -> None:
        self._clauses: list[str] = []
        self._parameters: dict[str, object] = {}
        self._parameter_names: set[str] = set()
        self._plan_cache = plan_cache or QueryPlanCache(max_cache_size)
        self._last_cache_key: tuple[str, tuple[tuple[str, object], ...]] | None = None
        self._parameter_index = 0

    def match(
        self,
        alias: str,
        *,
        labels: str | Sequence[str] | None = None,
        properties: Mapping[str, object] | None = None,
    ) -> Neo4jQueryBuilders:
        """Append a ``MATCH`` clause for a node."""
        alias_name = self._validate_alias(alias)
        label_clause = self._format_labels(labels)
        properties_clause = self._format_properties(alias_name, properties)
        self._clauses.append(
            f"MATCH ({alias_name}{label_clause}{properties_clause})",
        )
        self._invalidate_cache()
        return self

    def create(
        self,
        alias: str,
        *,
        labels: str | Sequence[str] | None = None,
        properties: Mapping[str, object] | None = None,
    ) -> Neo4jQueryBuilders:
        """Append a ``CREATE`` clause for a node."""
        alias_name = self._validate_alias(alias)
        label_clause = self._format_labels(labels)
        properties_clause = self._format_properties(alias_name, properties)
        self._clauses.append(
            f"CREATE ({alias_name}{label_clause}{properties_clause})",
        )
        self._invalidate_cache()
        return self

    def where(
        self,
        condition: str,
        parameters: Mapping[str, object] | None = None,
    ) -> Neo4jQueryBuilders:
        """Append a ``WHERE`` clause with optional parameters."""
        expression = self._validate_expression(condition, "WHERE condition")
        if parameters is not None:
            if not isinstance(parameters, Mapping):
                msg = "parameters must be a mapping"
                raise TypeError(msg)
            for name, value in parameters.items():
                param_name = self._validate_parameter_name(name)
                self._add_parameter(param_name, value)
        self._clauses.append(f"WHERE {expression}")
        self._invalidate_cache()
        return self

    def where_property(
        self,
        alias: str,
        property_name: str,
        operator: str,
        value: object,
    ) -> Neo4jQueryBuilders:
        """Append a safe property comparison."""
        alias_name = self._validate_alias(alias)
        escaped_property = self._escape_identifier(property_name)
        operator_token = self._validate_operator(operator)
        parameter = self._unique_parameter_name(alias_name, property_name)
        if operator_token == "IN":
            validated_value = self._validate_sequence(value)
        else:
            validated_value = value
        self._add_parameter(parameter, validated_value)
        clause = f"{alias_name}.{escaped_property} {operator_token} ${parameter}"
        self._clauses.append(f"WHERE {clause}")
        self._invalidate_cache()
        return self

    def with_(self, *items: str) -> Neo4jQueryBuilders:
        """Append a ``WITH`` clause."""
        if not items:
            msg = "WITH clause requires at least one item"
            raise ValueError(msg)
        expressions = [self._validate_expression(item, "WITH item") for item in items]
        joined = ", ".join(expressions)
        self._clauses.append(f"WITH {joined}")
        self._invalidate_cache()
        return self

    def return_(self, *items: str) -> Neo4jQueryBuilders:
        """Append a ``RETURN`` clause."""
        if not items:
            msg = "RETURN clause requires at least one item"
            raise ValueError(msg)
        expressions = [self._validate_expression(item, "RETURN item") for item in items]
        joined = ", ".join(expressions)
        self._clauses.append(f"RETURN {joined}")
        self._invalidate_cache()
        return self

    def order_by(
        self,
        expression: str,
        *,
        descending: bool = False,
    ) -> Neo4jQueryBuilders:
        """Append an ``ORDER BY`` clause."""
        value = self._validate_expression(expression, "ORDER BY expression")
        direction = " DESC" if descending else ""
        self._clauses.append(f"ORDER BY {value}{direction}")
        self._invalidate_cache()
        return self

    def limit(self, value: int) -> Neo4jQueryBuilders:
        """Append a ``LIMIT`` clause."""
        if not isinstance(value, int) or value <= 0:
            msg = "LIMIT must be a positive integer"
            raise ValueError(msg)
        self._clauses.append(f"LIMIT {value}")
        self._invalidate_cache()
        return self

    def set_parameter(
        self,
        name: str,
        value: object,
    ) -> Neo4jQueryBuilders:
        """Add or update a parameter explicitly."""
        parameter = self._validate_parameter_name(name)
        self._add_parameter(parameter, value)
        self._invalidate_cache()
        return self

    def build(self) -> tuple[str, dict[str, object]]:
        """Return the Cypher query string and bound parameters."""
        if not self._clauses:
            msg = "No clauses have been added"
            raise ValueError(msg)
        query = " ".join(self._clauses)
        parameters = dict(self._parameters)
        self._last_cache_key = self._plan_cache.make_key(query, parameters)
        return query, parameters

    def cache_plan(self, plan: object) -> None:
        """Cache a query plan for the last built query."""
        if self._last_cache_key is None:
            msg = "build() must be called before caching a plan"
            raise RuntimeError(msg)
        self._plan_cache.set(self._last_cache_key, plan)

    def get_cached_plan(self) -> object | None:
        """Return a cached plan for the last built query if available."""
        if self._last_cache_key is None:
            return None
        return self._plan_cache.get(self._last_cache_key)

    @property
    def parameters(self) -> Mapping[str, object]:
        """Return a read-only view of the current parameters."""
        return dict(self._parameters)

    def reset(self) -> None:
        """Clear all clauses and parameters."""
        self._clauses.clear()
        self._parameters.clear()
        self._parameter_names.clear()
        self._parameter_index = 0
        self._last_cache_key = None

    def _invalidate_cache(self) -> None:
        self._last_cache_key = None

    def _format_labels(
        self,
        labels: str | Sequence[str] | None,
    ) -> str:
        if labels is None:
            return ""
        if isinstance(labels, str):
            raw = [label for label in labels.split(":") if label]
        else:
            raw = []
            for label in labels:
                if not isinstance(label, str):
                    msg = "labels must contain strings"
                    raise TypeError(msg)
                raw.extend(part for part in label.split(":") if part)
        if not raw:
            return ""
        escaped = [self._escape_identifier(label) for label in raw]
        return ":" + ":".join(escaped)

    def _format_properties(
        self,
        alias: str,
        properties: Mapping[str, object] | None,
    ) -> str:
        if properties is None:
            return ""
        if not isinstance(properties, Mapping):
            msg = "properties must be a mapping"
            raise TypeError(msg)
        assignments: list[str] = []
        for name, value in properties.items():
            escaped = self._escape_identifier(name)
            parameter = self._unique_parameter_name(alias, name)
            self._add_parameter(parameter, value)
            assignments.append(f"{escaped}: ${parameter}")
        if not assignments:
            return ""
        joined = ", ".join(assignments)
        return f" {{{joined}}}"

    def _unique_parameter_name(
        self,
        alias: str,
        property_name: str,
    ) -> str:
        sanitized = (
            "".join(ch if ch.isalnum() else "_" for ch in property_name) or "value"
        )
        base = self._validate_parameter_name(f"{alias}_{sanitized}")
        if base not in self._parameter_names:
            self._parameter_names.add(base)
            return base
        while True:
            self._parameter_index += 1
            candidate = f"{base}_{self._parameter_index}"
            if candidate not in self._parameter_names:
                self._parameter_names.add(candidate)
                return candidate

    def _validate_alias(self, alias: str) -> str:
        if not isinstance(alias, str) or not alias.strip():
            msg = "alias must be a non-empty string"
            raise ValueError(msg)
        normalized = alias.strip()
        if not normalized[0].isalpha() and normalized[0] != "_":
            msg = "alias must start with a letter or underscore"
            raise ValueError(msg)
        if not all(ch.isalnum() or ch == "_" for ch in normalized):
            msg = f"Invalid alias: {alias}"
            raise ValueError(msg)
        return normalized

    def _validate_parameter_name(self, name: str) -> str:
        if not isinstance(name, str) or not name.strip():
            msg = "parameter name must be a non-empty string"
            raise ValueError(msg)
        normalized = name.strip()
        if not normalized[0].isalpha() and normalized[0] != "_":
            msg = "parameter name must start with a letter or underscore"
            raise ValueError(msg)
        if not all(ch.isalnum() or ch == "_" for ch in normalized):
            msg = f"Invalid parameter name: {name}"
            raise ValueError(msg)
        return normalized

    def _validate_expression(self, value: str, context: str) -> str:
        if not isinstance(value, str) or not value.strip():
            msg = f"{context} must be a non-empty string"
            raise ValueError(msg)
        if ";" in value:
            msg = f"{context} cannot contain semicolons"
            raise ValueError(msg)
        return value.strip()

    def _validate_operator(self, operator: str) -> str:
        if not isinstance(operator, str) or not operator.strip():
            msg = "operator must be a non-empty string"
            raise ValueError(msg)
        normalized = operator.strip().upper()
        allowed = {
            "=",
            "<>",
            ">",
            "<",
            ">=",
            "<=",
            "IN",
        }
        if normalized not in allowed:
            msg = f"Unsupported operator: {operator}"
            raise ValueError(msg)
        return normalized

    def _validate_sequence(self, value: object) -> Sequence[object]:
        if not isinstance(value, Sequence) or isinstance(value, (str, bytes)):
            msg = "value must be a sequence for IN comparisons"
            raise TypeError(msg)
        if not value:
            msg = "sequence value must not be empty"
            raise ValueError(msg)
        return list(value)

    def _escape_identifier(self, name: str) -> str:
        if not isinstance(name, str) or not name:
            msg = "identifier must be a non-empty string"
            raise ValueError(msg)
        if "`" in name:
            msg = "identifier cannot contain backticks"
            raise ValueError(msg)
        if name[0].isalpha() or name[0] == "_":
            if all(ch.isalnum() or ch == "_" for ch in name):
                return name
        if any(ch in name for ch in ";$"):
            msg = f"Invalid identifier: {name}"
            raise ValueError(msg)
        return f"`{name}`"

    def _add_parameter(self, name: str, value: object) -> None:
        if name in self._parameters and self._parameters[name] != value:
            msg = f"Parameter '{name}' already set"
            raise ValueError(msg)
        self._parameters[name] = value
        self._parameter_names.add(name)
