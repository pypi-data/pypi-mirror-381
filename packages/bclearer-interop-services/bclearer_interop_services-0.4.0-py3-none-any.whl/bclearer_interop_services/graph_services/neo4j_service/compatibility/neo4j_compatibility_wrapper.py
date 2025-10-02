"""Compatibility wrapper for the refactored Neo4j service."""

from __future__ import annotations

import json
import warnings
from collections.abc import Iterable, Mapping
from pathlib import Path
from typing import ClassVar, Self

from bclearer_interop_services.graph_services.neo4j_service.configurations.neo4j_configurations import (
    Neo4jConfigurations,
)
from bclearer_interop_services.graph_services.neo4j_service.neo4j_service_facade import (
    Neo4jServiceFacade,
)


class Neo4jCompatibilityWrapper:
    """Bridge legacy Neo4j service APIs to :class:`Neo4jServiceFacade`.

    The compatibility wrapper preserves the public interface that existed
    before the refactor while delegating work to the new
    :class:`Neo4jServiceFacade`.  Each call emits a ``DeprecationWarning`` to
    guide users towards the modern facade and configuration formats.
    """

    _DEPRECATION_MESSAGE: ClassVar[str] = (
        "Neo4jCompatibilityWrapper is deprecated and will be removed in a "
        "future release. Instantiate Neo4jServiceFacade directly."
    )
    _API_WARNING_TEMPLATE: ClassVar[str] = (
        "The '%s' API accessed through Neo4jCompatibilityWrapper is "
        "deprecated. Use Neo4jServiceFacade.%s instead."
    )
    _KEY_ALIASES: ClassVar[dict[str, tuple[str, ...]]] = {
        "uri": (
            "uri",
            "bolt_uri",
            "url",
            "neo4j_uri",
            "connection_uri",
        ),
        "database_name": (
            "database_name",
            "database",
            "db_name",
            "neo4j_database",
        ),
        "user_name": (
            "user_name",
            "username",
            "user",
            "neo4j_user",
            "neo4j_username",
        ),
        "password": (
            "password",
            "pass",
            "secret",
            "neo4j_password",
        ),
    }

    def __init__(
        self,
        configuration_file: str | None = None,
        *,
        configuration: (
            Neo4jConfigurations | Mapping[str, object] | None
        ) = None,
        profile: str = "default",
        **facade_kwargs: object,
    ) -> None:
        self._warn_deprecation(self._DEPRECATION_MESSAGE)
        config_object = self._prepare_configuration(
            configuration,
            configuration_file,
            profile,
        )

        facade_kwargs = dict(facade_kwargs)
        facade_kwargs.pop("configuration", None)
        facade_kwargs.pop("configuration_file", None)
        facade_kwargs["configuration"] = config_object
        self._facade = Neo4jServiceFacade(**facade_kwargs)

    @property
    def facade(self) -> Neo4jServiceFacade:
        """Return the underlying :class:`Neo4jServiceFacade` instance."""
        return self._facade

    @property
    def configuration(self) -> Neo4jConfigurations:
        """Expose the active configuration for backward compatibility."""
        return self._facade.configuration

    def close(self) -> None:
        """Close managed resources after emitting a deprecation warning."""
        self._warn_api_usage("close")
        self._facade.close()

    def __enter__(self) -> Self:
        self._warn_api_usage("__enter__")
        self._facade.__enter__()
        return self

    def __exit__(
        self,
        exc_type,
        exc,
        tb,
    ) -> None:
        self._warn_api_usage("__exit__")
        self._facade.__exit__(exc_type, exc, tb)

    def __getattr__(self, name: str) -> object:
        if name.startswith("_"):
            msg = f"{self.__class__.__name__} has no attribute '{name}'"
            raise AttributeError(msg)
        attribute = getattr(self._facade, name)
        self._warn_api_usage(name)
        return attribute

    @classmethod
    def convert_configuration(
        cls,
        legacy_data: Mapping[str, object],
        *,
        profile: str = "default",
    ) -> dict[str, dict[str, str]]:
        """Convert a legacy configuration mapping into profile format."""
        connection_data = cls._normalise_configuration(legacy_data)
        return {profile: connection_data}

    @classmethod
    def convert_configuration_file(
        cls,
        legacy_file: str | Path,
        *,
        profile: str = "default",
        output_file: str | Path | None = None,
    ) -> dict[str, dict[str, str]]:
        """Convert a legacy configuration file and optionally write output."""
        legacy_content = cls._read_json(legacy_file)
        converted = cls.convert_configuration(
            legacy_content,
            profile=profile,
        )
        if output_file is not None:
            Path(output_file).write_text(
                json.dumps(converted, indent=2),
                encoding="utf-8",
            )
        return converted

    @classmethod
    def _prepare_configuration(
        cls,
        configuration: (
            Neo4jConfigurations | Mapping[str, object] | None
        ),
        configuration_file: str | None,
        profile: str,
    ) -> Neo4jConfigurations:
        if isinstance(configuration, Neo4jConfigurations):
            return configuration
        if isinstance(configuration, Mapping):
            data = cls._normalise_configuration(configuration)
            return Neo4jConfigurations(**data)
        if configuration is not None:
            msg = (
                "configuration must be a Neo4jConfigurations instance or mapping"
            )
            raise TypeError(msg)
        if configuration_file is None:
            msg = "configuration or configuration_file must be provided"
            raise ValueError(msg)
        try:
            return Neo4jConfigurations.from_file(
                configuration_file,
                profile=profile,
            )
        except ValueError:
            legacy_content = cls._read_json(configuration_file)
            converted = cls.convert_configuration(
                legacy_content,
                profile=profile,
            )
            profile_data = converted.get(profile)
            if profile_data is None:
                profile_data = next(iter(converted.values()))
            return Neo4jConfigurations(**profile_data)

    @classmethod
    def _normalise_configuration(
        cls,
        legacy_data: Mapping[str, object],
    ) -> dict[str, str]:
        result: dict[str, str] = {}
        auth_mapping = cls._find_mapping(legacy_data, ("authentication", "auth"))
        for new_key, aliases in cls._KEY_ALIASES.items():
            value = cls._find_value_recursive(legacy_data, aliases)
            if value is None and new_key == "uri":
                value = cls._find_uri_recursive(legacy_data)
            if value is None and new_key == "user_name" and auth_mapping is not None:
                value = cls._find_value(
                    auth_mapping,
                    ("user_name", "username", "user"),
                )
            if value is None and new_key == "password" and auth_mapping is not None:
                value = cls._find_value(
                    auth_mapping,
                    ("password", "pass", "secret"),
                )
            if value is None:
                msg = (
                    "Could not determine Neo4j connection parameters from "
                    "legacy configuration"
                )
                raise ValueError(msg)
            result[new_key] = str(value)
        return result

    @classmethod
    def _find_uri_recursive(
        cls,
        legacy_data: Mapping[str, object],
    ) -> str | None:
        for candidate in cls._iter_candidates(legacy_data):
            value = cls._find_value(candidate, cls._KEY_ALIASES["uri"])
            if value is not None:
                return str(value)
            composed = cls._compose_uri(candidate)
            if composed is not None:
                return composed
        return None

    @staticmethod
    def _compose_uri(candidate: Mapping[str, object]) -> str | None:
        host = candidate.get("host") or candidate.get("hostname")
        port = candidate.get("port")
        scheme = candidate.get("scheme") or candidate.get("protocol") or "neo4j"
        if host and port:
            return f"{scheme}://{host}:{port}"
        if host:
            return f"{scheme}://{host}"
        return None

    @staticmethod
    def _find_value(
        candidate: Mapping[str, object],
        keys: Iterable[str],
    ) -> object | None:
        for key in keys:
            if key in candidate:
                value = candidate[key]
                if value is not None:
                    return value
        return None

    @classmethod
    def _find_value_recursive(
        cls,
        legacy_data: Mapping[str, object],
        keys: Iterable[str],
    ) -> object | None:
        for candidate in cls._iter_candidates(legacy_data):
            value = cls._find_value(candidate, keys)
            if value is not None:
                return value
        return None

    @classmethod
    def _find_mapping(
        cls,
        legacy_data: Mapping[str, object],
        names: Iterable[str],
    ) -> Mapping[str, object] | None:
        for candidate in cls._iter_candidates(legacy_data):
            for name in names:
                mapping = candidate.get(name)
                if isinstance(mapping, Mapping):
                    return mapping
        return None

    @classmethod
    def _iter_candidates(
        cls,
        data: Mapping[str, object],
    ) -> Iterable[Mapping[str, object]]:
        stack: list[Mapping[str, object]] = [data]
        seen: set[int] = set()
        while stack:
            current = stack.pop()
            identifier = id(current)
            if identifier in seen:
                continue
            seen.add(identifier)
            yield current
            for value in current.values():
                if isinstance(value, Mapping):
                    stack.append(value)

    @staticmethod
    def _read_json(file_path: str | Path) -> Mapping[str, object]:
        try:
            content = Path(file_path).read_text(encoding="utf-8")
        except OSError as exc:  # pragma: no cover - defensive
            raise ValueError(f"Unable to read configuration file: {exc}") from exc
        try:
            return json.loads(content)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Invalid JSON configuration file '{file_path}': {exc}",
            ) from exc

    @staticmethod
    def _warn_deprecation(message: str) -> None:
        warnings.warn(message, DeprecationWarning, stacklevel=3)

    def _warn_api_usage(self, api_name: str) -> None:
        warnings.warn(
            self._API_WARNING_TEMPLATE % (api_name, api_name),
            DeprecationWarning,
            stacklevel=3,
        )
