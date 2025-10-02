# Neo4j Service

Integration with [Neo4j](https://neo4j.com), providing synchronous and asynchronous graph operations for the bclearer PDK.

## Installation

```bash
pip install neo4j pandas networkx
```

> **Tip:** Install `pandas` and `networkx` to enable bulk loading utilities and export helpers. Optional features such as
> advanced credential storage may require additional dependencies documented in the related modules.

## Configuration

1. Copy the [example configuration](./configurations/example_configuration.json) to a secure location.
2. Update the `uri`, `database_name`, `user_name`, and `password` fields for each environment profile.
3. Select a profile when creating the service facade:
   ```python
   Neo4jServiceFacade("config.json", profile="production")
   ```
4. Enable optional features:
   - Set `features.encryption` to `true` for TLS connections (`neo4j+s://`).
   - Set `features.aura` to `true` when connecting to Neo4j Aura; the configuration helpers auto-adjust defaults.
5. Override sensitive values with environment variables or secret managers using the utilities in
   [security/credential_providers.py](./security/credential_providers.py).

## Getting started

```python
from bclearer_interop_services.graph_services.neo4j_service.neo4j_service_facade import (
    Neo4jServiceFacade,
)

with Neo4jServiceFacade("config.json") as service:
    session = service.create_session()
    session.execute_write(
        "CREATE (:Person {name: $name})",
        name="Alice",
    )
    records = session.execute_read(
        "MATCH (p:Person) RETURN p.name AS name"
    )
    print([record["name"] for record in records])
```

- The context manager closes connections automatically.
- Use `service.create_async_session()` for async/await workflows.
- Call `service.create_data_loader()` to bulk load nodes and relationships from pandas DataFrames.

## Usage examples

### Synchronous session operations

```python
from bclearer_interop_services.graph_services.neo4j_service.neo4j_service_facade import (
    Neo4jServiceFacade,
)

with Neo4jServiceFacade("config.json") as service:
    session = service.create_session()
    session.execute_transaction(
        lambda tx: tx.run(
            "CREATE (:Person {person_id: $id, name: $name})",
            id="123",
            name="Dana",
        ),
    )
    names = session.execute_read(
        """
        MATCH (p:Person)
        RETURN p.person_id AS id, p.name AS name
        ORDER BY name
        """
    )
    print([record["name"] for record in names])
```

- `create_session()` returns a synchronous wrapper with helper methods for reads, writes, and explicit transactions.
- `execute_transaction()` is useful for multi-step transactional logic using the Neo4j driver `Transaction` API.

### Async session operations

```python
import asyncio

from bclearer_interop_services.graph_services.neo4j_service.neo4j_service_facade import (
    Neo4jServiceFacade,
)


async def main() -> None:
    with Neo4jServiceFacade("config.json") as service:
        async with service.create_async_session() as session:
            await session.execute_write(
                "CREATE (:Event {name: $name})",
                {"name": "Conference"},
            )
            results = await session.execute_concurrent(
                [
                    ("MATCH (e:Event) RETURN e.name AS name", None, None),
                    (
                        "MATCH (e:Event) RETURN count(e) AS total",
                        None,
                        None,
                    ),
                ],
            )
            print(results)


asyncio.run(main())
```

- `create_async_session()` exposes async `execute_read`, `execute_write`, and `execute_concurrent` helpers backed by the connection pool.
- Limit concurrency by passing `limit` to `execute_concurrent()` when coordinating large batches of queries.

### Bulk loading from pandas DataFrames

```python
import pandas as pd

from bclearer_interop_services.graph_services.neo4j_service.neo4j_service_facade import (
    Neo4jServiceFacade,
)

nodes = pd.DataFrame(
    [
        {"person_id": "123", "name": "Dana"},
        {"person_id": "456", "name": "Elliot"},
    ]
)

relationships = pd.DataFrame(
    [
        {"source_id": "123", "target_id": "456", "kind": "KNOWS"},
    ]
)

node_query = """
UNWIND $batch AS row
MERGE (p:Person {person_id: row.person_id})
SET p.name = row.name
"""

relationship_query = """
UNWIND $batch AS row
MATCH (source:Person {person_id: row.source_id})
MATCH (target:Person {person_id: row.target_id})
MERGE (source)-[:KNOWS {kind: row.kind}]->(target)
"""

with Neo4jServiceFacade("config.json") as service:
    loader = service.create_data_loader(batch_size=5000)
    loader.upsert_nodes(nodes, node_query)
    loader.create_relationships(relationships, relationship_query)
```

- Loader helpers accept pandas DataFrames and execute parameterised Cypher using efficient batching and retry logic.
- Monitor progress by providing `progress_callback` or `performance_callback` keyword arguments to the loader methods.

### Exporting graph data

```python
from bclearer_interop_services.graph_services.neo4j_service.neo4j_service_facade import (
    Neo4jServiceFacade,
)

with Neo4jServiceFacade("config.json") as service:
    exporter = service.create_data_exporter()
    table = exporter.to_dataframe(
        "MATCH (p:Person) RETURN p.person_id AS id, p.name AS name",
    )
    graph = exporter.to_networkx(node_label="Person")
    exporter.to_graphml("people.graphml")
    tables = exporter.to_table_dictionary()

print(table.head())
print(graph.number_of_nodes(), graph.number_of_edges())
print(tables.keys())
```

- Use `to_dataframe()` for ad-hoc analytics with pandas.
- `to_networkx()` and `to_graphml()` support graph analytics and exchange formats.
- `to_table_dictionary()` returns a B-Dictionary structure ready for downstream orchestration services.

## Additional resources

- [Neo4j service facade](./neo4j_service_facade.py) – entry point exposing sessions, loaders, exporters, and algorithms.
- [Configuration helpers](./configurations/neo4j_configurations.py) – profile loading and validation utilities.
- [Security providers](./security/credential_providers.py) – integrations for environment variables and external secret stores.

## License

This project is licensed under the MIT License. See the [LICENSE](../../../../../LICENSE) file for details.
