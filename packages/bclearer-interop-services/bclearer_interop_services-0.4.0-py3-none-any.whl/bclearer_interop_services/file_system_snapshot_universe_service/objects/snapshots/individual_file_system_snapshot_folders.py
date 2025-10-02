from nf_common_base.b_source.services.file_system_service.objects.folders import (
    Folders,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.bie_file_system_snapshot_domain_types import (
    BieFileSystemSnapshotDomainTypes,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.extended.relative_paths import (
    RelativePaths,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.snapshots.individual_file_system_snapshot_objects import (
    IndividualFileSystemSnapshotObjects,
)
from nf_common_base.b_source.services.snapshot_universe_service.objects.folder_file_byte_contents import (
    FolderFileByteContents,
)


class IndividualFileSystemSnapshotFolders(
    IndividualFileSystemSnapshotObjects
):
    def __init__(
        self,
        folder: Folders,
        relative_path: RelativePaths,
    ):
        file_byte_content = (
            FolderFileByteContents()
        )

        super().__init__(
            bie_domain_type=BieFileSystemSnapshotDomainTypes.BIE_INDIVIDUAL_FILE_SYSTEM_SNAPSHOT_FOLDERS,
            file_system_object=folder,
            relative_path=relative_path,
            object_content=file_byte_content,
        )
