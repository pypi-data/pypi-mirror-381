import json
from typing import Any


class RaphtoryConfigurations:
    """Configuration loader for
    Raphtory graph service.
    """

    REQUIRED_PARAMETERS = [
        "graph_directory",
        "memory_limit_gb",
        "enable_persistence",
    ]

    def __init__(
        self,
        configuration_file: str,
        profile: str = "default",
    ) -> None:
        profile_data = self.validate(
            configuration_file,
            profile,
        )
        self.graph_directory: str = profile_data["graph_directory"]
        self.memory_limit_gb: int = profile_data["memory_limit_gb"]
        self.enable_persistence: bool = profile_data["enable_persistence"]
        self.graphql_enabled: bool = profile_data.get(
            "graphql_enabled",
            False,
        )
        self.persistence_path: str | None = profile_data.get(
            "persistence_path",
        )

    @classmethod
    def validate(
        cls,
        configuration_file: str,
        profile: str = "default",
    ) -> dict[str, Any]:
        try:
            with open(configuration_file) as file:
                all_profiles: dict[str, dict[str, Any]] = json.load(
                    file,
                )
        except json.JSONDecodeError as exc:  # pragma: no cover - exercised in tests
            raise ValueError(
                f"Invalid JSON in configuration file: {exc}",
            ) from exc
        except OSError as exc:  # pragma: no cover - exercised in tests
            raise ValueError(
                f"Error reading configuration file: {exc}",
            ) from exc

        if profile not in all_profiles:
            raise ValueError(
                f"Configuration profile '{profile}' not found",
            )

        profile_data = all_profiles[profile]

        missing = [
            param for param in cls.REQUIRED_PARAMETERS if param not in profile_data
        ]
        if missing:
            raise ValueError(
                "Missing configuration parameters: " + ", ".join(missing),
            )

        return profile_data


example_configuration = {
    "default": {
        "graph_directory": "/path/to/raphtory",
        "memory_limit_gb": 4,
        "enable_persistence": True,
        "graphql_enabled": False,
    },
}
