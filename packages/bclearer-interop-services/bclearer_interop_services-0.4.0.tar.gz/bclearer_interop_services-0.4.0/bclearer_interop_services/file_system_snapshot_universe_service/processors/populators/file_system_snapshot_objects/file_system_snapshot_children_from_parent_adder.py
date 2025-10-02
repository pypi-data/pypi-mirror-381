from nf_common_base.b_source.common.configurations.datastructure.logging_inspection_level_b_enums import (
    LoggingInspectionLevelBEnums,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.snapshots.individual_file_system_snapshot_folders import (
    IndividualFileSystemSnapshotFolders,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.populators.file_system_snapshot_objects.child_file_system_snapshot_object_creator import (
    create_child_file_system_snapshot_object,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.populators.file_system_snapshot_objects.first_level_deep_file_system_objects_for_snapshot_hierarchy_getter import (
    get_first_level_children_file_system_object_paths_for_snapshot_hierarchy,
)
from nf_common_base.b_source.services.reporting_service.reporters.inspection_message_logger import (
    log_inspection_message,
)
from nf_common_base.b_source.services.reporting_service.wrappers.run_and_log_function_wrapper import (
    run_and_log_function,
)


@run_and_log_function()
def add_file_system_snapshot_children_from_parent(
    parent_file_system_snapshot_folder: IndividualFileSystemSnapshotFolders,
) -> None:
    folder = (
        parent_file_system_snapshot_folder.get_file_system_object()
    )

    first_level_children_paths = get_first_level_children_file_system_object_paths_for_snapshot_hierarchy(
        input_file_system_object=folder,
        extension_to_filter=str(),
        parent_file_system_snapshot_folder=parent_file_system_snapshot_folder,
    )

    for (
        child_path_string
    ) in first_level_children_paths:
        log_inspection_message(
            message="Creating child file system snapshot for: {0}".format(
                child_path_string
            ),
            logging_inspection_level_b_enum=LoggingInspectionLevelBEnums.INFO,
        )

        child_file_system_snapshot_object = create_child_file_system_snapshot_object(
            parent_file_system_snapshot_folder=parent_file_system_snapshot_folder,
            child_path_string=child_path_string,
        )

        if isinstance(
            child_file_system_snapshot_object,
            IndividualFileSystemSnapshotFolders,
        ):
            log_inspection_message(
                message="Adding file system snapshot children for: {0}".format(
                    child_file_system_snapshot_object.base_hr_name
                ),
                logging_inspection_level_b_enum=LoggingInspectionLevelBEnums.INFO,
            )

            add_file_system_snapshot_children_from_parent(
                parent_file_system_snapshot_folder=child_file_system_snapshot_object
            )
