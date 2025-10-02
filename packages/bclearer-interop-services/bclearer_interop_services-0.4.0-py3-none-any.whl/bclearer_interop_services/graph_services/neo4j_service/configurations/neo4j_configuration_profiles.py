"""Profile loader for Neo4j configurations.

Provides environment-specific profile loading with environment variable
overrides and Neo4j Aura auto-detection.
"""

from __future__ import annotations

import os
from typing import Any

from .neo4j_configurations import Neo4jConfigurations


class Neo4jConfigurationProfiles:
    """Load configuration profiles for the Neo4j service."""

    ENV_VARS: dict[str, str] = {
        "uri": "NEO4J_URI",
        "database_name": "NEO4J_DATABASE",
        "user_name": "NEO4J_USERNAME",
        "password": "NEO4J_PASSWORD",
    }

    @classmethod
    def load(
        cls,
        configuration_file: str,
        profile: str = "default",
    ) -> Neo4jConfigurations:
        """Load profile configuration with overrides and Aura detection."""
        profile_data = Neo4jConfigurations.validate_file(
            configuration_file,
            profile,
        )
        profile_data = cls._apply_env_overrides(profile_data)
        profile_data = cls._detect_aura(profile_data)
        return Neo4jConfigurations(
            uri=profile_data["uri"],
            database_name=profile_data["database_name"],
            user_name=profile_data["user_name"],
            password=profile_data["password"],
        )

    @classmethod
    def _apply_env_overrides(cls, config: dict[str, Any]) -> dict[str, Any]:
        """Override configuration values with environment variables if set."""
        for field, env_var in cls.ENV_VARS.items():
            value = os.getenv(env_var)
            if value:
                config[field] = value
        return config

    @staticmethod
    def _detect_aura(config: dict[str, Any]) -> dict[str, Any]:
        """Detect Neo4j Aura and adjust URI scheme accordingly."""
        uri = config.get("uri", "")
        if "neo4j.io" in uri and not uri.startswith("neo4j+s://"):
            tail = uri.split("://", 1)[1] if "://" in uri else uri
            config["uri"] = f"neo4j+s://{tail}"
        return config
