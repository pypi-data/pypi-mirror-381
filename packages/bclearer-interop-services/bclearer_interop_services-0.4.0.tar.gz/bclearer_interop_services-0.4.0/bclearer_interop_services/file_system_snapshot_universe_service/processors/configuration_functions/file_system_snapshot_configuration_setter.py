from nf_common_base.b_source.services.file_system_service.objects.folders import (
    Folders,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.configurations.file_system_snapshot_configurations import (
    FileSystemSnapshotConfigurations,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.configuration_functions.single_fssu_output_folder_getter import (
    get_single_fssu_output_folder,
)


def set_file_system_snapshot_configuration(
    file_system_snapshot_multiverse,
    input_root_file_system_snapshot_container_folder: Folders,
    single_universe_runs_container_folder: Folders,
    iteration_index: int,
) -> FileSystemSnapshotConfigurations:
    single_fssu_output_folder = get_single_fssu_output_folder(
        file_system_snapshot_multiverse=file_system_snapshot_multiverse,
        single_universe_runs_container_folder=single_universe_runs_container_folder,
        iteration_index=iteration_index,
    )

    file_system_snapshot_configuration = FileSystemSnapshotConfigurations(
        single_fssu_output_folder=single_fssu_output_folder,
        input_snapshot_container_folder=input_root_file_system_snapshot_container_folder,
        remove_temporary_root_folder=False,
    )

    return file_system_snapshot_configuration
