from nf_common_base.b_source.services.file_system_service.objects.file_system_objects import (
    FileSystemObjects,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.bie.bie_id_creators.file_reference_number_extended_object_bie_id_creator import (
    create_file_reference_number_extended_object_bie_id,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.bie_file_system_snapshot_domain_types import (
    BieFileSystemSnapshotDomainTypes,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.os_functions.windows.file_reference_number_getter import (
    get_file_reference_number,
)
from nf_common_base.b_source.services.snapshot_universe_service.objects.extended_objects import (
    ExtendedObjects,
)


class FileReferenceNumbers(
    ExtendedObjects
):
    def __init__(
        self,
        file_system_object: FileSystemObjects,
    ):
        self.file_reference_number = get_file_reference_number(
            file_path_as_string=file_system_object.absolute_path_string
        )

        bie_id = create_file_reference_number_extended_object_bie_id(
            file_system_object=file_system_object,
            file_reference_number=self.file_reference_number,
        )

        super().__init__(
            bie_id=bie_id,
            base_hr_name=self.file_reference_number,
            bie_domain_type=BieFileSystemSnapshotDomainTypes.BIE_FILE_REFERENCE_NUMBERS,
        )
