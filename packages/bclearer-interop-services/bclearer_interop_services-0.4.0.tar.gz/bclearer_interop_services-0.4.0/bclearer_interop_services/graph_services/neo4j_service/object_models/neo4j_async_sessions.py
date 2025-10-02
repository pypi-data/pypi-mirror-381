from __future__ import annotations

import asyncio
from types import TracebackType
from typing import Any, Self

from neo4j import READ_ACCESS, WRITE_ACCESS

from .neo4j_connection_pools import Neo4jConnectionPools


class Neo4jAsyncSessions:
    """Execute Cypher queries asynchronously."""

    def __init__(
        self,
        pool: Neo4jConnectionPools,
        database_name: str,
        access_mode: str = WRITE_ACCESS,
    ) -> None:
        self.pool = pool
        self.database_name = database_name
        self.access_mode = access_mode

    async def _run(
        self,
        query: str,
        parameters: dict[str, Any],
        access_mode: str,
    ) -> list[Any]:
        if not isinstance(parameters, dict):
            msg = "parameters must be a dict"
            raise TypeError(msg)
        driver = self.pool.get_driver()
        async with driver.session(
            database=self.database_name,
            default_access_mode=access_mode,
        ) as session:
            result = await session.run(query, parameters)
            return await result.to_list()

    async def execute_read(
        self,
        query: str,
        parameters: dict[str, Any] | None = None,
    ) -> list[Any]:
        """Run a read query and return records."""
        params = parameters or {}
        return await self._run(query, params, READ_ACCESS)

    async def execute_write(
        self,
        query: str,
        parameters: dict[str, Any] | None = None,
    ) -> list[Any]:
        """Run a write query and return records."""
        params = parameters or {}
        return await self._run(query, params, WRITE_ACCESS)

    async def execute_concurrent(
        self,
        queries: list[tuple[str, dict[str, Any] | None, str | None]],
        limit: int | None = None,
    ) -> list[list[Any]]:
        """Run multiple queries concurrently.

        Args:
            queries: Tuples of query, parameters, and optional access mode.
            limit: Maximum concurrent queries. Unlimited if ``None``.

        Returns:
            List of results corresponding to each query.

        Raises:
            ExceptionGroup: If any query fails.

        """
        semaphore = asyncio.Semaphore(limit or len(queries))
        errors: list[BaseException] = []

        async def run_once(
            query: str,
            params: dict[str, Any] | None,
            mode: str | None,
        ) -> list[Any] | None:
            async with semaphore:
                try:
                    return await self._run(
                        query, params or {}, mode or self.access_mode
                    )
                except BaseException as exc:  # pragma: no cover - error path
                    errors.append(exc)
                    return None

        tasks = [run_once(q, p, m) for q, p, m in queries]
        results = await asyncio.gather(*tasks)
        if errors:
            raise ExceptionGroup("Concurrent query errors", errors)
        return results

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.pool.close()
