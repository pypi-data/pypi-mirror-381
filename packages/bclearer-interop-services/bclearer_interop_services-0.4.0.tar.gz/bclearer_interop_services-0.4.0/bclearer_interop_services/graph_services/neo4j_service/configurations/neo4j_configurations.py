import json
import os
from dataclasses import dataclass
from typing import Any, ClassVar


@dataclass
class Neo4jConfigurations:
    uri: str
    database_name: str
    user_name: str
    password: str

    REQUIRED_FIELDS: ClassVar[dict[str, type]] = {
        "uri": str,
        "database_name": str,
        "user_name": str,
        "password": str,
    }

    def __post_init__(self) -> None:
        self.validate()

    def validate(self) -> None:
        missing: list[str] = []
        for field_name, field_type in self.REQUIRED_FIELDS.items():
            value = getattr(self, field_name, None)
            if not isinstance(value, field_type) or not value:
                missing.append(f"{field_name}: {field_type.__name__}")
        if missing:
            raise ValueError(
                "Invalid configuration: " + ", ".join(missing),
            )

    @classmethod
    def validate_file(
        cls,
        configuration_file: str,
        profile: str = "default",
    ) -> dict[str, Any]:
        try:
            with open(configuration_file) as file:
                all_profiles: dict[str, dict[str, Any]] = json.load(file)
        except json.JSONDecodeError as exc:
            raise ValueError(
                f"Invalid JSON in configuration file: {exc}",
            ) from exc
        except OSError as exc:
            raise ValueError(
                f"Error reading configuration file: {exc}",
            ) from exc

        if profile not in all_profiles:
            raise ValueError(
                f"Configuration profile '{profile}' not found",
            )

        profile_data = all_profiles[profile]

        missing = [name for name in cls.REQUIRED_FIELDS if name not in profile_data]
        if missing:
            raise ValueError(
                "Missing configuration parameters: " + ", ".join(missing),
            )

        return profile_data

    @classmethod
    def from_file(
        cls,
        configuration_file: str,
        profile: str = "default",
    ) -> "Neo4jConfigurations":
        profile_data = cls.validate_file(
            configuration_file,
            profile,
        )
        return cls(
            uri=profile_data["uri"],
            database_name=profile_data["database_name"],
            user_name=profile_data["user_name"],
            password=profile_data["password"],
        )

    @classmethod
    def from_environment(cls) -> "Neo4jConfigurations":
        return cls(
            uri=os.getenv("NEO4J_URI", ""),
            database_name=os.getenv("NEO4J_DATABASE", ""),
            user_name=os.getenv("NEO4J_USERNAME", ""),
            password=os.getenv("NEO4J_PASSWORD", ""),
        )
