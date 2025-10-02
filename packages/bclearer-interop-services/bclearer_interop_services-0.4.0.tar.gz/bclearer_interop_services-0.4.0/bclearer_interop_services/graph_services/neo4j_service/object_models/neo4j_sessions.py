from __future__ import annotations

from collections.abc import Callable
from time import perf_counter
from typing import Any, TypeVar

from neo4j import READ_ACCESS, WRITE_ACCESS, Transaction

from .neo4j_connections import Neo4jConnections

T = TypeVar("T")


class Neo4jSessions:
    """Execute Cypher queries with transaction control."""

    def __init__(
        self,
        connection: Neo4jConnections,
        access_mode: str = WRITE_ACCESS,
    ) -> None:
        self.connection = connection
        self.database_name = self.connection.database_name
        self.access_mode = access_mode
        self._cache: dict[
            tuple[str, frozenset[tuple[str, Any]]],
            list[Any],
        ] = {}
        self.last_profile: list[dict[str, float]] = []

    def _run(
        self,
        query: str,
        parameters: dict[str, Any],
        access_mode: str,
    ) -> list[Any]:
        if not isinstance(parameters, dict):
            msg = "parameters must be a dict"
            raise TypeError(msg)
        driver = self.connection.get_driver()
        with driver.session(
            database=self.database_name,
            default_access_mode=access_mode,
        ) as session:
            result = session.run(query, parameters)
            return list(result)

    def execute_read(
        self,
        query: str,
        parameters: dict[str, Any] | None = None,
    ) -> list[Any]:
        """Run a read query and return records."""
        params = parameters or {}
        return self._run(query, params, READ_ACCESS)

    def execute_write(
        self,
        query: str,
        parameters: dict[str, Any] | None = None,
    ) -> list[Any]:
        """Run a write query and return records."""
        params = parameters or {}
        return self._run(query, params, WRITE_ACCESS)

    def execute_transaction(
        self,
        func: Callable[[Transaction], T],
        *,
        access_mode: str = WRITE_ACCESS,
    ) -> T:
        """Execute a callable within an explicit transaction."""
        if access_mode not in {READ_ACCESS, WRITE_ACCESS}:
            msg = "invalid access_mode"
            raise ValueError(msg)
        if not callable(func):
            msg = "func must be callable"
            raise TypeError(msg)
        driver = self.connection.get_driver()
        with driver.session(
            database=self.database_name,
            default_access_mode=access_mode,
        ) as session:
            if access_mode == WRITE_ACCESS:
                return session.execute_write(func)
            return session.execute_read(func)

    def execute_batch(
        self,
        queries: list[tuple[str, dict[str, Any] | None]],
        *,
        access_mode: str | None = None,
        use_cache: bool = False,
    ) -> list[list[Any]]:
        """Execute multiple queries sequentially.

        Parameters
        ----------
        queries:
            Tuples of Cypher query and parameters.
        access_mode:
            Override default access mode.
        use_cache:
            Reuse results for identical queries.

        """
        mode = access_mode or self.access_mode
        if mode not in {READ_ACCESS, WRITE_ACCESS}:
            msg = "invalid access_mode"
            raise ValueError(msg)
        driver = self.connection.get_driver()
        results: list[list[Any]] = []
        profile: list[dict[str, float]] = []
        with driver.session(
            database=self.database_name,
            default_access_mode=mode,
        ) as session:
            for query, params in queries:
                parameters = params or {}
                if not isinstance(parameters, dict):
                    msg = "parameters must be a dict"
                    raise TypeError(msg)
                key = (query, frozenset(parameters.items()))
                if use_cache and key in self._cache:
                    result = self._cache[key]
                else:
                    start = perf_counter()
                    result = list(session.run(query, parameters))
                    duration = perf_counter() - start
                    profile.append(
                        {"query": query, "time": duration},
                    )
                    if use_cache:
                        self._cache[key] = result
                results.append(result)
        self.last_profile = profile
        return results

    def execute_cypher_query(self, query: str) -> list[Any]:
        """Backward compatible query execution."""
        return self._run(query, {}, self.access_mode)

    def execute_cypher_query_with_parameters(
        self,
        query: str,
        params: dict[str, Any] | None = None,
    ) -> list[Any]:
        """Backward compatible query execution with parameters."""
        parameters = params or {}
        return self._run(query, parameters, self.access_mode)
