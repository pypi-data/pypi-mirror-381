"""Raphtory algorithm execution wrappers."""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass
from itertools import islice
from typing import Protocol

import networkx as nx
from raphtory import Graph, algorithms


class _NodeStateLike(Protocol):
    def items(self) -> Iterator[tuple[object, float]]:
        """Return node/value pairs."""


@dataclass
class RaphtoryAlgorithms:
    """Execute algorithms on a Raphtory graph."""

    graph: Graph

    def _node_state_to_dict(
        self,
        state: _NodeStateLike,
    ) -> dict[str, float]:
        """Convert Raphtory NodeState to dict."""
        return {node.name: value for node, value in state.items()}

    def pagerank(
        self,
        *,
        iter_count: int = 20,
        max_diff: float | None = None,
        use_l2_norm: bool = True,
        damping_factor: float = 0.85,
    ) -> dict[str, float]:
        """Run PageRank on the graph."""
        state = algorithms.pagerank(
            self.graph,
            iter_count=iter_count,
            max_diff=max_diff,
            use_l2_norm=use_l2_norm,
            damping_factor=damping_factor,
        )
        return self._node_state_to_dict(state)

    def clustering_coefficient(
        self,
        nodes: list[str] | None = None,
    ) -> dict[str, float]:
        """Compute clustering coefficients."""
        if nodes is None:
            nodes = [node.name for node in self.graph.nodes]
        state = algorithms.local_clustering_coefficient_batch(
            self.graph,
            nodes,
        )
        return self._node_state_to_dict(state)

    def shortest_path(
        self,
        source: str,
        target: str,
        *,
        weight: str | None = None,
        timeout: float | None = None,
    ) -> list[str]:
        """Return the shortest path between ``source`` and ``target``.

        If ``weight`` is provided, the graph is converted to a NetworkX graph and
        the weighted shortest path is computed using NetworkX's implementation.

        ``timeout`` controls how long the Raphtory search may run before
        terminating. This parameter is ignored when using the NetworkX fallback.
        """
        if weight is not None:
            nx_graph = self.graph.to_networkx()
            return nx.shortest_path(
                nx_graph,
                source=source,
                target=target,
                weight=weight,
            )
        path = algorithms.shortest_path(
            self.graph,
            source,
            target,
            timeout=timeout,
        )
        return [node.name for node in path]

    def degree_centrality(
        self,
        *,
        limit: int | None = None,
    ) -> dict[str, float]:
        """Compute degree centrality for nodes."""
        state = algorithms.degree_centrality(self.graph)
        centrality = self._node_state_to_dict(state)
        if limit is not None:
            return dict(islice(centrality.items(), limit))
        return centrality

    def connected_components(
        self,
        *,
        limit: int | None = None,
    ) -> list[list[str]]:
        """Return graph connected components."""
        nx_graph = self.graph.to_networkx().to_undirected()
        components: Iterator[set[str]] = nx.connected_components(nx_graph)
        if limit is not None:
            components = islice(components, limit)
        return [sorted(component) for component in components]
