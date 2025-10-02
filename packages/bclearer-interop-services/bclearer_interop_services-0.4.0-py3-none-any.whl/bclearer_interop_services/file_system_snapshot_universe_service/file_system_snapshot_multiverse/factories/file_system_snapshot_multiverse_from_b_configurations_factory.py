from nf_common_base.b_source.common.configurations.b_configurations.b_configurations import (
    BConfigurations,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshot_multiverse.processors.file_system_snapshot_multiverse_initialiser import (
    initialise_file_system_snapshot_multiverse,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshot_multiverse.verses.null_file_system_snapshot_multiverses import (
    NullFileSystemSnapshotMultiverses,
)


# TODO: create length variable and check via case match - extract out as a factory within a factories folder
def create_file_system_snapshot_multiverse_from_b_configurations():
    input_root_file_system_objects_count = len(
        BConfigurations.INPUT_ROOT_FILE_SYSTEM_OBJECTS
    )

    if (
        input_root_file_system_objects_count
        > 1
    ):
        file_system_snapshot_multiverse = (
            initialise_file_system_snapshot_multiverse()
        )

    elif (
        input_root_file_system_objects_count
        == 1
    ):
        file_system_snapshot_multiverse = (
            NullFileSystemSnapshotMultiverses()
        )

    # TODO: find a better exception
    else:
        raise FileExistsError

    return (
        file_system_snapshot_multiverse
    )
