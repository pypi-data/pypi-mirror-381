from __future__ import annotations

"""Structured exceptions for the Neo4j service."""

from collections.abc import Mapping


class Neo4jServiceError(Exception):
    """Base class for all Neo4j service errors."""

    error_code = "NEO4J_SERVICE_ERROR"

    def __init__(
        self,
        message: str,
        *,
        error_code: str | None = None,
        context: (
            Mapping[str, object] | None
        ) = None,
        recovery_hint: (
            str | None
        ) = None,
        cause: Exception | None = None,
    ) -> None:
        super().__init__(message)
        self.message = message
        self._error_code = (
            error_code
            or self.error_code
        )
        self.context: dict[
            str, object,
        ] = (
            dict(context)
            if context
            else {}
        )
        self.recovery_hint = (
            recovery_hint
        )
        self.cause = cause

    @property
    def code(self) -> str:
        """Return the error code associated with the exception."""
        return self._error_code

    def add_context(
        self, **extra_context: object,
    ) -> None:
        """Augment the error with additional diagnostic context."""
        self.context.update(
            extra_context,
        )

    def to_dict(
        self,
    ) -> dict[str, object]:
        """Serialise the error for logging or structured reporting."""
        data: dict[str, object] = {
            "code": self.code,
            "message": self.message,
            "context": dict(
                self.context,
            ),
        }
        if self.recovery_hint:
            data["recovery_hint"] = (
                self.recovery_hint
            )
        if self.cause:
            data["cause"] = repr(
                self.cause,
            )
        return data

    def __str__(self) -> str:
        segments = [
            f"[{self.code}] {self.message}",
        ]
        details: list[str] = []
        if self.context:
            context_parts = ", ".join(
                f"{key}={value!r}"
                for key, value in self.context.items()
            )
            details.append(
                f"context: {context_parts}",
            )
        if self.recovery_hint:
            details.append(
                f"hint: {self.recovery_hint}",
            )
        if self.cause:
            details.append(
                f"cause: {self.cause!r}",
            )
        if details:
            segments.append(
                f"({'; '.join(details)})",
            )
        return " ".join(segments)


class Neo4jConfigurationError(
    Neo4jServiceError,
):
    """Configuration is missing or invalid."""

    error_code = (
        "NEO4J_CONFIGURATION_ERROR"
    )


class Neo4jAuthenticationError(
    Neo4jServiceError,
):
    """Authentication with Neo4j failed."""

    error_code = (
        "NEO4J_AUTHENTICATION_ERROR"
    )


class Neo4jConnectionError(
    Neo4jServiceError,
):
    """Low-level connection to Neo4j failed."""

    error_code = (
        "NEO4J_CONNECTION_ERROR"
    )


class Neo4jSessionError(
    Neo4jServiceError,
):
    """Session acquisition or management failed."""

    error_code = "NEO4J_SESSION_ERROR"


class Neo4jTransactionError(
    Neo4jServiceError,
):
    """A transactional operation failed."""

    error_code = (
        "NEO4J_TRANSACTION_ERROR"
    )


class Neo4jQueryError(
    Neo4jServiceError,
):
    """A Cypher query or parameter binding failed."""

    error_code = "NEO4J_QUERY_ERROR"


class Neo4jDataLoadError(
    Neo4jServiceError,
):
    """Loading data into Neo4j was unsuccessful."""

    error_code = "NEO4J_DATA_LOAD_ERROR"


class Neo4jDataExportError(
    Neo4jServiceError,
):
    """Exporting data from Neo4j failed."""

    error_code = (
        "NEO4J_DATA_EXPORT_ERROR"
    )


class Neo4jSchemaError(
    Neo4jServiceError,
):
    """Schema management operation failed."""

    error_code = "NEO4J_SCHEMA_ERROR"


class Neo4jAlgorithmError(
    Neo4jServiceError,
):
    """Graph algorithm execution encountered an error."""

    error_code = "NEO4J_ALGORITHM_ERROR"


class Neo4jAsyncOperationError(
    Neo4jServiceError,
):
    """An asynchronous Neo4j operation failed."""

    error_code = (
        "NEO4J_ASYNC_OPERATION_ERROR"
    )


class Neo4jCompatibilityError(
    Neo4jServiceError,
):
    """Legacy compatibility layer failed to complete."""

    error_code = (
        "NEO4J_COMPATIBILITY_ERROR"
    )


__all__ = [
    "Neo4jAlgorithmError",
    "Neo4jAsyncOperationError",
    "Neo4jAuthenticationError",
    "Neo4jCompatibilityError",
    "Neo4jConfigurationError",
    "Neo4jConnectionError",
    "Neo4jDataExportError",
    "Neo4jDataLoadError",
    "Neo4jQueryError",
    "Neo4jSchemaError",
    "Neo4jServiceError",
    "Neo4jSessionError",
    "Neo4jTransactionError",
]
