from __future__ import annotations

from collections.abc import Iterable, Iterator, Mapping
from pathlib import Path
from typing import Any, Protocol

import networkx as nx
import pandas as pd
from neo4j import READ_ACCESS

from bclearer_interop_services.graph_services.neo4j_service.object_models.neo4j_sessions import (
    Neo4jSessions,
)

_NODE_EXPORT_QUERY = (
    "MATCH (n) "
    "WHERE $node_label IS NULL OR $node_label IN labels(n) "
    "RETURN id(n) AS id, labels(n) AS labels, properties(n) AS properties"
)

_RELATIONSHIP_EXPORT_QUERY = (
    "MATCH (source)-[r]->(target) "
    "WHERE ($node_label IS NULL OR $node_label IN labels(source)) "
    "AND ($rel_type IS NULL OR type(r) = $rel_type) "
    "RETURN id(r) AS id, id(source) AS source, id(target) AS target, "
    "type(r) AS type, properties(r) AS properties"
)


class SupportsData(Protocol):
    """Protocol for Neo4j records exposing ``data``."""

    def data(self) -> Mapping[str, object]:
        """Return a mapping representation of the record."""


class Neo4jDataExporters:
    """Export data from Neo4j into tabular and graph formats."""

    def __init__(self, session: Neo4jSessions) -> None:
        """Create a new exporter backed by ``session``."""
        self.session = session
        self._connection = session.connection
        self._database = session.database_name

    def to_dataframe(
        self,
        query: str,
        parameters: Mapping[str, object] | None = None,
    ) -> pd.DataFrame:
        """Execute ``query`` and return the result as a DataFrame."""
        if not isinstance(query, str) or not query.strip():
            msg = "query must be a non-empty string"
            raise ValueError(msg)
        params = dict(parameters or {})
        records = self.session.execute_read(query, params)
        rows = [self._record_to_dict(record) for record in records]
        return pd.DataFrame(rows)

    def to_networkx(
        self,
        *,
        node_label: str | None = None,
        relationship_type: str | None = None,
    ) -> nx.MultiDiGraph:
        """Return the database contents as a NetworkX ``MultiDiGraph``."""
        nodes = self._execute_export_query(
            _NODE_EXPORT_QUERY,
            {"node_label": node_label},
        )
        relationships = self._execute_export_query(
            _RELATIONSHIP_EXPORT_QUERY,
            {"node_label": node_label, "rel_type": relationship_type},
        )
        graph = nx.MultiDiGraph()
        for node in nodes:
            node_id = node["id"]
            properties = self._ensure_mapping(node.get("properties"))
            labels = list(node.get("labels", []))
            graph.add_node(node_id, labels=labels, **properties)
        for relationship in relationships:
            properties = self._ensure_mapping(
                relationship.get("properties"),
            )
            source = relationship["source"]
            target = relationship["target"]
            key = relationship.get("id")
            rel_type = relationship.get("type")
            if source not in graph:
                graph.add_node(source)
            if target not in graph:
                graph.add_node(target)
            graph.add_edge(
                source,
                target,
                key=key,
                type=rel_type,
                **properties,
            )
        return graph

    def to_table_dictionary(self) -> dict[str, Any]:
        """Return the graph contents as B-Dictionary tables."""
        from bclearer_orchestration_services.identification_services.b_identity_ecosystem.bie_id_creators.bie_id_for_single_object_creator import (  # noqa: PLC0415
            create_bie_id_for_single_object,
        )

        from bclearer_interop_services.b_dictionary_service.dataframe_to_table_b_dictionary_converter import (  # noqa: PLC0415
            convert_dataframe_to_table_b_dictionary,
        )

        graph = self.to_networkx()
        node_rows = [{"id": node, **data} for node, data in graph.nodes(data=True)]
        relationship_rows = [
            {"source": source, "target": target, "id": key, **data}
            for source, target, key, data in graph.edges(
                data=True,
                keys=True,
            )
        ]
        node_frame = pd.DataFrame(node_rows)
        relationship_frame = pd.DataFrame(relationship_rows)

        node_table = convert_dataframe_to_table_b_dictionary(
            dataframe=node_frame,
            table_name="neo4j_nodes",
            bie_table_id=create_bie_id_for_single_object(
                "neo4j_nodes",
            ),
        )
        relationship_table = convert_dataframe_to_table_b_dictionary(
            dataframe=relationship_frame,
            table_name="neo4j_relationships",
            bie_table_id=create_bie_id_for_single_object(
                "neo4j_relationships",
            ),
        )
        return {
            "nodes": node_table,
            "relationships": relationship_table,
        }

    def to_graphml(self, file_path: str | Path) -> None:
        """Export the graph to a GraphML file."""
        path = Path(file_path)
        if path.suffix.lower() != ".graphml":
            msg = "file_path must end with .graphml"
            raise ValueError(msg)
        if not path.parent.exists():
            msg = f"directory does not exist: {path.parent}"
            raise FileNotFoundError(msg)
        graph = self.to_networkx()
        try:
            nx.write_graphml(
                graph,
                path,
                encoding="utf-8",
                prettyprint=True,
            )
        except OSError as exc:  # pragma: no cover - IO failures
            msg = f"failed to write GraphML to {path}"
            raise OSError(msg) from exc

    def stream_results(
        self,
        query: str,
        parameters: Mapping[str, object] | None = None,
        *,
        chunk_size: int = 1000,
    ) -> Iterator[pd.DataFrame]:
        """Yield DataFrames containing ``chunk_size`` rows of ``query`` results."""
        if not isinstance(query, str) or not query.strip():
            msg = "query must be a non-empty string"
            raise ValueError(msg)
        if chunk_size <= 0:
            msg = "chunk_size must be a positive integer"
            raise ValueError(msg)
        params = dict(parameters or {})
        driver = self._connection.get_driver()
        with driver.session(
            database=self._database,
            default_access_mode=READ_ACCESS,
        ) as neo4j_session:
            result = neo4j_session.run(query, params)
            chunk: list[dict[str, object]] = []
            for record in result:
                chunk.append(self._record_to_dict(record))
                if len(chunk) >= chunk_size:
                    yield pd.DataFrame(chunk)
                    chunk.clear()
            if chunk:
                yield pd.DataFrame(chunk)

    def _execute_export_query(
        self,
        query: str,
        parameters: Mapping[str, object],
    ) -> list[dict[str, object]]:
        records = self.session.execute_read(query, dict(parameters))
        return [self._record_to_dict(record) for record in records]

    @staticmethod
    def _record_to_dict(
        record: SupportsData | Mapping[str, object] | Iterable[tuple[str, object]],
    ) -> dict[str, object]:
        if isinstance(record, Mapping):
            data = record
        elif hasattr(record, "data"):
            data = record.data()
        else:
            try:
                data = dict(record)
            except TypeError as exc:  # pragma: no cover - defensive
                msg = "record must be convertible to a mapping"
                raise TypeError(msg) from exc
        if not isinstance(data, Mapping):
            msg = "record data must be a mapping"
            raise TypeError(msg)
        return dict(data)

    @staticmethod
    def _ensure_mapping(value: Mapping[str, object] | None) -> dict[str, object]:
        if value is None:
            return {}
        if isinstance(value, Mapping):
            return dict(value)
        msg = "properties must be a mapping when present"
        raise TypeError(msg)
