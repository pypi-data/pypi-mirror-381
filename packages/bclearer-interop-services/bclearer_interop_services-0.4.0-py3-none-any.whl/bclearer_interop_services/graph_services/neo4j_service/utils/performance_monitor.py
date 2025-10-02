from __future__ import annotations

import tracemalloc
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from dataclasses import dataclass, field
from time import monotonic
from typing import Any


def _default_memory_sampler() -> int:
    """Return the current traced memory usage in bytes."""
    if not tracemalloc.is_tracing():
        tracemalloc.start()
    current, _ = tracemalloc.get_traced_memory()
    return current


@dataclass(slots=True)
class PerformanceSample:
    """Single performance measurement."""

    name: str
    started_at: float
    ended_at: float
    duration: float
    memory_before: int
    memory_after: int
    memory_delta: int
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Return a serialisable representation of the sample."""
        return {
            "name": self.name,
            "started_at": self.started_at,
            "ended_at": self.ended_at,
            "duration": self.duration,
            "memory_before": self.memory_before,
            "memory_after": self.memory_after,
            "memory_delta": self.memory_delta,
            "metadata": self.metadata.copy(),
        }


@dataclass(slots=True)
class PerformanceSummary:
    """Aggregated metrics for a named operation."""

    name: str
    count: int = 0
    total_duration: float = 0.0
    min_duration: float | None = None
    max_duration: float | None = None
    total_memory_delta: int = 0
    min_memory_delta: int | None = None
    max_memory_delta: int | None = None
    total_units: float = 0.0

    def add_sample(self, sample: PerformanceSample) -> None:
        """Update summary statistics using ``sample``."""
        self.count += 1
        self.total_duration += sample.duration
        self.min_duration = (
            sample.duration
            if self.min_duration is None
            else min(self.min_duration, sample.duration)
        )
        self.max_duration = (
            sample.duration
            if self.max_duration is None
            else max(self.max_duration, sample.duration)
        )
        self.total_memory_delta += sample.memory_delta
        self.min_memory_delta = (
            sample.memory_delta
            if self.min_memory_delta is None
            else min(self.min_memory_delta, sample.memory_delta)
        )
        self.max_memory_delta = (
            sample.memory_delta
            if self.max_memory_delta is None
            else max(self.max_memory_delta, sample.memory_delta)
        )
        units = self._extract_units(sample.metadata)
        if units is not None:
            self.total_units += units

    def clone(self) -> PerformanceSummary:
        """Return a copy of the summary."""
        return PerformanceSummary(
            name=self.name,
            count=self.count,
            total_duration=self.total_duration,
            min_duration=self.min_duration,
            max_duration=self.max_duration,
            total_memory_delta=self.total_memory_delta,
            min_memory_delta=self.min_memory_delta,
            max_memory_delta=self.max_memory_delta,
            total_units=self.total_units,
        )

    @property
    def avg_duration(self) -> float:
        """Return the average duration."""
        return self.total_duration / self.count if self.count else 0.0

    @property
    def avg_memory_delta(self) -> float:
        """Return the average memory delta."""
        return self.total_memory_delta / self.count if self.count else 0.0

    @property
    def avg_throughput(self) -> float:
        """Return average processed units per second."""
        if not self.count or self.total_duration <= 0:
            return 0.0
        return self.total_units / self.total_duration

    def to_dict(self) -> dict[str, Any]:
        """Return summary metrics as a dictionary."""
        return {
            "name": self.name,
            "count": self.count,
            "total_duration": self.total_duration,
            "avg_duration": self.avg_duration,
            "min_duration": self.min_duration or 0.0,
            "max_duration": self.max_duration or 0.0,
            "total_memory_delta": self.total_memory_delta,
            "avg_memory_delta": self.avg_memory_delta,
            "min_memory_delta": self.min_memory_delta or 0,
            "max_memory_delta": self.max_memory_delta or 0,
            "total_units": self.total_units,
            "avg_throughput": self.avg_throughput,
        }

    def _extract_units(self, metadata: dict[str, Any]) -> float | None:
        value = metadata.get("rows")
        if value is None:
            value = metadata.get("items")
        if value is None:
            value = metadata.get("count")
        if value is None:
            return None
        if isinstance(value, (int, float)):
            return float(value)
        return None


class PerformanceMonitor:
    """Collect performance samples with timing and memory data."""

    def __init__(
        self,
        *,
        clock: Callable[[], float] | None = None,
        memory_sampler: Callable[[], int] | None = None,
    ) -> None:
        self._clock = clock or monotonic
        self._memory_sampler = memory_sampler or _default_memory_sampler
        self._samples: list[PerformanceSample] = []
        self._summaries: dict[str, PerformanceSummary] = {}

    @property
    def samples(self) -> list[PerformanceSample]:
        """Return a copy of recorded samples."""
        return list(self._samples)

    def iter_samples(
        self,
        name: str | None = None,
    ) -> Iterator[PerformanceSample]:
        """Yield samples optionally filtered by name."""
        for sample in self._samples:
            if name is None or sample.name == name:
                yield sample

    def get_summary(self, name: str) -> PerformanceSummary | None:
        """Return the summary for ``name`` if present."""
        summary = self._summaries.get(name)
        if summary is None:
            return None
        return summary.clone()

    def get_metrics(self) -> dict[str, dict[str, Any]]:
        """Return all summary metrics as dictionaries."""
        return {
            name: summary.to_dict() for name, summary in self._summaries.items()
        }

    @contextmanager
    def track(
        self,
        name: str,
        *,
        metadata: dict[str, Any] | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Context manager capturing duration and memory usage."""
        info = dict(metadata) if metadata else {}
        start = self._clock()
        mem_before = self._memory_sampler()
        try:
            yield info
        finally:
            end = self._clock()
            mem_after = self._memory_sampler()
            sample = PerformanceSample(
                name=name,
                started_at=start,
                ended_at=end,
                duration=end - start,
                memory_before=mem_before,
                memory_after=mem_after,
                memory_delta=mem_after - mem_before,
                metadata=info.copy(),
            )
            self._register_sample(sample)

    def record(
        self,
        name: str,
        *,
        duration: float,
        metadata: dict[str, Any] | None = None,
        memory_delta: int = 0,
        started_at: float | None = None,
        memory_before: int | None = None,
    ) -> PerformanceSample:
        """Record an externally measured sample."""
        if duration < 0:
            msg = "duration must be non-negative"
            raise ValueError(msg)
        metadata_copy = dict(metadata) if metadata else {}
        if started_at is None:
            end = self._clock()
            start = end - duration
        else:
            start = started_at
            end = started_at + duration
        before = memory_before if memory_before is not None else 0
        after = before + memory_delta
        sample = PerformanceSample(
            name=name,
            started_at=start,
            ended_at=end,
            duration=duration,
            memory_before=before,
            memory_after=after,
            memory_delta=memory_delta,
            metadata=metadata_copy,
        )
        self._register_sample(sample)
        return sample

    def reset(self) -> None:
        """Clear all stored samples and summaries."""
        self._samples.clear()
        self._summaries.clear()

    def _register_sample(self, sample: PerformanceSample) -> None:
        self._samples.append(sample)
        summary = self._summaries.get(sample.name)
        if summary is None:
            summary = PerformanceSummary(name=sample.name)
            self._summaries[sample.name] = summary
        summary.add_sample(sample)


__all__ = [
    "PerformanceMonitor",
    "PerformanceSample",
    "PerformanceSummary",
]
