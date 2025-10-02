"""Raphtory graph vectorisation utilities."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from dataclasses import dataclass, field
from pathlib import Path

from langchain.embeddings import HuggingFaceEmbeddings
from raphtory import Graph
from raphtory.vectors import VectorisedGraph, VectorSelection


@dataclass
class RaphtoryVectorizations:
    """Handle graph vectorisation."""

    graph: Graph
    embedding_model: str = "thenlper/gte-small"
    _vectorised: VectorisedGraph | None = field(
        default=None,
        init=False,
    )

    def vectorize_graph(
        self,
        embedding_fn: Callable[[str], list[float]] | None = None,
    ) -> VectorisedGraph:
        """Vectorise graph using an embedding fn.

        If no embedding function is supplied, use a HuggingFace model
        configured via ``embedding_model``.
        """
        if embedding_fn is None:
            embedding_fn = HuggingFaceEmbeddings(
                model_name=self.embedding_model,
            ).embed_query
        self._vectorised = self.graph.vectorise(embedding_fn)
        return self._vectorised

    def get_embeddings(self) -> VectorisedGraph:
        """Return cached graph embeddings."""
        if self._vectorised is None:
            self.vectorize_graph()
        return self._vectorised

    def cache_embeddings(self, path: str | Path) -> None:
        """Persist embeddings to a cache file."""
        self.get_embeddings()
        self.graph.cache(str(path))

    def similarity_search(
        self,
        query: Sequence[float] | str,
        limit: int,
        window: tuple[int | str, int | str] | None = None,
    ) -> VectorSelection:
        """Find graph entities similar to a query."""
        vectorised = self.get_embeddings()
        return vectorised.entities_by_similarity(query, limit, window)
