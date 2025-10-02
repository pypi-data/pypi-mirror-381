from nf_common_base.b_source.services.file_system_service.objects.file_system_objects import (
    FileSystemObjects,
)
from nf_common_base.b_source.services.file_system_service.objects.folders import (
    Folders,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.extended.root_relative_paths import (
    RootRelativePaths,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.snapshots.individual_file_system_snapshot_folders import (
    IndividualFileSystemSnapshotFolders,
)


# TODO: DZa to ask - should not this be a IndividualFileSystemSnapshotObjects return type?
#  are the compressed files process as a Folder or a different container type?
def create_root_relative_path(
    file_system_object: FileSystemObjects,
) -> RootRelativePaths:
    root_relative_path = (
        RootRelativePaths()
    )

    if isinstance(
        file_system_object, Folders
    ):
        root_snapshot = IndividualFileSystemSnapshotFolders(
            folder=file_system_object,
            relative_path=root_relative_path,
        )

    # TODO: add compressed containers
    else:
        raise TypeError

    return root_relative_path
