from nf_common_base.b_source.common.infrastructure.nf.objects.verses.nf_multiverses import (
    NfMultiverses,
)


class BaseFileSystemSnapshotMultiverses(
    NfMultiverses
):
    def __init__(self):
        super().__init__()

    def is_null_file_system_snapshot_multiverse(
        self,
    ) -> bool:
        from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshot_multiverse.verses.null_file_system_snapshot_multiverses import (
            NullFileSystemSnapshotMultiverses,
        )

        if isinstance(
            self,
            NullFileSystemSnapshotMultiverses,
        ):
            return True

        return False
