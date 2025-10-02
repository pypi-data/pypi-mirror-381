from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.extended.root_relative_paths import (
    RootRelativePaths,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.snapshots.individual_file_system_snapshot_folders import (
    IndividualFileSystemSnapshotFolders,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.populators.file_system_snapshot_objects.file_system_snapshot_children_from_parent_adder import (
    add_file_system_snapshot_children_from_parent,
)
from nf_common_base.b_source.services.reporting_service.wrappers.run_and_log_function_wrapper import (
    run_and_log_function,
)


@run_and_log_function()
def populate_root_relative_path(
    root_relative_path: RootRelativePaths,
) -> None:
    # TODO: Think about compressed verses
    if isinstance(
        root_relative_path.snapshot,
        IndividualFileSystemSnapshotFolders,
    ):
        add_file_system_snapshot_children_from_parent(
            parent_file_system_snapshot_folder=root_relative_path.snapshot
        )
