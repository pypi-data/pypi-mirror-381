from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshot_multiverse.verses.base_file_system_snapshot_multiverses import (
    BaseFileSystemSnapshotMultiverses,
)


class NullFileSystemSnapshotMultiverses(
    BaseFileSystemSnapshotMultiverses
):
    def __init__(self):
        super().__init__()
