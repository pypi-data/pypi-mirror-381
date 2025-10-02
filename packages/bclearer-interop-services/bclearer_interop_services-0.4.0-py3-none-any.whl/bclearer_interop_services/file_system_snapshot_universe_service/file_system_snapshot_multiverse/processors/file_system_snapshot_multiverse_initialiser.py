from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshot_multiverse.verses.file_system_snapshot_multiverses import (
    FileSystemSnapshotMultiverses,
)
from nf_common_base.b_source.services.reporting_service.wrappers.run_and_log_function_wrapper import (
    run_and_log_function,
)


# TODO: is this encapsulation needed?
@run_and_log_function()
def initialise_file_system_snapshot_multiverse() -> (
    FileSystemSnapshotMultiverses
):
    file_system_snapshot_multiverse = (
        FileSystemSnapshotMultiverses()
    )

    return (
        file_system_snapshot_multiverse
    )
