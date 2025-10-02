"""Wrappers for Neo4j Graph Data Science algorithms."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

from neo4j import READ_ACCESS, WRITE_ACCESS, Driver

from .neo4j_connection_pools import Neo4jConnectionPools


@dataclass
class Neo4jAlgorithms:
    """Execute graph algorithms through the Neo4j GDS library."""

    pool: Neo4jConnectionPools
    database_name: str = "neo4j"
    last_path_cost: float | None = None

    def pagerank(
        self,
        graph_name: str,
        *,
        config: Mapping[str, Any] | None = None,
        limit: int | None = None,
        id_property: str | None = None,
    ) -> dict[str, float]:
        """Return PageRank scores for the projected graph."""
        payload: dict[str, Any] = {
            "graph_name": self._validate_graph_name(graph_name),
            "config": self._normalise_config(config),
        }
        validated_limit = self._validate_limit(limit)
        query = (
            "CALL gds.pageRank.stream($graph_name, $config) "
            "YIELD nodeId, score "
            "RETURN gds.util.asNode(nodeId) AS node, score "
            "ORDER BY score DESC"
        )
        if validated_limit is not None:
            payload["limit"] = validated_limit
            query = f"{query} LIMIT $limit"
        records = self._run_stream(query, payload)
        return {
            self._node_identifier(record["node"], id_property): record["score"]
            for record in records
        }

    def community_detection(
        self,
        graph_name: str,
        *,
        algorithm: str = "louvain",
        config: Mapping[str, Any] | None = None,
        id_property: str | None = None,
    ) -> dict[str, int]:
        """Run the chosen community detection algorithm."""
        procedure = self._community_procedure(algorithm)
        payload = {
            "graph_name": self._validate_graph_name(graph_name),
            "config": self._normalise_config(config),
        }
        query = (
            f"CALL {procedure}($graph_name, $config) "
            "YIELD nodeId, communityId "
            "RETURN gds.util.asNode(nodeId) AS node, communityId "
            "ORDER BY communityId"
        )
        records = self._run_stream(query, payload)
        return {
            self._node_identifier(record["node"], id_property): record["communityId"]
            for record in records
        }

    def shortest_path(
        self,
        graph_name: str,
        source: str,
        target: str,
        *,
        id_property: str | None = None,
        weight_property: str | None = None,
    ) -> list[str]:
        """Return the node identifiers that make up the shortest path."""
        payload: dict[str, Any] = {
            "graph_name": self._validate_graph_name(graph_name),
            "source": self._validate_identifier(source, "source"),
            "target": self._validate_identifier(target, "target"),
        }
        if weight_property is not None:
            if not isinstance(weight_property, str) or not weight_property:
                msg = "weight_property must be a non-empty string"
                raise ValueError(msg)
            payload["weight_property"] = weight_property
        if id_property is None:
            match_clause = (
                "MATCH (source) WHERE elementId(source) = $source "
                "MATCH (target) WHERE elementId(target) = $target "
            )
        else:
            property_name = self._validate_property_name(id_property)
            match_clause = (
                f"MATCH (source) WHERE source.{property_name} = $source "
                f"MATCH (target) WHERE target.{property_name} = $target "
            )
        config_parts = [
            "sourceNode: id(source)",
            "targetNode: id(target)",
        ]
        if weight_property is not None:
            config_parts.append(
                "relationshipWeightProperty: $weight_property",
            )
        config = ", ".join(config_parts)
        query = (
            f"{match_clause}"
            "CALL gds.shortestPath.dijkstra.stream("
            f"$graph_name, {{{config}}}) "
            "YIELD nodeIds, totalCost "
            "RETURN gds.util.asNodes(nodeIds) AS nodes, totalCost"
        )
        records = self._run_stream(query, payload)
        if not records:
            self.last_path_cost = None
            return []
        result = records[0]
        self.last_path_cost = result.get("totalCost")
        nodes = result.get("nodes", [])
        return [self._node_identifier(node, id_property) for node in nodes]

    def similarity(
        self,
        *,
        index_name: str | None = None,
        vector: Sequence[float] | None = None,
        graph_name: str | None = None,
        embedding_property: str | None = None,
        top_k: int = 10,
        id_property: str | None = None,
        filters: Mapping[str, Any] | None = None,
        similarity_metric: str = "cosine",
        source: str | None = None,
    ) -> list[dict[str, Any]]:
        """Execute a vector similarity search."""
        validated_top_k = self._validate_limit(top_k)
        if validated_top_k is None:
            validated_top_k = 10
        if index_name is not None:
            if vector is None:
                msg = "vector must be provided when using index_name"
                raise ValueError(msg)
            return self._vector_index_similarity(
                index_name,
                vector,
                validated_top_k,
                id_property,
                filters,
            )
        if graph_name is not None:
            if embedding_property is None:
                msg = "embedding_property must be provided when graph_name is set"
                raise ValueError(msg)
            return self._graph_similarity(
                graph_name,
                embedding_property,
                validated_top_k,
                similarity_metric,
                id_property,
                source,
            )
        msg = "Either index_name or graph_name must be provided"
        raise ValueError(msg)

    def call_procedure(
        self,
        procedure: str,
        *,
        arguments: Mapping[str, Any] | Sequence[Any] | None = None,
        yield_fields: Sequence[str] | None = None,
        write: bool = False,
        id_properties: Mapping[str, str] | None = None,
    ) -> list[dict[str, Any]]:
        """Call an arbitrary Neo4j procedure and format the result."""
        validated_name = self._validate_procedure_name(procedure)
        clause, payload = self._build_argument_clause(arguments)
        yield_clause = ""
        if yield_fields:
            validated_fields = [
                self._validate_parameter_name(field, "yield field")
                for field in yield_fields
            ]
            yield_clause = f" YIELD {', '.join(validated_fields)}"
        query = f"CALL {validated_name}{clause}{yield_clause}"
        records = self._run_stream(
            query,
            payload,
            access_mode=WRITE_ACCESS if write else READ_ACCESS,
        )
        return self._format_records(records, id_properties=id_properties)

    def _run_stream(
        self,
        query: str,
        parameters: Mapping[str, Any],
        *,
        access_mode: str = READ_ACCESS,
    ) -> list[dict[str, Any]]:
        payload = dict(parameters)

        def operation(driver: Driver) -> list[dict[str, Any]]:
            with driver.session(
                database=self.database_name,
                default_access_mode=access_mode,
            ) as session:
                result = session.run(query, payload)
                return [record.data() for record in result]

        return self.pool.execute_with_retry(operation)

    def _vector_index_similarity(
        self,
        index_name: str,
        vector: Sequence[float],
        top_k: int,
        id_property: str | None,
        filters: Mapping[str, Any] | None,
    ) -> list[dict[str, Any]]:
        validated_index = self._validate_identifier(index_name, "index_name")
        payload: dict[str, Any] = {
            "index_name": validated_index,
            "top_k": top_k,
            "query_vector": self._normalise_vector(vector),
        }
        options = {"includeMetadata": True}
        normalized_filters = self._normalise_filters(filters)
        if normalized_filters:
            options["filter"] = normalized_filters
        if options:
            payload["options"] = options
        query_parts = [
            "CALL db.index.vector.queryNodes(",
            "$index_name, $top_k, $query_vector",
        ]
        if "options" in payload:
            query_parts.append(", $options")
        query_parts.append(") YIELD node, score, metadata ")
        query_parts.append(
            "RETURN gds.util.asNode(node) AS node, score, metadata "
            "ORDER BY score DESC"
        )
        query = "".join(query_parts)
        records = self._run_stream(query, payload)
        formatted = self._format_records(
            records,
            id_properties={"node": id_property} if id_property else None,
        )
        return [self._format_vector_result(record) for record in formatted]

    def _graph_similarity(
        self,
        graph_name: str,
        embedding_property: str,
        top_k: int,
        similarity_metric: str,
        id_property: str | None,
        source: str | None,
    ) -> list[dict[str, Any]]:
        payload: dict[str, Any] = {
            "graph_name": self._validate_graph_name(graph_name),
            "config": {
                "nodeProperties": self._validate_property_name(
                    embedding_property
                ),
                "topK": top_k,
                "similarityMetric": self._validate_similarity_metric(
                    similarity_metric
                ),
            },
        }
        query = (
            "CALL gds.similarity.knn.stream($graph_name, $config) "
            "YIELD node1, node2, similarity "
            "RETURN gds.util.asNode(node1) AS node1, "
            "gds.util.asNode(node2) AS node2, similarity "
            "ORDER BY similarity DESC"
        )
        records = self._run_stream(query, payload)
        formatted = self._format_records(
            records,
            id_properties={"node1": id_property, "node2": id_property}
            if id_property
            else None,
        )
        pairs = [self._format_pair_result(record) for record in formatted]
        if source is not None:
            source_id = self._validate_identifier(source, "source")
            pairs = [
                pair
                for pair in pairs
                if pair["source"] == source_id or pair["target"] == source_id
            ]
        return pairs

    def _format_vector_result(
        self,
        record: Mapping[str, Any],
    ) -> dict[str, Any]:
        result = {
            "node": record.get("node"),
            "score": float(record.get("score", 0.0)),
        }
        metadata = record.get("metadata")
        if metadata is not None:
            result["metadata"] = metadata
        return result

    def _format_pair_result(
        self,
        record: Mapping[str, Any],
    ) -> dict[str, Any]:
        return {
            "source": record.get("node1"),
            "target": record.get("node2"),
            "score": float(record.get("similarity", 0.0)),
        }

    def _format_records(
        self,
        records: list[dict[str, Any]],
        *,
        id_properties: Mapping[str, str] | None = None,
    ) -> list[dict[str, Any]]:
        if id_properties is None:
            id_properties = {}
        formatted: list[dict[str, Any]] = []
        for record in records:
            formatted_record: dict[str, Any] = {}
            for key, value in record.items():
                formatted_record[key] = self._format_value(
                    value,
                    id_properties.get(key),
                )
            formatted.append(formatted_record)
        return formatted

    def _format_value(
        self,
        value: Any,
        id_property: str | None,
    ) -> Any:
        if self._looks_like_node(value):
            return self._node_identifier(value, id_property)
        if isinstance(value, list):
            return [self._format_value(item, id_property) for item in value]
        if isinstance(value, Mapping):
            return {
                str(key): self._format_value(item, id_property)
                for key, item in value.items()
            }
        return value

    def _looks_like_node(self, value: Any) -> bool:
        return hasattr(value, "element_id") or hasattr(value, "id")

    def _validate_similarity_metric(self, metric: str) -> str:
        if not isinstance(metric, str) or not metric.strip():
            msg = "similarity_metric must be a non-empty string"
            raise ValueError(msg)
        normalized = metric.strip().upper()
        allowed = {"COSINE", "EUCLIDEAN", "DOT"}
        if normalized not in allowed:
            msg = f"Unsupported similarity metric: {metric}"
            raise ValueError(msg)
        return normalized

    def _normalise_filters(
        self,
        filters: Mapping[str, Any] | None,
    ) -> dict[str, Any]:
        if filters is None:
            return {}
        if not isinstance(filters, Mapping):
            msg = "filters must be a mapping"
            raise TypeError(msg)
        return dict(filters)

    def _normalise_vector(self, vector: Sequence[float]) -> list[float]:
        if not isinstance(vector, Sequence) or isinstance(vector, (str, bytes)):
            msg = "vector must be a sequence of numbers"
            raise TypeError(msg)
        values = [float(value) for value in vector]
        if not values:
            msg = "vector must contain at least one value"
            raise ValueError(msg)
        return values

    def _build_argument_clause(
        self,
        arguments: Mapping[str, Any] | Sequence[Any] | None,
    ) -> tuple[str, dict[str, Any]]:
        if arguments is None:
            return "", {}
        payload: dict[str, Any] = {}
        if isinstance(arguments, Mapping):
            placeholders: list[str] = []
            for key, value in arguments.items():
                param_name = self._validate_parameter_name(key, "argument name")
                placeholders.append(f"${param_name}")
                payload[param_name] = value
            clause = f"({', '.join(placeholders)})" if placeholders else ""
            return clause, payload
        placeholders = []
        for index, value in enumerate(arguments):
            param_name = f"arg_{index}"
            placeholders.append(f"${param_name}")
            payload[param_name] = value
        clause = f"({', '.join(placeholders)})" if placeholders else ""
        return clause, payload

    def _validate_procedure_name(self, procedure: str) -> str:
        if not isinstance(procedure, str) or not procedure.strip():
            msg = "procedure must be a non-empty string"
            raise ValueError(msg)
        normalized = procedure.strip()
        allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._")
        if not set(normalized) <= allowed:
            msg = f"Invalid procedure name: {procedure}"
            raise ValueError(msg)
        return normalized

    def _validate_parameter_name(
        self,
        name: str,
        context: str,
    ) -> str:
        if not isinstance(name, str) or not name.strip():
            msg = f"{context} must be a non-empty string"
            raise ValueError(msg)
        normalized = name.strip()
        if not normalized.replace("_", "").isalnum():
            msg = f"Invalid {context}: {name}"
            raise ValueError(msg)
        return normalized

    def _normalise_config(
        self,
        config: Mapping[str, Any] | None,
    ) -> dict[str, Any]:
        if config is None:
            return {}
        if not isinstance(config, Mapping):
            msg = "config must be a mapping"
            raise TypeError(msg)
        return dict(config)

    def _validate_graph_name(self, graph_name: str) -> str:
        if not isinstance(graph_name, str) or not graph_name.strip():
            msg = "graph_name must be a non-empty string"
            raise ValueError(msg)
        return graph_name

    def _validate_limit(self, limit: int | None) -> int | None:
        if limit is None:
            return None
        if not isinstance(limit, int) or limit <= 0:
            msg = "limit must be a positive integer"
            raise ValueError(msg)
        return limit

    def _validate_identifier(self, value: str, parameter: str) -> str:
        if not isinstance(value, str) or not value:
            msg = f"{parameter} must be a non-empty string"
            raise ValueError(msg)
        return value

    def _validate_property_name(self, property_name: str) -> str:
        if not isinstance(property_name, str) or not property_name:
            msg = "id_property must be a non-empty string"
            raise ValueError(msg)
        normalized = property_name.replace("_", "")
        if not normalized.isalnum():
            msg = f"Invalid property name: {property_name}"
            raise ValueError(msg)
        return property_name

    def _community_procedure(self, algorithm: str) -> str:
        if not isinstance(algorithm, str) or not algorithm.strip():
            msg = "algorithm must be a non-empty string"
            raise ValueError(msg)
        normalized = algorithm.strip().lower().replace("-", "_")
        procedures = {
            "louvain": "gds.louvain.stream",
            "leiden": "gds.leiden.stream",
            "label_propagation": "gds.labelPropagation.stream",
        }
        if normalized not in procedures:
            msg = f"Unsupported community detection algorithm: {algorithm}"
            raise ValueError(msg)
        return procedures[normalized]

    def _node_identifier(
        self,
        node: object,
        id_property: str | None,
    ) -> str:
        if id_property:
            value = self._node_property(node, id_property)
            if value is not None:
                return str(value)
        element_id = getattr(node, "element_id", None)
        if element_id is not None:
            return str(element_id)
        legacy_id = getattr(node, "id", None)
        if legacy_id is not None:
            return str(legacy_id)
        if hasattr(node, "__str__"):
            return str(node)
        raise TypeError("Unable to derive node identifier")

    def _node_property(
        self,
        node: object,
        property_name: str,
    ) -> object | None:
        getter = getattr(node, "get", None)
        if callable(getter):
            value = getter(property_name, None)
            if value is not None:
                return value
        accessor = getattr(node, "__getitem__", None)
        if callable(accessor):
            try:
                return accessor(property_name)
            except Exception:
                return None
        return None
