from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.bie_file_system_snapshot_domain_types import (
    BieFileSystemSnapshotDomainTypes,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.extended.root_relative_paths import (
    RootRelativePaths,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.verses.root_relative_path_bie_signature_registries import (
    RootRelativePathBieSignatureRegistries,
)


# TODO: To be promoted to universe
class FileSystemSnapshotContainerBieIdProfiles:
    def __init__(
        self,
        root_relative_path: RootRelativePaths,
    ):
        root_relative_path_snapshot = (
            root_relative_path.snapshot
        )

        self.root_relative_path_snapshot_bie_id = (
            root_relative_path_snapshot.bie_id
        )

        self.root_bie_signature_registry = (
            RootRelativePathBieSignatureRegistries()
        )

        self.root_file_reference_number_bie_id = root_relative_path_snapshot.extended_objects[
            BieFileSystemSnapshotDomainTypes.BIE_FILE_REFERENCE_NUMBERS
        ].bie_id

        self.root_relative_path_bie_id = root_relative_path_snapshot.extended_objects[
            BieFileSystemSnapshotDomainTypes.BIE_RELATIVE_PATHS
        ].bie_id

        self.root_content_bie_id = root_relative_path_snapshot.extended_objects[
            BieFileSystemSnapshotDomainTypes.BIE_FILE_BYTE_CONTENTS
        ].bie_id

        # TODO: to deprecate
        self.is_root_content_bie_id_empty = (
            self.root_content_bie_id.is_empty
        )

        self.root_bie_relative_path_descendant_sum_bie_id = root_relative_path_snapshot.inclusive_descendant_sum_objects[
            BieFileSystemSnapshotDomainTypes.BIE_RELATIVE_PATHS
        ].bie_id

        self.root_bie_file_reference_number_descendant_sum_bie_id = root_relative_path_snapshot.inclusive_descendant_sum_objects[
            BieFileSystemSnapshotDomainTypes.BIE_FILE_REFERENCE_NUMBERS
        ].bie_id

        self.root_bie_file_byte_content_descendant_sum_bie_id = root_relative_path_snapshot.inclusive_descendant_sum_objects[
            BieFileSystemSnapshotDomainTypes.BIE_FILE_BYTE_CONTENTS
        ].bie_id

        self.root_bie_file_byte_content_signature_sum_bie_id = (
            None
        )

        self.root_bie_file_reference_number_signature_sum_bie_id = (
            None
        )

        self.root_bie_individual_file_system_snapshot_files_signature_sum_bie_id = (
            None
        )

        self.root_bie_individual_file_system_snapshot_folders_signature_sum_bie_id = (
            None
        )

        self.root_bie_relative_path_signature_sum_bie_id = (
            None
        )

        self.is_root_bie_relative_path_signature_sum_and_descendant_sum_bie_ids_equal = (
            None
        )

        self.is_root_bie_file_reference_number_signature_sum_and_descendant_sum_bie_ids_equal = (
            None
        )

        self.is_root_bie_file_byte_content_signature_sum_and_descendant_sum_bie_ids_equal = (
            None
        )

        self.are_root_bie_signature_sums_and_descendant_sums_bie_ids_all_equal = (
            None
        )

        self.is_root_bie_file_byte_content_signature_sum_bie_id_empty = (
            None
        )

    def populate_signature_comparisons(
        self,
    ):
        self.root_bie_file_byte_content_signature_sum_bie_id = self.root_bie_signature_registry.file_system_snapshot_object_bie_id_signatures[
            BieFileSystemSnapshotDomainTypes.BIE_FILE_BYTE_CONTENTS
        ].signature_sum_bie_id

        self.root_bie_file_reference_number_signature_sum_bie_id = self.root_bie_signature_registry.file_system_snapshot_object_bie_id_signatures[
            BieFileSystemSnapshotDomainTypes.BIE_FILE_REFERENCE_NUMBERS
        ].signature_sum_bie_id

        # TODO: double-check there is no risk for this to happen as well with the FOLDERS (there will always be one
        #  folder which is the container)
        if (
            BieFileSystemSnapshotDomainTypes.BIE_INDIVIDUAL_FILE_SYSTEM_SNAPSHOT_FILES
            in self.root_bie_signature_registry.file_system_snapshot_object_bie_id_signatures
        ):
            self.root_bie_individual_file_system_snapshot_files_signature_sum_bie_id = self.root_bie_signature_registry.file_system_snapshot_object_bie_id_signatures[
                BieFileSystemSnapshotDomainTypes.BIE_INDIVIDUAL_FILE_SYSTEM_SNAPSHOT_FILES
            ].signature_sum_bie_id

        self.root_bie_individual_file_system_snapshot_folders_signature_sum_bie_id = self.root_bie_signature_registry.file_system_snapshot_object_bie_id_signatures[
            BieFileSystemSnapshotDomainTypes.BIE_INDIVIDUAL_FILE_SYSTEM_SNAPSHOT_FOLDERS
        ].signature_sum_bie_id

        self.root_bie_relative_path_signature_sum_bie_id = self.root_bie_signature_registry.file_system_snapshot_object_bie_id_signatures[
            BieFileSystemSnapshotDomainTypes.BIE_RELATIVE_PATHS
        ].signature_sum_bie_id

        self.is_root_bie_file_byte_content_signature_sum_bie_id_empty = (
            self.root_bie_file_byte_content_signature_sum_bie_id.is_empty
        )

        self.is_root_bie_relative_path_signature_sum_and_descendant_sum_bie_ids_equal = (
            self.root_bie_relative_path_signature_sum_bie_id
            == self.root_bie_relative_path_descendant_sum_bie_id
        )

        self.is_root_bie_file_reference_number_signature_sum_and_descendant_sum_bie_ids_equal = (
            self.root_bie_file_reference_number_signature_sum_bie_id
            == self.root_bie_file_reference_number_descendant_sum_bie_id
        )

        self.is_root_bie_file_byte_content_signature_sum_and_descendant_sum_bie_ids_equal = (
            self.root_bie_file_byte_content_signature_sum_bie_id
            == self.root_bie_file_byte_content_descendant_sum_bie_id
        )

        self.are_root_bie_signature_sums_and_descendant_sums_bie_ids_all_equal = (
            self.is_root_bie_relative_path_signature_sum_and_descendant_sum_bie_ids_equal
            and self.is_root_bie_file_reference_number_signature_sum_and_descendant_sum_bie_ids_equal
            and self.is_root_bie_file_byte_content_signature_sum_and_descendant_sum_bie_ids_equal
        )

    def compare_with_me(
        self,
        other_file_system_snapshot_container_bie_id_profile: "FileSystemSnapshotContainerBieIdProfiles",
    ) -> "FileSystemSnapshotContainerBieIdProfileComparers":
        from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.profiles.file_system_snapshot_container_bie_id_profile_comparers import (
            FileSystemSnapshotContainerBieIdProfileComparers,
        )

        file_system_snapshot_container_bie_id_profile_comparer = FileSystemSnapshotContainerBieIdProfileComparers(
            first_profile=self,
            second_profile=other_file_system_snapshot_container_bie_id_profile,
        )

        return file_system_snapshot_container_bie_id_profile_comparer
