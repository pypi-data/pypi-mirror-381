from nf_common_base.b_source.services.file_system_service.objects.file_system_objects import (
    FileSystemObjects,
)
from nf_common_base.b_source.services.file_system_service.objects.path_properties import (
    PathProperties,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.bie.bie_id_creators.file_system_snapshot_object_bie_id_creator import (
    create_file_system_snapshot_object_bie_id,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.bie_file_system_snapshot_domain_types import (
    BieFileSystemSnapshotDomainTypes,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.extended.file_reference_numbers import (
    FileReferenceNumbers,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.extended.relative_paths import (
    RelativePaths,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.snapshots.file_system_snapshot_objects import (
    FileSystemSnapshotObjects,
)
from nf_common_base.b_source.services.snapshot_universe_service.objects.object_contents import (
    ObjectContents,
)


class IndividualFileSystemSnapshotObjects(
    FileSystemSnapshotObjects
):
    def __init__(
        self,
        bie_domain_type: BieFileSystemSnapshotDomainTypes,
        file_system_object: FileSystemObjects,
        relative_path: RelativePaths,
        object_content: ObjectContents,
    ):
        self._file_system_object = (
            file_system_object
        )

        file_reference_number = FileReferenceNumbers(
            file_system_object=self._file_system_object
        )

        bie_id = create_file_system_snapshot_object_bie_id(
            base_system_object_bie_id=file_reference_number.bie_id
        )

        if (
            file_system_object.absolute_path.exists()
        ):
            self.file_system_object_properties = PathProperties(
                input_file_system_object_path=file_system_object.absolute_path_string
            )

        super().__init__(
            bie_id=bie_id,
            base_hr_name=file_system_object.base_name,
            bie_domain_type=bie_domain_type,
            relative_path=relative_path,
            file_reference_number=file_reference_number,
            object_content=object_content,
        )

    def get_file_system_object(
        self,
    ) -> FileSystemObjects:
        return self._file_system_object
