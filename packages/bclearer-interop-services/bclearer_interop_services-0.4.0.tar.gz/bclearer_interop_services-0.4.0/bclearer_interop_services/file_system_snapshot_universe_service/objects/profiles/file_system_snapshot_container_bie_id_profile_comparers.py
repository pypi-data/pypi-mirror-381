from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.bie_file_system_snapshot_domain_types import (
    BieFileSystemSnapshotDomainTypes,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.profiles.file_system_snapshot_container_bie_id_profiles import (
    FileSystemSnapshotContainerBieIdProfiles,
)


# TODO: To be promoted to universe
# TODO: rename "measurer? difference report? differemnt instrument"
class FileSystemSnapshotContainerBieIdProfileComparers:
    def __init__(
        self,
        first_profile: FileSystemSnapshotContainerBieIdProfiles,
        second_profile: FileSystemSnapshotContainerBieIdProfiles,
    ):
        self.is_container_bie_id_equal = (
            first_profile.root_relative_path_snapshot_bie_id
            == second_profile.root_relative_path_snapshot_bie_id
        )

        self.is_container_file_reference_number_bie_id_equal = (
            first_profile.root_file_reference_number_bie_id
            == second_profile.root_file_reference_number_bie_id
        )

        self.is_container_content_bie_id_equal = (
            first_profile.root_content_bie_id
            == second_profile.root_content_bie_id
        )

        self.is_container_relative_path_bie_id_equal = (
            first_profile.root_relative_path_bie_id
            == second_profile.root_relative_path_bie_id
        )

        first_profile_signature_dictionary = (
            first_profile.root_bie_signature_registry.file_system_snapshot_object_bie_id_signatures
        )

        second_profile_signature_dictionary = (
            second_profile.root_bie_signature_registry.file_system_snapshot_object_bie_id_signatures
        )

        self.is_container_signature_sum_file_reference_number_equal = (
            first_profile_signature_dictionary[
                BieFileSystemSnapshotDomainTypes.BIE_FILE_REFERENCE_NUMBERS
            ].signature_sum_bie_id
            == second_profile_signature_dictionary[
                BieFileSystemSnapshotDomainTypes.BIE_FILE_REFERENCE_NUMBERS
            ].signature_sum_bie_id
        )

        self.is_container_signature_sum_relative_path_equal = (
            first_profile_signature_dictionary[
                BieFileSystemSnapshotDomainTypes.BIE_RELATIVE_PATHS
            ].signature_sum_bie_id
            == second_profile_signature_dictionary[
                BieFileSystemSnapshotDomainTypes.BIE_RELATIVE_PATHS
            ].signature_sum_bie_id
        )

        self.is_container_signature_sum_content_equal = (
            first_profile_signature_dictionary[
                BieFileSystemSnapshotDomainTypes.BIE_FILE_BYTE_CONTENTS
            ].signature_sum_bie_id
            == second_profile_signature_dictionary[
                BieFileSystemSnapshotDomainTypes.BIE_FILE_BYTE_CONTENTS
            ].signature_sum_bie_id
        )
