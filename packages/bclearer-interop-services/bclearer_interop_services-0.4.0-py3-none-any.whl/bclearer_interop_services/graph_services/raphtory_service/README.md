# Raphtory Service

Integration with [Raphtory](https://raphtory.com), an in-memory temporal graph database, for the bclearer PDK.

## Installation

```bash
pip install raphtory
```

## Requirements and Dependencies

- Python 3.12+
- raphtory
- pandas
- langchain (optional, for embeddings)
- networkx (optional, for export)

## Usage

### Create and query a graph

```python
from bclearer_interop_services.graph_services.raphtory_service.raphtory_service_facade import (
    RaphtoryServiceFacade,
)

with RaphtoryServiceFacade("config.json") as service:
    service.create_graph("demo")
    graph = service.get_graph("demo")
    graph.add_node(0, "alice", {})
    graph.add_edge(1, "alice", "bob", {})
    ranks = service.get_algorithms("demo").pagerank()
    print(ranks)
```

### Load edges from pandas

```python
import pandas as pd
from bclearer_interop_services.graph_services.raphtory_service.raphtory_service_facade import (
    RaphtoryServiceFacade,
)

edges = pd.DataFrame(
    {
        "time": [1, 2],
        "src": ["alice", "bob"],
        "dst": ["bob", "carol"],
    }
)

with RaphtoryServiceFacade("config.json") as service:
    service.create_graph("demo")
    loader = service.get_data_loader("demo")
    loader.load_from_pandas(
        edges,
        time_col="time",
        source_col="src",
        destination_col="dst",
    )
```

### Temporal queries

```python
from bclearer_interop_services.graph_services.raphtory_service.raphtory_service_facade import (
    RaphtoryServiceFacade,
)

with RaphtoryServiceFacade("config.json") as service:
    service.create_graph("demo")
    views = service.get_temporal_views("demo")
    past = views.time_travel(1)
```

## License

This project is licensed under the MIT License. See the [LICENSE](../../../../../LICENSE) file for details.

