"""Circuit breaker implementation for Neo4j."""

from __future__ import annotations

import time
from collections.abc import Callable
from dataclasses import dataclass
from enum import Enum


class CircuitBreakerState(Enum):
    """Possible circuit breaker states."""

    CLOSED = "closed"
    OPEN = "open"
    HALF_OPEN = "half_open"


@dataclass(slots=True)
class CircuitBreakerMetrics:
    """Track metrics for the circuit breaker."""

    consecutive_failures: int = 0
    consecutive_successes: int = 0
    total_failures: int = 0
    total_successes: int = 0
    open_events: int = 0
    half_open_events: int = 0
    last_failure_time: float | None = None
    last_success_time: float | None = None
    last_state_change: float | None = None

    def to_dict(self) -> dict[str, float | int | None]:
        """Return a serialisable view of the metrics."""
        return {
            "consecutive_failures": self.consecutive_failures,
            "consecutive_successes": self.consecutive_successes,
            "total_failures": self.total_failures,
            "total_successes": self.total_successes,
            "open_events": self.open_events,
            "half_open_events": self.half_open_events,
            "last_failure_time": self.last_failure_time,
            "last_success_time": self.last_success_time,
            "last_state_change": self.last_state_change,
        }


class CircuitBreaker:
    """Simple circuit breaker with metrics."""

    def __init__(
        self,
        *,
        failure_threshold: int = 5,
        recovery_timeout: float = 30.0,
        half_open_max_calls: int = 1,
        success_threshold: int = 1,
        clock: Callable[[], float] | None = None,
    ) -> None:
        if failure_threshold < 1:
            msg = "failure_threshold must be positive"
            raise ValueError(msg)
        if recovery_timeout <= 0:
            msg = "recovery_timeout must be positive"
            raise ValueError(msg)
        if half_open_max_calls < 1:
            msg = "half_open_max_calls must be positive"
            raise ValueError(msg)
        if success_threshold < 1:
            msg = "success_threshold must be positive"
            raise ValueError(msg)
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.half_open_max_calls = half_open_max_calls
        self.success_threshold = success_threshold
        self._clock = clock or time.monotonic
        self._state = CircuitBreakerState.CLOSED
        self._open_until: float | None = None
        self._half_open_calls = 0
        self._metrics = CircuitBreakerMetrics()

    @property
    def state(self) -> CircuitBreakerState:
        """Return the current state."""
        return self._state

    @property
    def metrics(self) -> dict[str, float | int | None]:
        """Return a copy of the metrics."""
        return self._metrics.to_dict().copy()

    def allow(self, *, now: float | None = None) -> bool:
        """Return whether an operation is permitted."""
        current = self._now(now)
        if self._state is CircuitBreakerState.OPEN:
            assert self._open_until is not None
            if current >= self._open_until:
                self._to_half_open(current)
            else:
                return False
        if self._state is CircuitBreakerState.HALF_OPEN:
            if self._half_open_calls >= self.half_open_max_calls:
                return False
            self._half_open_calls += 1
        return True

    def record_success(self, *, now: float | None = None) -> None:
        """Record a successful operation."""
        current = self._now(now)
        self._metrics.total_successes += 1
        self._metrics.last_success_time = current
        self._metrics.consecutive_successes += 1
        self._metrics.consecutive_failures = 0
        if self._state is CircuitBreakerState.HALF_OPEN:
            if self._metrics.consecutive_successes >= self.success_threshold:
                self._to_closed(current)
        elif self._state is CircuitBreakerState.OPEN:
            self._to_half_open(current)

    def record_failure(self, *, now: float | None = None) -> None:
        """Record a failed operation and update state."""
        current = self._now(now)
        self._metrics.total_failures += 1
        self._metrics.last_failure_time = current
        self._metrics.consecutive_failures += 1
        self._metrics.consecutive_successes = 0
        if self._state is CircuitBreakerState.HALF_OPEN:
            self._to_open(current)
            return
        if self._metrics.consecutive_failures >= self.failure_threshold:
            self._to_open(current)

    def reset(self) -> None:
        """Reset the breaker to a closed state."""
        self._state = CircuitBreakerState.CLOSED
        self._open_until = None
        self._half_open_calls = 0
        self._metrics = CircuitBreakerMetrics()

    def _now(self, override: float | None) -> float:
        return override if override is not None else self._clock()

    def _to_open(self, current: float) -> None:
        self._state = CircuitBreakerState.OPEN
        self._open_until = current + self.recovery_timeout
        self._half_open_calls = 0
        self._metrics.open_events += 1
        self._metrics.consecutive_failures = 0
        self._metrics.consecutive_successes = 0
        self._metrics.last_state_change = current

    def _to_half_open(self, current: float) -> None:
        self._state = CircuitBreakerState.HALF_OPEN
        self._open_until = None
        self._half_open_calls = 0
        self._metrics.half_open_events += 1
        self._metrics.consecutive_successes = 0
        self._metrics.consecutive_failures = 0
        self._metrics.last_state_change = current

    def _to_closed(self, current: float) -> None:
        self._state = CircuitBreakerState.CLOSED
        self._open_until = None
        self._half_open_calls = 0
        self._metrics.consecutive_failures = 0
        self._metrics.last_state_change = current
