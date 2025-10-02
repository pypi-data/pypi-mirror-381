from pathlib import Path

from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.file_system_snapshot_domain_literals import (
    FileSystemSnapshotDomainLiterals,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.extended.relative_paths import (
    RelativePaths,
)


class RootRelativePaths(RelativePaths):
    def __init__(self):
        relative_path = Path(str())

        super().__init__(
            base_hr_name=FileSystemSnapshotDomainLiterals.root_relative_path,
            relative_path=relative_path,
        )
