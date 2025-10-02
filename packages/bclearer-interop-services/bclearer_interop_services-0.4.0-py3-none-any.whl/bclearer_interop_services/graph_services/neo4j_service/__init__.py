from __future__ import annotations

import sys
from importlib import import_module
from importlib.metadata import PackageNotFoundError, version

import bclearer_interop_services.graph_services.neo4j_service.object_models as neo4j_object_models

try:
    __version__ = version("bclearer-neo4j-service")
except PackageNotFoundError:
    __version__ = "0.0.0"

sys.modules.setdefault(
    "neo4j_object_models",
    neo4j_object_models,
)

__all__ = [
    "AwsSecretsManagerCredentialProvider",
    "BaseCredentialProvider",
    "CircuitBreaker",
    "CircuitBreakerMetrics",
    "CircuitBreakerState",
    "CredentialProviderError",
    "EnvironmentVariableCredentialProvider",
    "HashicorpVaultCredentialProvider",
    "Neo4jAlgorithmError",
    "Neo4jAlgorithms",
    "Neo4jAsyncOperationError",
    "Neo4jAsyncSessions",
    "Neo4jAuthenticationError",
    "Neo4jCompatibilityWrapper",
    "Neo4jConfigurationError",
    "Neo4jConfigurationProfiles",
    "Neo4jConfigurations",
    "Neo4jConnectionError",
    "Neo4jConnectionPools",
    "Neo4jConnections",
    "Neo4jDataExportError",
    "Neo4jDataExporters",
    "Neo4jDataLoadError",
    "Neo4jDataLoadOrchestrators",
    "Neo4jDataLoaders",
    "Neo4jDatabases",
    "Neo4jMigrationHelpers",
    "Neo4jQueryBuilders",
    "Neo4jQueryError",
    "Neo4jSchemaError",
    "Neo4jSchemas",
    "Neo4jServiceError",
    "Neo4jServiceFacade",
    "Neo4jSessionError",
    "Neo4jSessions",
    "Neo4jTransactionError",
    "PerformanceMonitor",
    "PerformanceSample",
    "PerformanceSummary",
    "QueryPlanCache",
    "neo4j_object_models",
]

_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    "Neo4jServiceFacade": (
        ".neo4j_service_facade",
        "Neo4jServiceFacade",
    ),
    "Neo4jConfigurations": (
        ".configurations.neo4j_configurations",
        "Neo4jConfigurations",
    ),
    "Neo4jConfigurationProfiles": (
        ".configurations.neo4j_configuration_profiles",
        "Neo4jConfigurationProfiles",
    ),
    "Neo4jConnectionPools": (
        ".object_models.neo4j_connection_pools",
        "Neo4jConnectionPools",
    ),
    "Neo4jConnections": (
        ".object_models.neo4j_connections",
        "Neo4jConnections",
    ),
    "Neo4jDatabases": (
        ".object_models.neo4j_databases",
        "Neo4jDatabases",
    ),
    "Neo4jSessions": (
        ".object_models.neo4j_sessions",
        "Neo4jSessions",
    ),
    "Neo4jAsyncSessions": (
        ".object_models.neo4j_async_sessions",
        "Neo4jAsyncSessions",
    ),
    "Neo4jAlgorithms": (
        ".object_models.neo4j_algorithms",
        "Neo4jAlgorithms",
    ),
    "Neo4jSchemas": (
        ".object_models.neo4j_schemas",
        "Neo4jSchemas",
    ),
    "Neo4jQueryBuilders": (
        ".object_models.neo4j_query_builders",
        "Neo4jQueryBuilders",
    ),
    "QueryPlanCache": (
        ".object_models.neo4j_query_builders",
        "QueryPlanCache",
    ),
    "Neo4jDataLoaders": (
        ".orchestrators.neo4j_data_loaders",
        "Neo4jDataLoaders",
    ),
    "Neo4jDataLoadOrchestrators": (
        ".orchestrators.neo4j_data_loaders",
        "Neo4jDataLoadOrchestrators",
    ),
    "Neo4jDataExporters": (
        ".orchestrators.neo4j_data_exporters",
        "Neo4jDataExporters",
    ),
    "Neo4jCompatibilityWrapper": (
        ".compatibility.neo4j_compatibility_wrapper",
        "Neo4jCompatibilityWrapper",
    ),
    "Neo4jMigrationHelpers": (
        ".compatibility.migration_helpers",
        "Neo4jMigrationHelpers",
    ),
    "Neo4jServiceError": (
        ".exceptions",
        "Neo4jServiceError",
    ),
    "Neo4jConfigurationError": (
        ".exceptions",
        "Neo4jConfigurationError",
    ),
    "Neo4jAuthenticationError": (
        ".exceptions",
        "Neo4jAuthenticationError",
    ),
    "Neo4jConnectionError": (
        ".exceptions",
        "Neo4jConnectionError",
    ),
    "Neo4jSessionError": (
        ".exceptions",
        "Neo4jSessionError",
    ),
    "Neo4jTransactionError": (
        ".exceptions",
        "Neo4jTransactionError",
    ),
    "Neo4jQueryError": (
        ".exceptions",
        "Neo4jQueryError",
    ),
    "Neo4jDataLoadError": (
        ".exceptions",
        "Neo4jDataLoadError",
    ),
    "Neo4jDataExportError": (
        ".exceptions",
        "Neo4jDataExportError",
    ),
    "Neo4jSchemaError": (
        ".exceptions",
        "Neo4jSchemaError",
    ),
    "Neo4jAlgorithmError": (
        ".exceptions",
        "Neo4jAlgorithmError",
    ),
    "Neo4jAsyncOperationError": (
        ".exceptions",
        "Neo4jAsyncOperationError",
    ),
    "CredentialProviderError": (
        ".security.credential_providers",
        "CredentialProviderError",
    ),
    "BaseCredentialProvider": (
        ".security.credential_providers",
        "BaseCredentialProvider",
    ),
    "EnvironmentVariableCredentialProvider": (
        ".security.credential_providers",
        "EnvironmentVariableCredentialProvider",
    ),
    "HashicorpVaultCredentialProvider": (
        ".security.credential_providers",
        "HashicorpVaultCredentialProvider",
    ),
    "AwsSecretsManagerCredentialProvider": (
        ".security.credential_providers",
        "AwsSecretsManagerCredentialProvider",
    ),
    "PerformanceMonitor": (
        ".utils.performance_monitor",
        "PerformanceMonitor",
    ),
    "PerformanceSample": (
        ".utils.performance_monitor",
        "PerformanceSample",
    ),
    "PerformanceSummary": (
        ".utils.performance_monitor",
        "PerformanceSummary",
    ),
    "CircuitBreaker": (
        ".utils.circuit_breaker",
        "CircuitBreaker",
    ),
    "CircuitBreakerMetrics": (
        ".utils.circuit_breaker",
        "CircuitBreakerMetrics",
    ),
    "CircuitBreakerState": (
        ".utils.circuit_breaker",
        "CircuitBreakerState",
    ),
}


def __getattr__(name: str) -> object:
    try:
        module_path, attr_name = _LAZY_IMPORTS[name]
    except KeyError as error:  # pragma: no cover - defensive
        raise AttributeError(
            f"module {__name__!r} has no attribute {name!r}",
        ) from error
    module = import_module(f"{__name__}{module_path}")
    value = getattr(module, attr_name)
    globals()[name] = value
    return value


def __dir__() -> list[str]:  # pragma: no cover - trivial
    return sorted({*globals(), *__all__})
