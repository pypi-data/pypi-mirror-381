from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.extended.root_relative_paths import (
    RootRelativePaths,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.snapshots.file_system_snapshot_objects import (
    FileSystemSnapshotObjects,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.populators.sum_objects.exclusive_ancestor_snapshot_sum_objects_populator import (
    populate_exclusive_ancestor_snapshot_sum_objects,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.populators.sum_objects.exclusive_descendant_snapshot_sum_objects_populator import (
    populate_exclusive_descendant_snapshot_sum_objects,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.populators.sum_objects.inclusive_ancestor_snapshot_sum_objects_populator import (
    populate_inclusive_ancestor_snapshot_sum_objects,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.populators.sum_objects.inclusive_descendant_snapshot_sum_objects_populator import (
    populate_inclusive_descendant_snapshot_sum_objects,
)
from nf_common_base.b_source.services.reporting_service.wrappers.run_and_log_function_wrapper import (
    run_and_log_function,
)


@run_and_log_function()
def populate_snapshot_sum_objects(
    root_relative_path: RootRelativePaths,
) -> None:
    if isinstance(
        root_relative_path.snapshot,
        FileSystemSnapshotObjects,
    ):
        populate_inclusive_ancestor_snapshot_sum_objects(
            file_system_snapshot_object=root_relative_path.snapshot
        )

        populate_inclusive_descendant_snapshot_sum_objects(
            file_system_snapshot_object=root_relative_path.snapshot
        )

        populate_exclusive_ancestor_snapshot_sum_objects(
            file_system_snapshot_object=root_relative_path.snapshot
        )

        populate_exclusive_descendant_snapshot_sum_objects(
            file_system_snapshot_object=root_relative_path.snapshot
        )
