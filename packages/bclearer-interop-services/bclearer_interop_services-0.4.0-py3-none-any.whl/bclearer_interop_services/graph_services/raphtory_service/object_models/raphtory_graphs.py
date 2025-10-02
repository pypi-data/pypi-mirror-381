"""Raphtory graph management utilities."""

from __future__ import annotations

import gc

from raphtory import Graph


class RaphtoryGraphs:
    """Manage Raphtory graph instances."""

    def __init__(self) -> None:
        self._graphs: dict[str, Graph] = {}

    def create_graph(
        self,
        name: str,
        **graph_kwargs: object,
    ) -> Graph:
        """Create a new Raphtory graph.

        Raises:
            ValueError: If the graph name exists.
            MemoryError: If graph creation fails.

        """
        if name in self._graphs:
            raise ValueError(
                f"Graph '{name}' already exists",
            )
        try:
            graph = Graph(**graph_kwargs)
        except MemoryError as exc:
            raise MemoryError(
                "Insufficient memory to create graph",
            ) from exc
        self._graphs[name] = graph
        return graph

    def get_graph(self, name: str) -> Graph:
        """Retrieve a managed Raphtory graph."""
        try:
            return self._graphs[name]
        except KeyError as exc:
            raise KeyError(
                f"Graph '{name}' not found",
            ) from exc

    def delete_graph(self, name: str) -> None:
        """Delete a graph and free its resources."""
        graph = self._graphs.pop(name, None)
        if graph is not None:
            del graph
            gc.collect()

    def save_graph(
        self,
        name: str,
        path: str,
    ) -> None:
        """Persist a graph to disk.

        Raises:
            KeyError: If the graph name does not exist.
            OSError: If the file cannot be written.

        """
        graph = self.get_graph(name)
        try:
            graph.save_to_file(path)
        except OSError as exc:
            raise OSError(
                f"Failed to save graph '{name}' to '{path}'",
            ) from exc

    def load_graph(
        self,
        name: str,
        path: str,
    ) -> Graph:
        """Load a persisted graph and manage it.

        Raises:
            ValueError: If the graph name exists.
            OSError: If the file cannot be read.
            MemoryError: If loading requires more memory than available.

        """
        if name in self._graphs:
            raise ValueError(
                f"Graph '{name}' already exists",
            )
        try:
            graph = Graph.load_from_file(path)
        except MemoryError as exc:
            raise MemoryError(
                "Insufficient memory to load graph",
            ) from exc
        except OSError as exc:
            raise OSError(
                f"Failed to load graph from '{path}'",
            ) from exc
        self._graphs[name] = graph
        return graph
