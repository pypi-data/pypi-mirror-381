"""Basic Raphtory temporal analysis example."""

from __future__ import annotations

from pathlib import Path

from bclearer_interop_services.graph_services.raphtory_service.raphtory_service_facade import (
    RaphtoryServiceFacade,
)

CONFIG_PATH = (
    Path(__file__).resolve().parents[1]
    / "configurations"
    / "example_configuration.json"
)


def main() -> None:
    """Create a graph and query a time window."""
    with RaphtoryServiceFacade(str(CONFIG_PATH)) as service:
        service.create_graph("demo")
        graph = service.get_graph("demo")
        graph.add_node(0, "alice", {})
        graph.add_node(1, "bob", {})
        graph.add_edge(2, "alice", "bob", {})
        views = service.get_temporal_views("demo")
        window = views.create_window_view(0, 2)
        print(list(window.nodes()))
        print(list(window.edges()))


if __name__ == "__main__":
    main()
