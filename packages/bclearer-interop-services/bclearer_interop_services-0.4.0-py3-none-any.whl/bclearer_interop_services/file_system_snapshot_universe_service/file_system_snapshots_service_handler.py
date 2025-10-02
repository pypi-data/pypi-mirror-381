from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshot_multiverse.factories.file_system_snapshot_multiverse_from_b_configurations_factory import (
    create_file_system_snapshot_multiverse_from_b_configurations,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshot_multiverse.verses.file_system_snapshot_multiverses import (
    FileSystemSnapshotMultiverses,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.input_root_file_system_snapshots_container_folders_processor import (
    process_input_root_file_system_snapshots_container_folders,
)


def handle_file_system_snapshots_service() -> (
    FileSystemSnapshotMultiverses
):
    file_system_snapshot_multiverse = (
        create_file_system_snapshot_multiverse_from_b_configurations()
    )

    process_input_root_file_system_snapshots_container_folders(
        file_system_snapshot_multiverse=file_system_snapshot_multiverse
    )

    return (
        file_system_snapshot_multiverse
    )
