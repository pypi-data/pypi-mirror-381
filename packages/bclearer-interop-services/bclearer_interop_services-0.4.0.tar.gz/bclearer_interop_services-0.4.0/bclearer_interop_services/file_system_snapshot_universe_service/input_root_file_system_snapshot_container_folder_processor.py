from nf_common_base.b_source.services.file_system_service.objects.folders import (
    Folders,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshot_multiverse.verses.file_system_snapshot_multiverses import (
    FileSystemSnapshotMultiverses,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.configuration_functions.file_system_snapshot_configuration_setter import (
    set_file_system_snapshot_configuration,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.runners.file_system_snapshot_universe_runner_and_exporter import (
    run_and_export_file_system_snapshot_universe,
)


def process_input_root_file_system_snapshot_container_folder(
    input_root_file_system_snapshot_container_folder: Folders,
    file_system_snapshot_multiverse: FileSystemSnapshotMultiverses,
    iteration_index: int,
    runs_container_folder: Folders,
):
    file_system_snapshot_configuration = set_file_system_snapshot_configuration(
        file_system_snapshot_multiverse=file_system_snapshot_multiverse,
        input_root_file_system_snapshot_container_folder=input_root_file_system_snapshot_container_folder,
        single_universe_runs_container_folder=runs_container_folder,
        iteration_index=iteration_index,
    )

    file_system_snapshot_universe = run_and_export_file_system_snapshot_universe(
        file_system_snapshot_configuration=file_system_snapshot_configuration
    )

    if (
        not file_system_snapshot_multiverse.is_null_file_system_snapshot_multiverse()
    ):
        file_system_snapshot_multiverse.add_universe_to_registry(
            file_system_snapshot_universe=file_system_snapshot_universe
        )
