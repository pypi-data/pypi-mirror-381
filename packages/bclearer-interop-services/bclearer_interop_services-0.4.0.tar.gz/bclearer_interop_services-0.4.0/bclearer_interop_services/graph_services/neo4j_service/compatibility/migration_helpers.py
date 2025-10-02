"""Utility helpers for migrating to the refactored Neo4j service."""

from __future__ import annotations

import re
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path

from bclearer_interop_services.graph_services.neo4j_service.compatibility.neo4j_compatibility_wrapper import (
    Neo4jCompatibilityWrapper,
)
from bclearer_interop_services.graph_services.neo4j_service.configurations.neo4j_configurations import (
    Neo4jConfigurations,
)


@dataclass(slots=True)
class MigrationIssue:
    """Describes a potential migration problem discovered in code or config."""

    message: str
    suggestion: str | None = None


@dataclass(slots=True)
class CodeChange:
    """Record describing an automatic code transformation."""

    description: str
    occurrences: int
    replacement: str


@dataclass(slots=True)
class CodeMigrationResult:
    """Outcome of running the code migration helper."""

    updated_code: str
    changes: list[CodeChange]
    issues: list[MigrationIssue]

    @property
    def has_changes(self) -> bool:
        """Return ``True`` when any replacements were applied."""
        return bool(self.changes)


@dataclass(slots=True)
class MigrationValidation:
    """Validation result for migrated code and configuration profiles."""

    issues: list[MigrationIssue]

    @property
    def is_successful(self) -> bool:
        """Return ``True`` when no validation issues were detected."""
        return not self.issues


@dataclass(slots=True)
class _ReplacementRule:
    pattern: re.Pattern[str]
    replacement: str
    description: str


@dataclass(slots=True)
class _LegacyPattern:
    pattern: re.Pattern[str]
    message: str
    suggestion: str | None = None


