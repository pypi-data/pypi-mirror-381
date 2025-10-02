from pathlib import Path

from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.extended.relative_paths import (
    RelativePaths,
)


class NonRootRelativePaths(
    RelativePaths
):
    def __init__(
        self,
        relative_path: Path,
        relative_path_parent: "RelativePaths",
    ):
        self.relative_path_parent = (
            relative_path_parent
        )

        relative_path_parent.add_relative_path_child(
            relative_path_child=self
        )

        super().__init__(
            base_hr_name=relative_path.name,
            relative_path=relative_path,
        )
