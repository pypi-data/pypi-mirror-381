# Neo4j Service Migration Guide

This guide describes the breaking changes introduced by the
refactored Neo4j service and the steps required to migrate existing
code and configuration. It focuses on requirement 6.1 (compatibility
wrappers) and requirement 6.3 (configuration auto-conversion).

## Summary of breaking changes

| Legacy usage | Replacement | Notes |
| --- | --- | --- |
| `Neo4jService` from `neo4j_service.neo4j_service` | `Neo4jServiceFacade` from [`neo4j_service_facade.py`](./neo4j_service_facade.py) | Centralises access to sessions, loaders, exporters, algorithms, and schema helpers. |
| `Neo4jDataLoadOrchestrators` | `Neo4jDataLoaders` from [`orchestrators/neo4j_data_loaders.py`](./orchestrators/neo4j_data_loaders.py) | The orchestrator module now exposes loader helpers with matching method names. |
| Direct `Neo4jConnections` usage | `Neo4jConnectionPools` and `Neo4jDatabases` composed inside the facade | Connection pooling, retries, and health checks are handled by [`neo4j_connection_pools.py`](./object_models/neo4j_connection_pools.py) and [`neo4j_databases.py`](./object_models/neo4j_databases.py). |
| Flat JSON configuration with ad-hoc keys | Profile-based configuration consumed by [`neo4j_configurations.py`](./configurations/neo4j_configurations.py) | Each profile must define `uri`, `database_name`, `user_name`, and `password`. |

## Deprecated APIs and replacements

### Service entry point

The refactor removes the legacy `Neo4jService` class. Import the new
facade instead:

```python
# Old
from bclearer_interop_services.graph_services.neo4j_service.neo4j_service import Neo4jService
service = Neo4jService(config_path)

# New
from bclearer_interop_services.graph_services.neo4j_service.neo4j_service_facade import (
    Neo4jServiceFacade,
)
service = Neo4jServiceFacade(configuration_file=config_path, profile="default")
```

The facade exposes convenience methods such as `create_session()`,
`create_async_session()`, `create_data_loader()`, and
`create_data_exporter()` for synchronous, asynchronous, loading, and
export scenarios respectively.

### Data loading helpers

`Neo4jDataLoadOrchestrators` has been replaced by
`Neo4jDataLoaders`. The legacy module still re-exports the new class
for transitional compatibility, but code should update its imports to
avoid deprecation warnings.

```python
# Old
from bclearer_interop_services.graph_services.neo4j_service.orchestrators.neo4j_data_load_orchestrators import (
    Neo4jDataLoadOrchestrators,
)
loader = Neo4jDataLoadOrchestrators(connection)

# New
from bclearer_interop_services.graph_services.neo4j_service.orchestrators.neo4j_data_loaders import (
    Neo4jDataLoaders,
)
loader = service.create_data_loader()
```

### Connection management

Projects that instantiated `Neo4jConnections` directly should instead
rely on the facade-managed `Neo4jConnectionPools` and
`Neo4jDatabases` objects:

```python
with Neo4jServiceFacade(configuration_file=config_path) as service:
    pool = service.connection_pool  # Provides retry-aware driver access
    database = service.database     # Exposes connection helpers
    session = service.create_session()
    session.execute_write("RETURN 1")
```

The facade owns these resources and releases them when exiting the
context manager.

## Configuration format changes

Legacy configuration files typically used a flat structure:

```json
{
  "uri": "bolt://localhost:7687",
  "database": "neo4j",
  "username": "neo4j",
  "password": "secret"
}
```

The refactored service expects a profile-based document where each
profile defines the four required connection fields plus optional
sections for retries and features. See
[`configurations/example_configuration.json`](./configurations/example_configuration.json)
for a full template.

```json
{
  "default": {
    "uri": "neo4j://localhost:7687",
    "database_name": "neo4j",
    "user_name": "neo4j",
    "password": "secret"
  },
  "production": {
    "uri": "neo4j+s://prod.neo4j.io",
    "database_name": "neo4j",
    "user_name": "service", 
    "password": "managed"
  }
}
```

Use the compatibility helpers to convert existing files automatically:

```python
from bclearer_interop_services.graph_services.neo4j_service.compatibility.neo4j_compatibility_wrapper import (
    Neo4jCompatibilityWrapper,
)

Neo4jCompatibilityWrapper.convert_configuration_file(
    "legacy_config.json",
    profile="default",
    output_file="neo4j_profiles.json",
)
```

## Compatibility wrapper

The `Neo4jCompatibilityWrapper` class bridges the legacy constructor
and attribute access patterns to the new facade. It accepts either a
legacy mapping or a legacy configuration file and forwards calls to an
internal `Neo4jServiceFacade` instance while emitting
`DeprecationWarning` messages. Prefer instantiating the facade directly
once code has been migrated.

Enable deprecation warnings during testing to identify remaining
wrappers:

```bash
PYTHONWARNINGS=default pytest
```

## Automated migration helpers

[`compatibility/migration_helpers.py`](./compatibility/migration_helpers.py)
contains `Neo4jMigrationHelpers` utilities that automate common tasks:

- `migrate_configuration_file()` converts legacy configuration files
  into profile-based JSON.
- `update_code()` rewrites imports and class names such as
  `Neo4jService` → `Neo4jServiceFacade` and
  `Neo4jDataLoadOrchestrators` → `Neo4jDataLoaders`.
- `validate_migration()` scans migrated code or configuration for
  remaining legacy usage and reports actionable issues.

Integrate these helpers into your upgrade scripts to accelerate code
changes and catch lingering incompatibilities.

## Migration checklist

1. Convert configuration files to the profile format using the
   compatibility helpers.
2. Replace `Neo4jService` imports with `Neo4jServiceFacade` and update
   constructor arguments (`configuration_file` + `profile`).
3. Switch loader imports to `Neo4jDataLoaders` or use the facade’s
   `create_data_loader()` factory.
4. Remove direct `Neo4jConnections` usage; rely on the facade for
   sessions and connection pooling.
5. Run the automated migration helpers and enable deprecation warnings
   to verify no legacy APIs remain.
6. Execute the Neo4j unit and integration tests to confirm behaviour is
   unchanged.
