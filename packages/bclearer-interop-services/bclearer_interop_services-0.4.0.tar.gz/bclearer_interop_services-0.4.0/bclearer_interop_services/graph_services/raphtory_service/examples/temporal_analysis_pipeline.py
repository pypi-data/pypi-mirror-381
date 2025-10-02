"""Advanced Raphtory temporal analysis pipeline example."""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from bclearer_interop_services.graph_services.raphtory_service.raphtory_service_facade import (
    RaphtoryServiceFacade,
)

CONFIG_PATH = (
    Path(__file__).resolve().parents[1]
    / "configurations"
    / "example_configuration.json"
)
GRAPH_NAME = "advanced_pipeline"

EDGE_DATA = pd.DataFrame(
    [
        {"time": 0, "source": "alice", "destination": "bob"},
        {"time": 1, "source": "bob", "destination": "carol"},
        {"time": 2, "source": "carol", "destination": "dave"},
        {"time": 3, "source": "dave", "destination": "alice"},
    ],
)


def main() -> None:
    """Run a data loading, windowing, and algorithm pipeline."""
    with RaphtoryServiceFacade(str(CONFIG_PATH)) as service:
        service.create_graph(GRAPH_NAME)
        loader = service.get_data_loader(GRAPH_NAME)
        loader.load_from_pandas(
            EDGE_DATA,
            time_col="time",
            source_col="source",
            destination_col="destination",
        )

        views = service.get_temporal_views(GRAPH_NAME)
        window = views.create_window_view(1, 3)
        print("Window nodes:", sorted(node.name for node in window.nodes()))

        algorithms = service.get_algorithms(GRAPH_NAME)
        pagerank_scores = algorithms.pagerank()
        print("PageRank:", pagerank_scores)


if __name__ == "__main__":
    main()
