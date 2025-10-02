from __future__ import annotations

from pathlib import Path

import pandas as pd
from raphtory import Graph


class RaphtoryDataLoaders:
    """Load tabular data into a Raphtory graph."""

    def __init__(self, graph: Graph) -> None:
        """Create a new data loader for the provided ``graph``.

        Parameters
        ----------
        graph:
            The Raphtory graph instance that will receive the loaded data.

        """
        self.graph = graph

    def load_from_pandas(
        self,
        df: pd.DataFrame,
        time_col: str,
        source_col: str,
        destination_col: str,
        **properties: str,
    ) -> None:
        """Load edges from a DataFrame into ``graph``.

        Parameters
        ----------
        df:
            The DataFrame containing edge data.
        time_col:
            Column name for edge timestamps.
        source_col:
            Column name for source node identifiers.
        destination_col:
            Column name for destination node identifiers.
        **properties:
            Mapping of additional edge property names to
            DataFrame columns.

        """
        self.graph.load_edges_from_pandas(
            df,
            time_col,
            source_col,
            destination_col,
            **properties,
        )

    def load_from_csv(
        self,
        file_path: str | Path,
        time_col: str,
        source_col: str,
        destination_col: str,
        **properties: str,
    ) -> None:
        """Load edges from a CSV file into ``graph``.

        Parameters
        ----------
        file_path:
            Path to the CSV file.
        time_col:
            Column name for edge timestamps.
        source_col:
            Column name for source node identifiers.
        destination_col:
            Column name for destination node identifiers.
        **properties:
            Mapping of edge property names to CSV
            columns.

        """
        df = pd.read_csv(file_path)
        required = {
            time_col,
            source_col,
            destination_col,
            *properties.values(),
        }
        missing = required.difference(df.columns)
        if missing:
            missing_cols = ", ".join(sorted(missing))
            msg = f"CSV missing columns: {missing_cols}"
            raise ValueError(msg)

        self.load_from_pandas(
            df,
            time_col,
            source_col,
            destination_col,
            **properties,
        )

    def add_nodes_batch(
        self,
        df: pd.DataFrame,
        time_col: str,
        id_col: str,
        **properties: str,
    ) -> None:
        """Add nodes to ``graph`` from ``df``.

        Parameters
        ----------
        df:
            DataFrame containing node data.
        time_col:
            Column name for node timestamps.
        id_col:
            Column name for node identifiers.
        **properties:
            Mapping of node property names to
            DataFrame columns.

        """
        for row in df.itertuples(index=False):
            data = row._asdict()
            props = {name: data[col] for name, col in properties.items()}
            self.graph.add_node(
                data[time_col],
                data[id_col],
                props,
            )

    def add_edges_batch(
        self,
        df: pd.DataFrame,
        time_col: str,
        source_col: str,
        destination_col: str,
        layer_col: str | None = None,
        **properties: str,
    ) -> None:
        """Add edges to ``graph`` from ``df``.

        Parameters
        ----------
        df:
            DataFrame containing edge data.
        time_col:
            Column name for edge timestamps.
        source_col:
            Column name for source node identifiers.
        destination_col:
            Column name for destination node identifiers.
        layer_col:
            Optional column name for edge layer.
        **properties:
            Mapping of edge property names to
            DataFrame columns.

        """
        for row in df.itertuples(index=False):
            data = row._asdict()
            props = {name: data[col] for name, col in properties.items()}
            args = [
                data[time_col],
                data[source_col],
                data[destination_col],
                props,
            ]
            if layer_col is not None:
                args.append(data[layer_col])
            self.graph.add_edge(*args)
