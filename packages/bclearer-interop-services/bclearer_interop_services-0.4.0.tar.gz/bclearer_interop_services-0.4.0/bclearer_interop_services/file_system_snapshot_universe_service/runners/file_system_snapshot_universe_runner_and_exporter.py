from nf_common_base.b_source.services.file_system_snapshot_universe_service.configurations.file_system_snapshot_configurations import (
    FileSystemSnapshotConfigurations,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.file_system_snapshot_universe_if_inspection_is_enabled_exporter import (
    export_file_system_snapshot_universe_if_inspection_is_enabled,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.verses.file_system_snapshot_universes import (
    FileSystemSnapshotUniverses,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.runners.file_system_snapshot_service_handler import (
    handle_file_system_snapshot_service,
)


# TODO: Find duplicates (single service test) and merge
def run_and_export_file_system_snapshot_universe(
    file_system_snapshot_configuration: FileSystemSnapshotConfigurations,
) -> FileSystemSnapshotUniverses:
    file_system_snapshot_universe = handle_file_system_snapshot_service(
        file_system_snapshot_configuration=file_system_snapshot_configuration
    )

    export_file_system_snapshot_universe_if_inspection_is_enabled(
        file_system_snapshot_universe=file_system_snapshot_universe,
        output_folder=file_system_snapshot_configuration.single_fssu_output_folder,
    )

    return file_system_snapshot_universe
