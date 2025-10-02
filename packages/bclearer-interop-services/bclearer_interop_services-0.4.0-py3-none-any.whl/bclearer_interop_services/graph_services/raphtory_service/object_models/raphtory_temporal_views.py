"""Raphtory temporal view utilities."""

from __future__ import annotations

from raphtory import Graph


class RaphtoryTemporalViews:
    """Create temporal views of Raphtory graphs."""

    def __init__(self, graph: Graph) -> None:
        self.graph = graph

    def _validate_timestamp(self, timestamp: int) -> None:
        """Validate timestamp is within graph time range."""
        earliest = self.graph.earliest_time()
        latest = self.graph.latest_time()
        if timestamp < earliest or timestamp > latest:
            raise ValueError(
                f"Timestamp {timestamp} is outside graph range {earliest}-{latest}",
            )

    def _validate_range(self, start: int, end: int) -> None:
        """Validate start/end define a proper time range."""
        if start > end:
            raise ValueError("Start time must not exceed end time")
        self._validate_timestamp(start)
        self._validate_timestamp(end)

    def create_window_view(
        self,
        start: int,
        end: int,
    ) -> Graph:
        """Return a view for a fixed window."""
        self._validate_range(start, end)
        return self.graph.window(start, end)

    def create_rolling_view(
        self,
        window_size: int,
        step: int,
    ) -> Graph:
        """Return a rolling window view."""
        return self.graph.rolling(window_size, step)

    def create_expanding_view(
        self,
        step: int,
    ) -> Graph:
        """Return an expanding window view."""
        return self.graph.expanding(step)

    def time_travel(
        self,
        timestamp: int,
    ) -> Graph:
        """Return view at a point in time."""
        self._validate_timestamp(timestamp)
        return self.graph.at(timestamp)
