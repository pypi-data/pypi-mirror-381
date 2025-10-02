from nf_common_base.b_source.common.configurations.b_configurations.b_configurations import (
    BConfigurations,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshot_multiverse.verses.file_system_snapshot_multiverses import (
    FileSystemSnapshotMultiverses,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.input_root_file_system_snapshot_container_folder_processor import (
    process_input_root_file_system_snapshot_container_folder,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.configuration_functions.runs_container_folder_setuper import (
    setup_runs_container_folder,
)


# TODO: process_x - or run_all_x's
#  process_input_root_file_system_snapshot_container_folders?? - DONE
def process_input_root_file_system_snapshots_container_folders(
    file_system_snapshot_multiverse: FileSystemSnapshotMultiverses,
):
    runs_container_folder = setup_runs_container_folder(
        file_system_snapshot_multiverse=file_system_snapshot_multiverse
    )

    # TODO: input_root_file_system_snapshot_container_folders?? - DONE
    input_root_file_system_snapshot_container_folders = (
        BConfigurations.INPUT_ROOT_FILE_SYSTEM_OBJECTS
    )

    for (
        iteration_index,
        input_root_file_system_snapshot_container_folder,
    ) in enumerate(
        input_root_file_system_snapshot_container_folders
    ):
        # TODO: process/run_x
        #  process_input_root_file_system_snapshot_container_folder?? - DONE
        process_input_root_file_system_snapshot_container_folder(
            input_root_file_system_snapshot_container_folder=input_root_file_system_snapshot_container_folder,
            file_system_snapshot_multiverse=file_system_snapshot_multiverse,
            iteration_index=iteration_index,
            runs_container_folder=runs_container_folder,
        )
