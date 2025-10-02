"""Neo4j service facade."""

from __future__ import annotations

from collections.abc import Callable, Iterator, Mapping
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Self, TypeVar

import networkx as nx
import pandas as pd
from neo4j import READ_ACCESS, WRITE_ACCESS, Transaction

from .configurations.neo4j_configurations import (
    Neo4jConfigurations,
)
from .object_models.neo4j_algorithms import (
    Neo4jAlgorithms,
)
from .object_models.neo4j_async_sessions import (
    Neo4jAsyncSessions,
)
from .object_models.neo4j_connection_pools import (
    Neo4jConnectionPools,
)
from .object_models.neo4j_databases import (
    Neo4jDatabases,
)
from .object_models.neo4j_query_builders import (
    Neo4jQueryBuilders,
    QueryPlanCache,
)
from .object_models.neo4j_schemas import (
    Neo4jSchemas,
)
from .object_models.neo4j_sessions import (
    Neo4jSessions,
)
from .orchestrators.neo4j_data_exporters import (
    Neo4jDataExporters,
)
from .orchestrators.neo4j_data_loaders import (
    Neo4jDataLoaders,
)

T = TypeVar("T")


class Neo4jServiceFacade:
    """Main entry point for Neo4j service components."""

    def __init__(
        self,
        configuration_file: str | None = None,
        *,
        profile: str = "default",
        configuration: Neo4jConfigurations | None = None,
        connection_pool: Neo4jConnectionPools | None = None,
        database: Neo4jDatabases | None = None,
        session_factory: type[Neo4jSessions] = Neo4jSessions,
        async_session_factory: type[Neo4jAsyncSessions] = Neo4jAsyncSessions,
        algorithms_factory: type[Neo4jAlgorithms] = Neo4jAlgorithms,
        schema_factory: type[Neo4jSchemas] = Neo4jSchemas,
        data_loader_factory: type[Neo4jDataLoaders] = Neo4jDataLoaders,
        data_exporter_factory: type[Neo4jDataExporters] = Neo4jDataExporters,
        query_builder_factory: type[Neo4jQueryBuilders] = Neo4jQueryBuilders,
        connection_pool_kwargs: Mapping[str, Any] | None = None,
    ) -> None:
        if configuration is None:
            if configuration_file is None:
                msg = "configuration or configuration_file must be provided"
                raise ValueError(msg)
            configuration = Neo4jConfigurations.from_file(
                configuration_file,
                profile=profile,
            )
        self.configuration = configuration

        pool_kwargs = dict(connection_pool_kwargs or {})
        if connection_pool is None:
            supported_keys = {
                "max_connection_pool_size",
                "connection_timeout",
                "max_retries",
                "retry_delay",
                "circuit_breaker_threshold",
                "circuit_breaker_timeout",
                "circuit_breaker_half_open_max_calls",
                "circuit_breaker_success_threshold",
            }
            filtered_kwargs = {
                key: pool_kwargs[key] for key in supported_keys if key in pool_kwargs
            }
            connection_pool = Neo4jConnectionPools(
                configuration.uri,
                (
                    configuration.user_name,
                    configuration.password,
                ),
                **filtered_kwargs,
            )
            self._owns_pool = True
        else:
            self._owns_pool = False
        self.connection_pool = connection_pool

        if database is None:
            database = Neo4jDatabases(
                uri=configuration.uri,
                user=configuration.user_name,
                password=configuration.password,
                database_name=configuration.database_name,
            )
            self._owns_database = True
        else:
            self._owns_database = False
        self.database = database

        self._session_factory = session_factory
        self._async_session_factory = async_session_factory
        self._algorithms_factory = algorithms_factory
        self._schema_factory = schema_factory
        self._data_loader_factory = data_loader_factory
        self._data_exporter_factory = data_exporter_factory
        self._query_builder_factory = query_builder_factory
        self._closed = False

    def create_session(
        self,
        *,
        access_mode: str = WRITE_ACCESS,
    ) -> Neo4jSessions:
        """Return a synchronous session backed by the configuration."""
        return self._session_factory(
            connection=self.database.connection,
            access_mode=access_mode,
        )

    def create_async_session(
        self,
        *,
        access_mode: str = WRITE_ACCESS,
    ) -> Neo4jAsyncSessions:
        """Return an asynchronous session backed by the connection pool."""
        return self._async_session_factory(
            self.connection_pool,
            self.configuration.database_name,
            access_mode=access_mode,
        )

    def get_algorithms(self) -> Neo4jAlgorithms:
        """Return helpers for running Graph Data Science algorithms."""
        return self._algorithms_factory(
            pool=self.connection_pool,
            database_name=self.configuration.database_name,
        )

    def get_schema_manager(
        self,
        *,
        initial_version: str | None = None,
    ) -> Neo4jSchemas:
        """Return helper for schema management."""
        return self._schema_factory(
            self.connection_pool,
            database_name=self.configuration.database_name,
            initial_version=initial_version,
        )

    def create_data_loader(
        self,
        *,
        batch_size: int = 10_000,
        target_rate: int = 100_000,
        workers: int = 4,
        memory_limit: int = 2 * 1024**3,
    ) -> Neo4jDataLoaders:
        """Return a configured data loader for bulk operations."""
        return self._data_loader_factory(
            self.database,
            batch_size=batch_size,
            target_rate=target_rate,
            workers=workers,
            memory_limit=memory_limit,
        )

    def create_data_exporter(
        self,
        *,
        session: Neo4jSessions | None = None,
        access_mode: str = READ_ACCESS,
    ) -> Neo4jDataExporters:
        """Return a data exporter using an existing or new session."""
        session_obj = session or self.create_session(
            access_mode=access_mode,
        )
        return self._data_exporter_factory(session_obj)

    def create_query_builder(
        self,
        *,
        plan_cache: QueryPlanCache | None = None,
        max_cache_size: int = 128,
    ) -> Neo4jQueryBuilders:
        """Return a query builder with optional plan caching."""
        builder_kwargs: dict[str, object] = {
            "max_cache_size": max_cache_size,
        }
        if plan_cache is not None:
            builder_kwargs["plan_cache"] = plan_cache
        return self._query_builder_factory(**builder_kwargs)

    def run_read_query(
        self,
        query: str,
        parameters: Mapping[str, object] | None = None,
    ) -> list[Any]:
        """Execute a Cypher read query using a managed session."""
        session = self.create_session(access_mode=READ_ACCESS)
        params = dict(parameters or {})
        return session.execute_read(query, params)

    def run_write_query(
        self,
        query: str,
        parameters: Mapping[str, object] | None = None,
    ) -> list[Any]:
        """Execute a Cypher write query using a managed session."""
        session = self.create_session(access_mode=WRITE_ACCESS)
        params = dict(parameters or {})
        return session.execute_write(query, params)

    def run_transaction(
        self,
        func: Callable[[Transaction], T],
        *,
        access_mode: str = WRITE_ACCESS,
    ) -> T:
        """Execute ``func`` inside an explicit transaction."""
        session = self.create_session(access_mode=access_mode)
        return session.execute_transaction(
            func,
            access_mode=access_mode,
        )

    def _create_data_loader_with_overrides(
        self,
        *,
        batch_size: int | None = None,
        target_rate: int | None = None,
        workers: int | None = None,
        memory_limit: int | None = None,
    ) -> Neo4jDataLoaders:
        loader_kwargs: dict[str, int] = {}
        if batch_size is not None:
            loader_kwargs["batch_size"] = batch_size
        if target_rate is not None:
            loader_kwargs["target_rate"] = target_rate
        if workers is not None:
            loader_kwargs["workers"] = workers
        if memory_limit is not None:
            loader_kwargs["memory_limit"] = memory_limit
        return self.create_data_loader(**loader_kwargs)

    def load_nodes(
        self,
        nodes: pd.DataFrame,
        merge_query: str,
        *,
        batch_size: int | None = None,
        target_rate: int | None = None,
        workers: int | None = None,
        memory_limit: int | None = None,
        progress_callback: Callable[[int, int], None] | None = None,
        performance_callback: Callable[[int, float], None] | None = None,
    ) -> None:
        """Load ``nodes`` into Neo4j using the bulk loader."""
        loader = self._create_data_loader_with_overrides(
            batch_size=batch_size,
            target_rate=target_rate,
            workers=workers,
            memory_limit=memory_limit,
        )
        loader.upsert_nodes(
            nodes,
            merge_query,
            progress_callback=progress_callback,
            performance_callback=performance_callback,
        )

    def load_relationships(
        self,
        relationships: pd.DataFrame,
        relationship_query: str,
        *,
        batch_size: int | None = None,
        target_rate: int | None = None,
        workers: int | None = None,
        memory_limit: int | None = None,
        progress_callback: Callable[[int, int], None] | None = None,
        performance_callback: Callable[[int, float], None] | None = None,
    ) -> None:
        """Load ``relationships`` into Neo4j using the bulk loader."""
        loader = self._create_data_loader_with_overrides(
            batch_size=batch_size,
            target_rate=target_rate,
            workers=workers,
            memory_limit=memory_limit,
        )
        loader.create_relationships(
            relationships,
            relationship_query,
            progress_callback=progress_callback,
            performance_callback=performance_callback,
        )

    def load_graph(
        self,
        *,
        nodes: pd.DataFrame | None = None,
        node_query: str | None = None,
        relationships: pd.DataFrame | None = None,
        relationship_query: str | None = None,
        batch_size: int | None = None,
        target_rate: int | None = None,
        workers: int | None = None,
        memory_limit: int | None = None,
        node_progress_callback: Callable[[int, int], None] | None = None,
        node_performance_callback: Callable[[int, float], None] | None = None,
        relationship_progress_callback: Callable[[int, int], None] | None = None,
        relationship_performance_callback: Callable[[int, float], None] | None = None,
    ) -> None:
        """Load nodes and relationships in a single operation."""
        if (nodes is None) != (node_query is None):
            msg = "nodes and node_query must be provided together"
            raise ValueError(msg)
        if (relationships is None) != (relationship_query is None):
            msg = "relationships and relationship_query must be provided together"
            raise ValueError(msg)
        if nodes is None and relationships is None:
            msg = "at least one of nodes or relationships must be provided"
            raise ValueError(msg)
        loader = self._create_data_loader_with_overrides(
            batch_size=batch_size,
            target_rate=target_rate,
            workers=workers,
            memory_limit=memory_limit,
        )
        if nodes is not None and node_query is not None:
            loader.upsert_nodes(
                nodes,
                node_query,
                progress_callback=node_progress_callback,
                performance_callback=node_performance_callback,
            )
        if relationships is not None and relationship_query is not None:
            loader.create_relationships(
                relationships,
                relationship_query,
                progress_callback=relationship_progress_callback,
                performance_callback=relationship_performance_callback,
            )

    def export_to_dataframe(
        self,
        query: str,
        parameters: Mapping[str, object] | None = None,
        *,
        session: Neo4jSessions | None = None,
    ) -> pd.DataFrame:
        """Return ``query`` results as a DataFrame."""
        exporter = self.create_data_exporter(
            session=session,
            access_mode=READ_ACCESS,
        )
        return exporter.to_dataframe(query, parameters)

    def export_to_networkx(
        self,
        *,
        node_label: str | None = None,
        relationship_type: str | None = None,
        session: Neo4jSessions | None = None,
    ) -> nx.MultiDiGraph:
        """Return the graph contents as a NetworkX ``MultiDiGraph``."""
        exporter = self.create_data_exporter(
            session=session,
            access_mode=READ_ACCESS,
        )
        return exporter.to_networkx(
            node_label=node_label,
            relationship_type=relationship_type,
        )

    def export_to_table_dictionary(
        self,
        *,
        session: Neo4jSessions | None = None,
    ) -> dict[str, Any]:
        """Return the graph contents as B-Dictionary tables."""
        exporter = self.create_data_exporter(
            session=session,
            access_mode=READ_ACCESS,
        )
        return exporter.to_table_dictionary()

    def export_to_graphml(
        self,
        file_path: str | Path,
        *,
        session: Neo4jSessions | None = None,
    ) -> None:
        """Write the graph to ``file_path`` in GraphML format."""
        exporter = self.create_data_exporter(
            session=session,
            access_mode=READ_ACCESS,
        )
        exporter.to_graphml(file_path)

    def stream_query_results(
        self,
        query: str,
        parameters: Mapping[str, object] | None = None,
        *,
        chunk_size: int = 1000,
        session: Neo4jSessions | None = None,
    ) -> Iterator[pd.DataFrame]:
        """Yield DataFrames containing chunks of ``query`` results."""
        exporter = self.create_data_exporter(
            session=session,
            access_mode=READ_ACCESS,
        )
        return exporter.stream_results(
            query,
            parameters,
            chunk_size=chunk_size,
        )

    def export_graph(
        self,
        *,
        session: Neo4jSessions | None = None,
        node_label: str | None = None,
        relationship_type: str | None = None,
        include_networkx: bool = True,
        include_table_dictionary: bool = False,
    ) -> dict[str, Any]:
        """Export graph data in one or more formats."""
        if not include_networkx and not include_table_dictionary:
            msg = "at least one export format must be requested"
            raise ValueError(msg)
        exporter = self.create_data_exporter(
            session=session,
            access_mode=READ_ACCESS,
        )
        result: dict[str, Any] = {}
        if include_networkx:
            result["networkx"] = exporter.to_networkx(
                node_label=node_label,
                relationship_type=relationship_type,
            )
        if include_table_dictionary:
            result["table_dictionary"] = exporter.to_table_dictionary()
        return result

    @contextmanager
    def transaction(
        self,
        *,
        access_mode: str = WRITE_ACCESS,
    ) -> Iterator[Transaction]:
        """Provide a transaction context manager."""
        driver = self.database.connection.get_driver()
        with driver.session(
            database=self.configuration.database_name,
            default_access_mode=access_mode,
        ) as neo4j_session:
            tx = neo4j_session.begin_transaction()
            try:
                yield tx
            except Exception:
                tx.rollback()
                raise
            else:
                tx.commit()

    def check_health(self) -> bool:
        """Return True when the service connection is healthy."""
        if hasattr(self.connection_pool, "health_check"):
            return bool(self.connection_pool.health_check())
        try:
            session = self.create_session(access_mode=READ_ACCESS)
            session.execute_read("RETURN 1")
        except Exception:  # pragma: no cover - defensive fallback
            return False
        return True

    def close(self) -> None:
        """Release managed resources."""
        if self._closed:
            return
        if self._owns_database:
            connection = getattr(self.database, "connection", None)
            if connection is not None and hasattr(connection, "close"):
                connection.close()
            if hasattr(self.database, "close"):
                self.database.close()
        if self._owns_pool and hasattr(self.connection_pool, "close"):
            self.connection_pool.close()
        self._closed = True

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type,
        exc,
        tb,
    ) -> None:
        self.close()
