from __future__ import annotations

from pathlib import Path
from typing import Any

import networkx as nx
import pandas as pd
from raphtory import Graph


class RaphtoryDataExporters:
    """Export data from a Raphtory graph."""

    def __init__(self, graph: Graph) -> None:
        """Create a new exporter for ``graph``."""
        self.graph = graph

    def to_networkx(self) -> nx.DiGraph:
        """Return ``graph`` as a NetworkX ``DiGraph``."""
        return self.graph.to_networkx()

    def to_pandas_nodes(self) -> pd.DataFrame:
        """Return nodes of ``graph`` as a ``DataFrame``."""
        nx_graph = self.to_networkx()
        rows = [{"id": node, **data} for node, data in nx_graph.nodes(data=True)]
        return pd.DataFrame(rows)

    def to_pandas_edges(self) -> pd.DataFrame:
        """Return edges of ``graph`` as a ``DataFrame``."""
        nx_graph = self.to_networkx()
        rows = [
            {"source": u, "destination": v, **data}
            for u, v, data in nx_graph.edges(data=True)
        ]
        return pd.DataFrame(rows)

    def to_table_dictionary(self) -> dict[str, Any]:
        """Return ``graph`` as B-Dictionary tables."""
        from bclearer_orchestration_services.identification_services.b_identity_ecosystem.bie_id_creators.bie_id_for_single_object_creator import (  # noqa: PLC0415
            create_bie_id_for_single_object,
        )

        from bclearer_interop_services.b_dictionary_service.dataframe_to_table_b_dictionary_converter import (  # noqa: PLC0415
            convert_dataframe_to_table_b_dictionary,
        )

        nodes = self.to_pandas_nodes()
        edges = self.to_pandas_edges()

        node_id = create_bie_id_for_single_object(
            "raphtory_nodes",
        )
        edge_id = create_bie_id_for_single_object(
            "raphtory_edges",
        )

        node_table = convert_dataframe_to_table_b_dictionary(
            dataframe=nodes,
            table_name="raphtory_nodes",
            bie_table_id=node_id,
        )
        edge_table = convert_dataframe_to_table_b_dictionary(
            dataframe=edges,
            table_name="raphtory_edges",
            bie_table_id=edge_id,
        )

        return {
            "nodes": node_table,
            "edges": edge_table,
        }

    def to_graphml(self, file_path: str | Path) -> None:
        """Export ``graph`` to GraphML at ``file_path``."""
        path = Path(file_path)
        if path.suffix != ".graphml":
            raise ValueError(
                "file_path must end with .graphml",
            )
        if not path.parent.exists():
            raise FileNotFoundError(
                f"directory does not exist: {path.parent}",
            )
        nx_graph = self.to_networkx()
        try:
            nx.write_graphml(
                nx_graph,
                path,
                encoding="utf-8",
                prettyprint=True,
            )
        except OSError as err:
            msg = f"failed to write GraphML to {path}"
            raise OSError(msg) from err
