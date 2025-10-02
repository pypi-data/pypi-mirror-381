from __future__ import annotations

import gc
import logging
import os
import tempfile
import time
from collections.abc import Callable
from concurrent.futures import (
    FIRST_COMPLETED,
    Future,
    ThreadPoolExecutor,
    wait,
)
from threading import Lock, Semaphore

import pandas as pd
import psutil

from bclearer_interop_services.graph_services.neo4j_service.object_models.neo4j_databases import (
    Neo4jDatabases,
)
from bclearer_interop_services.graph_services.neo4j_service.orchestrators.neo4j_edge_loaders import (
    EdgeLoader,
)
from bclearer_interop_services.graph_services.neo4j_service.orchestrators.neo4j_node_loaders import (
    NodeLoader,
)

logger = logging.getLogger(__name__)


class Neo4jDataLoaders:
    """Load tabular data into Neo4j."""

    def __init__(
        self,
        neo4j_database: Neo4jDatabases,
        batch_size: int = 10_000,
        target_rate: int = 100_000,
        workers: int = 4,
        memory_limit: int = 2 * 1024**3,
    ) -> None:
        """Create data loaders for ``neo4j_database``."""
        self.neo4j_database = neo4j_database
        self.default_batch_size = batch_size
        self.current_batch_size = batch_size
        self.target_rate = target_rate
        self.workers = workers
        self.memory_limit = memory_limit
        self._semaphore = Semaphore(workers)
        self.min_batch_size = max(1, batch_size // 10)
        self.max_batch_size = batch_size * 10
        self.node_loader = NodeLoader(
            neo4j_database=neo4j_database,
            batch_size=batch_size,
        )
        self.edge_loader = EdgeLoader(
            neo4j_database=neo4j_database,
            batch_size=batch_size,
        )

    def upsert_nodes(
        self,
        nodes_df: pd.DataFrame,
        merge_query: str,
        progress_callback: Callable[[int, int], None] | None = None,
        performance_callback: Callable[[int, float], None] | None = None,
    ) -> None:
        """Upsert nodes using ``merge_query``.

        Args:
            nodes_df: DataFrame of node properties.
            merge_query: Cypher MERGE query for nodes.
            progress_callback: Optional callback accepting
                ``(loaded, total)`` counts.
            performance_callback: Optional callback
                receiving ``(rows, seconds)`` for each batch.

        """
        total = len(nodes_df)
        if total == 0:
            return

        if nodes_df.memory_usage(deep=True).sum() > self.memory_limit:
            logger.warning(
                "Nodes DataFrame exceeds %.2fGB limit; spilling to disk",
                self.memory_limit / 1024**3,
            )
            self._spill_to_disk(
                df=nodes_df,
                query=merge_query,
                loader=self.node_loader.load_nodes,
                loader_obj=self.node_loader,
                progress_callback=progress_callback,
                performance_callback=performance_callback,
            )
            return

        self._optimise_batch_size(total)
        index = 0
        completed = 0
        errors: list[Exception] = []
        lock = Lock()

        def submit_batch(
            executor: ThreadPoolExecutor,
        ) -> Future[tuple[int, float]] | None:
            nonlocal index
            if index >= total:
                return None
            batch_size = min(self.current_batch_size, total - index)
            batch_df = nodes_df.iloc[index : index + batch_size]
            index += batch_size

            def run_batch(df: pd.DataFrame) -> tuple[int, float]:
                with self._semaphore:
                    self.node_loader.batch_size = len(df)
                    start = time.perf_counter()
                    self.node_loader.load_nodes(df, merge_query)
                    return len(df), time.perf_counter() - start

            return executor.submit(run_batch, batch_df)

        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            futures = {f for _ in range(self.workers) if (f := submit_batch(executor))}
            while futures:
                done, futures = wait(futures, return_when=FIRST_COMPLETED)
                for future in done:
                    try:
                        processed, duration = future.result()
                    except Exception as exc:  # pragma: no cover - error aggregation
                        errors.append(exc)
                    else:
                        if performance_callback:
                            performance_callback(processed, duration)
                        with lock:
                            completed += processed
                            if progress_callback:
                                progress_callback(completed, total)
                        self._optimise_batch_size(processed, duration)
                        self._warn_if_memory_high()
                    if f := submit_batch(executor):
                        futures.add(f)

        if errors:
            raise ExceptionGroup("Batch processing errors", errors)

    def create_relationships(
        self,
        edges_df: pd.DataFrame,
        relationship_query: str,
        progress_callback: Callable[[int, int], None] | None = None,
        performance_callback: Callable[[int, float], None] | None = None,
    ) -> None:
        """Create relationships using ``relationship_query``.

        Args:
            edges_df: DataFrame of relationship data.
            relationship_query: Cypher query for relationships.
            progress_callback: Optional callback accepting
                ``(loaded, total)`` counts.
            performance_callback: Optional callback
                receiving ``(rows, seconds)`` for each batch.

        """
        total = len(edges_df)
        if total == 0:
            return

        if edges_df.memory_usage(deep=True).sum() > self.memory_limit:
            logger.warning(
                "Edges DataFrame exceeds %.2fGB limit; spilling to disk",
                self.memory_limit / 1024**3,
            )
            self._spill_to_disk(
                df=edges_df,
                query=relationship_query,
                loader=self.edge_loader.load_edges,
                loader_obj=self.edge_loader,
                progress_callback=progress_callback,
                performance_callback=performance_callback,
            )
            return

        self._optimise_batch_size(total)
        index = 0
        completed = 0
        errors: list[Exception] = []
        lock = Lock()

        def submit_batch(
            executor: ThreadPoolExecutor,
        ) -> Future[tuple[int, float]] | None:
            nonlocal index
            if index >= total:
                return None
            batch_size = min(self.current_batch_size, total - index)
            batch_df = edges_df.iloc[index : index + batch_size]
            index += batch_size

            def run_batch(df: pd.DataFrame) -> tuple[int, float]:
                with self._semaphore:
                    self.edge_loader.batch_size = len(df)
                    start = time.perf_counter()
                    self.edge_loader.load_edges(df, relationship_query)
                    return len(df), time.perf_counter() - start

            return executor.submit(run_batch, batch_df)

        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            futures = {f for _ in range(self.workers) if (f := submit_batch(executor))}
            while futures:
                done, futures = wait(futures, return_when=FIRST_COMPLETED)
                for future in done:
                    try:
                        processed, duration = future.result()
                    except Exception as exc:  # pragma: no cover - error aggregation
                        errors.append(exc)
                    else:
                        if performance_callback:
                            performance_callback(processed, duration)
                        with lock:
                            completed += processed
                            if progress_callback:
                                progress_callback(completed, total)
                        self._optimise_batch_size(processed, duration)
                        self._warn_if_memory_high()
                    if f := submit_batch(executor):
                        futures.add(f)

        if errors:
            raise ExceptionGroup("Batch processing errors", errors)

    def _warn_if_memory_high(self) -> None:
        """Log a warning if process memory exceeds the limit."""
        used = psutil.Process().memory_info().rss
        if used > self.memory_limit:
            logger.warning(
                "Memory usage %.2fGB exceeds %.2fGB limit",
                used / 1024**3,
                self.memory_limit / 1024**3,
            )

    def _spill_to_disk(
        self,
        df: pd.DataFrame,
        query: str,
        loader: Callable[[pd.DataFrame, str], None],
        loader_obj: NodeLoader | EdgeLoader,
        progress_callback: Callable[[int, int], None] | None,
        performance_callback: Callable[[int, float], None] | None,
    ) -> None:
        """Write ``df`` to disk and load it in chunks."""
        total = len(df)
        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tmp:
            df.to_csv(tmp.name, index=False)
            path = tmp.name
        del df
        gc.collect()
        completed = 0
        try:
            for chunk in pd.read_csv(path, chunksize=self.current_batch_size):
                loader_obj.batch_size = len(chunk)
                start = time.perf_counter()
                loader(chunk, query)
                duration = time.perf_counter() - start
                completed += len(chunk)
                if performance_callback:
                    performance_callback(len(chunk), duration)
                if progress_callback:
                    progress_callback(completed, total)
                self._warn_if_memory_high()
        finally:
            os.remove(path)

    def _optimise_batch_size(
        self,
        processed: int,
        duration: float | None = None,
    ) -> int:
        """Tune batch size based on performance."""
        if duration is None:
            self.current_batch_size = min(self.default_batch_size, processed)
            return self.current_batch_size
        if duration <= 0 or processed <= 0:
            return self.current_batch_size
        rate = processed / duration
        if rate >= self.target_rate and self.current_batch_size < self.max_batch_size:
            self.current_batch_size = min(
                self.current_batch_size * 2,
                self.max_batch_size,
            )
        elif rate < self.target_rate and self.current_batch_size > self.min_batch_size:
            self.current_batch_size = max(
                self.current_batch_size // 2,
                self.min_batch_size,
            )
        return self.current_batch_size

    def load_from_dataframe(
        self,
        nodes_df: pd.DataFrame | None = None,
        edges_df: pd.DataFrame | None = None,
        node_query: str | None = None,
        edge_query: str | None = None,
    ) -> None:
        """Load nodes and edges from DataFrames."""
        if nodes_df is not None and node_query:
            self.node_loader.batch_size = self._optimise_batch_size(len(nodes_df))
            self.node_loader.load_nodes(
                nodes_df,
                node_query,
            )

        if edges_df is not None and edge_query:
            self.edge_loader.batch_size = self._optimise_batch_size(len(edges_df))
            self.edge_loader.load_edges(
                edges_df,
                edge_query,
            )

    def load_data(self, nodes_info=None, edges_info=None) -> None:
        """Backward compatible wrapper for CSV loading."""
        if nodes_info and "nodes_info" in nodes_info:
            for node in nodes_info["nodes_info"]:
                node_df = pd.read_csv(node["csv_file"])
                node_df.fillna(value="", inplace=True)
                self.load_from_dataframe(
                    nodes_df=node_df,
                    node_query=node["query"],
                )

        if edges_info and "edges_info" in edges_info:
            for edge in edges_info["edges_info"]:
                edge_df = pd.read_csv(edge["csv_file"])
                edge_df.fillna(value="", inplace=True)
                self.load_from_dataframe(
                    edges_df=edge_df,
                    edge_query=edge["query"],
                )

    def load_from_csv(self, object_info) -> None:
        """Load nodes and edges from CSV ``object_info``."""
        nodes_info = object_info.get("nodes_info")
        edges_info = object_info.get("edges_info")
        self.load_data(
            nodes_info=nodes_info,
            edges_info=edges_info,
        )
        self.neo4j_database.close()

    def orchestrate_neo4j_data_load_from_csv(self, object_info) -> None:
        """Backward compatible wrapper for :meth:`load_from_csv`."""
        self.load_from_csv(object_info)


Neo4jDataLoadOrchestrators = Neo4jDataLoaders
