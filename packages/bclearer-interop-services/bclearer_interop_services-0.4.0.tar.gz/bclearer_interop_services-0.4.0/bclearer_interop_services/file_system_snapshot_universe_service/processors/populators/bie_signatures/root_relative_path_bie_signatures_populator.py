from nf_common_base.b_source.common.configurations.datastructure.logging_inspection_level_b_enums import (
    LoggingInspectionLevelBEnums,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.extended.root_relative_paths import (
    RootRelativePaths,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.snapshots.file_system_snapshot_objects import (
    FileSystemSnapshotObjects,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.verses.root_relative_path_bie_signature_registries import (
    RootRelativePathBieSignatureRegistries,
)
from nf_common_base.b_source.services.reporting_service.reporters.inspection_message_logger import (
    log_inspection_message,
)
from nf_common_base.b_source.services.reporting_service.wrappers.run_and_log_function_wrapper import (
    run_and_log_function,
)


@run_and_log_function()
def populate_root_relative_path_bie_signatures(
    bie_signature_registry: RootRelativePathBieSignatureRegistries,
    root_relative_path: RootRelativePaths,
) -> None:
    if isinstance(
        root_relative_path.snapshot,
        FileSystemSnapshotObjects,
    ):
        bie_signature_registry.add_file_system_snapshot_object_to_registry(
            file_system_snapshot_object=root_relative_path.snapshot
        )

        __add_file_system_snapshot_children_from_parent(
            bie_signature_registry=bie_signature_registry,
            file_system_snapshot_object=root_relative_path.snapshot,
        )


def __add_file_system_snapshot_children_from_parent(
    bie_signature_registry: RootRelativePathBieSignatureRegistries,
    file_system_snapshot_object: FileSystemSnapshotObjects,
) -> None:
    for (
        part
    ) in (
        file_system_snapshot_object.parts
    ):
        log_inspection_message(
            message="Adding file system snapshot children from parent: {0}".format(
                str(part.base_hr_name)
            ),
            logging_inspection_level_b_enum=LoggingInspectionLevelBEnums.INFO,
        )

        bie_signature_registry.add_file_system_snapshot_object_to_registry(
            file_system_snapshot_object=part
        )

        __add_file_system_snapshot_children_from_parent(
            bie_signature_registry=bie_signature_registry,
            file_system_snapshot_object=part,
        )