class Neo4jMigrationHelpers:
    """Helpers that automate common migration steps.

    The helpers provide three primary capabilities:

    * Convert legacy configuration formats to the new profile-based layout
    * Detect and automatically update common legacy code patterns
    * Validate that migrated code and configuration no longer rely on legacy APIs
    """

    _CODE_REPLACEMENTS: tuple[_ReplacementRule, ...] = (
        _ReplacementRule(
            re.compile(
                r"from bclearer_interop_services\.graph_services\.neo4j_service\.neo4j_service "
                r"import Neo4jService",
            ),
            "from bclearer_interop_services.graph_services.neo4j_service.neo4j_service_facade "
            "import Neo4jServiceFacade",
            "Update legacy Neo4jService import to the service facade",
        ),
        _ReplacementRule(
            re.compile(r"\bNeo4jService\("),
            "Neo4jServiceFacade(",
            "Replace Neo4jService construction with Neo4jServiceFacade",
        ),
        _ReplacementRule(
            re.compile(r"neo4j_data_load_orchestrators"),
            "neo4j_data_loaders",
            "Rename module import to neo4j_data_loaders",
        ),
        _ReplacementRule(
            re.compile(r"Neo4jDataLoadOrchestrators"),
            "Neo4jDataLoaders",
            "Rename class usage to Neo4jDataLoaders",
        ),
    )

    _LEGACY_PATTERNS: tuple[_LegacyPattern, ...] = (
        _LegacyPattern(
            re.compile(r"\bNeo4jService\b"),
            "Legacy 'Neo4jService' API detected.",
            "Instantiate 'Neo4jServiceFacade' instead.",
        ),
        _LegacyPattern(
            re.compile(r"\bNeo4jDataLoadOrchestrators\b"),
            "Legacy 'Neo4jDataLoadOrchestrators' class detected.",
            "Use 'Neo4jDataLoaders'.",
        ),
        _LegacyPattern(
            re.compile(r"\bneo4j_data_load_orchestrators\b"),
            "Legacy neo4j_data_load_orchestrators module import detected.",
            "Import from 'neo4j_data_loaders' instead.",
        ),
        _LegacyPattern(
            re.compile(r"\bNeo4jConnections\b"),
            "Legacy 'Neo4jConnections' helper detected.",
            "Leverage 'Neo4jServiceFacade.connection_pool' or 'Neo4jDatabases'.",
        ),
        _LegacyPattern(
            re.compile(r"\bNeo4jCompatibilityWrapper\b"),
            "Compatibility wrapper usage detected.",
            "Instantiate 'Neo4jServiceFacade' directly where possible.",
        ),
    )

    @classmethod
    def migrate_configuration(
        cls,
        legacy_data: Mapping[str, object],
        *,
        profile: str = "default",
    ) -> dict[str, dict[str, str]]:
        """Convert a legacy configuration mapping to the profile structure."""
        return Neo4jCompatibilityWrapper.convert_configuration(
            legacy_data,
            profile=profile,
        )

    @classmethod
    def migrate_configuration_file(
        cls,
        legacy_file: str | Path,
        *,
        profile: str = "default",
        output_file: str | Path | None = None,
    ) -> dict[str, dict[str, str]]:
        """Convert a legacy configuration file and optionally persist the result."""
        return Neo4jCompatibilityWrapper.convert_configuration_file(
            legacy_file,
            profile=profile,
            output_file=output_file,
        )

    @classmethod
    def update_code(cls, code: str) -> CodeMigrationResult:
        """Apply automatic updates to code snippets using legacy APIs."""
        updated = code
        applied_changes: list[CodeChange] = []

        for rule in cls._CODE_REPLACEMENTS:
            matches = list(rule.pattern.finditer(updated))
            if not matches:
                continue
            updated = rule.pattern.sub(rule.replacement, updated)
            applied_changes.append(
                CodeChange(
                    description=rule.description,
                    occurrences=len(matches),
                    replacement=rule.replacement,
                ),
            )

        issues = cls._collect_legacy_issues(updated)
        return CodeMigrationResult(
            updated_code=updated,
            changes=applied_changes,
            issues=issues,
        )

    @classmethod
    def update_code_file(
        cls,
        file_path: str | Path,
        *,
        in_place: bool = False,
        encoding: str = "utf-8",
    ) -> CodeMigrationResult:
        """Apply ``update_code`` to a file and optionally persist changes."""
        path = Path(file_path)
        original = path.read_text(encoding=encoding)
        result = cls.update_code(original)
        if in_place and result.updated_code != original:
            path.write_text(result.updated_code, encoding=encoding)
        return result

    @classmethod
    def validate_migration(
        cls,
        code: str,
        configurations: Mapping[str, Mapping[str, object]] | None = None,
    ) -> MigrationValidation:
        """Validate migrated code and optional configuration mappings."""
        issues = cls._collect_legacy_issues(code)
        issues.extend(cls._validate_configurations(configurations))
        return MigrationValidation(issues)

    @classmethod
    def _collect_legacy_issues(cls, code: str) -> list[MigrationIssue]:
        issues: list[MigrationIssue] = []
        for pattern in cls._LEGACY_PATTERNS:
            for match in pattern.pattern.finditer(code):
                issues.append(
                    MigrationIssue(
                        message=pattern.message,
                        suggestion=pattern.suggestion,
                    ),
                )
        return issues

    @classmethod
    def _validate_configurations(
        cls,
        configurations: Mapping[str, Mapping[str, object]] | None,
    ) -> list[MigrationIssue]:
        if configurations is None:
            return []

        issues: list[MigrationIssue] = []
        for profile, data in configurations.items():
            try:
                Neo4jConfigurations(**dict(data))
            except (TypeError, ValueError) as exc:
                issues.append(
                    MigrationIssue(
                        message=(
                            f"Configuration profile '{profile}' failed validation: {exc}"
                        ),
                        suggestion=(
                            "Ensure the profile defines uri, database_name, "
                            "user_name and password."
                        ),
                    ),
                )
        return issues


__all__ = [
    "CodeChange",
    "CodeMigrationResult",
    "MigrationIssue",
    "MigrationValidation",
    "Neo4jMigrationHelpers",
]
