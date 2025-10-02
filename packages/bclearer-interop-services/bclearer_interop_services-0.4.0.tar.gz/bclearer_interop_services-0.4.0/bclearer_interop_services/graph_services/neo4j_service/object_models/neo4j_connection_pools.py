from __future__ import annotations

import time
from collections.abc import Callable
from types import TracebackType
from typing import Self, TypeVar

from neo4j import Driver, GraphDatabase

from bclearer_interop_services.graph_services.neo4j_service.utils.circuit_breaker import (
    CircuitBreaker,
)

T = TypeVar("T")


class Neo4jConnectionPools:
    """Manage Neo4j driver connection pooling."""

    def __init__(
        self,
        uri: str,
        auth: tuple[str, str],
        max_connection_pool_size: int = 10,
        connection_timeout: float | None = None,
        max_retries: int = 3,
        retry_delay: float = 0.1,
        circuit_breaker_threshold: int = 5,
        circuit_breaker_timeout: float = 30.0,
        circuit_breaker_half_open_max_calls: int = 1,
        circuit_breaker_success_threshold: int = 1,
    ) -> None:
        self.uri = uri
        self.auth = auth
        self.max_connection_pool_size = max_connection_pool_size
        self.connection_timeout = connection_timeout
        self._driver: Driver | None = None
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.circuit_breaker_threshold = circuit_breaker_threshold
        self.circuit_breaker_timeout = circuit_breaker_timeout
        self._circuit_breaker = CircuitBreaker(
            failure_threshold=circuit_breaker_threshold,
            recovery_timeout=circuit_breaker_timeout,
            half_open_max_calls=circuit_breaker_half_open_max_calls,
            success_threshold=circuit_breaker_success_threshold,
        )

    def get_driver(self) -> Driver:
        """Return a pooled driver, creating it if needed."""
        if self._driver is None:
            self._driver = GraphDatabase.driver(
                self.uri,
                auth=self.auth,
                max_connection_pool_size=self.max_connection_pool_size,
                connection_timeout=self.connection_timeout,
            )
        return self._driver

    def execute_with_retry(
        self,
        operation: Callable[[Driver], T],
    ) -> T:
        """Execute an operation with retry logic."""
        if not self._circuit_breaker.allow():
            raise RuntimeError("circuit breaker open")
        delay = self.retry_delay
        for attempt in range(1, self.max_retries + 1):
            try:
                result = operation(self.get_driver())
                self._circuit_breaker.record_success()
                return result
            except Exception as exc:
                self._circuit_breaker.record_failure()
                if attempt == self.max_retries:
                    diagnostics = {
                        "healthy": self.health_check(),
                        "circuit": self._circuit_breaker.metrics,
                    }
                    msg = (
                        "operation failed after "
                        f"{self.max_retries} retries: "
                        f"{exc}. diagnostics: {diagnostics}"
                    )
                    raise RuntimeError(msg) from exc
                time.sleep(delay)
                delay *= 2
        raise RuntimeError("retry loop exited")

    def health_check(self) -> bool:
        """Run a simple query to verify connectivity."""
        try:
            with self.get_driver().session() as session:
                session.run("RETURN 1")
            return True
        except Exception:
            return False

    def close(self) -> None:
        """Close the underlying driver."""
        if self._driver is not None:
            self._driver.close()
            self._driver = None

    @property
    def circuit_breaker_state(self) -> str:
        """Return the current circuit breaker state."""
        return self._circuit_breaker.state.value

    @property
    def circuit_breaker_metrics(self) -> dict[str, float | int | None]:
        """Expose circuit breaker metrics."""
        return self._circuit_breaker.metrics.copy()

    def reset_circuit_breaker(self) -> None:
        """Reset the circuit breaker to closed."""
        self._circuit_breaker.reset()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.close()
