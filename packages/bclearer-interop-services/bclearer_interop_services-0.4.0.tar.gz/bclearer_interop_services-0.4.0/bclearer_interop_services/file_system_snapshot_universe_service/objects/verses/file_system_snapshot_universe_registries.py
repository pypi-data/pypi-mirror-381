from nf_common_base.b_source.common.infrastructure.nf.objects.registries.nf_universe_registries import (
    NfUniverseRegistries,
)
from nf_common_base.b_source.services.file_system_service.objects.file_system_objects import (
    FileSystemObjects,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.fssu_registries_dataframes_dictionary_creator import (
    create_fssu_registries_dataframes_dictionary,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.profiles.file_system_snapshot_container_bie_id_profiles import (
    FileSystemSnapshotContainerBieIdProfiles,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.populators.bie_signatures.root_relative_path_bie_signatures_populator import (
    populate_root_relative_path_bie_signatures,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.populators.file_system_snapshot_objects.root_relative_path_populator import (
    populate_root_relative_path,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.populators.root_relative_path_creator import (
    create_root_relative_path,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.populators.sum_objects.snapshot_sum_objects_populator import (
    populate_snapshot_sum_objects,
)


class FileSystemSnapshotUniverseRegistries(
    NfUniverseRegistries
):
    def __init__(
        self,
        owning_file_system_snapshot_universe,
        root_file_system_object: FileSystemObjects,
    ):
        super().__init__()

        from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.verses.file_system_snapshot_universes import (
            FileSystemSnapshotUniverses,
        )

        if not isinstance(
            owning_file_system_snapshot_universe,
            FileSystemSnapshotUniverses,
        ):
            raise TypeError

        self.owning_universe = owning_file_system_snapshot_universe

        self.root_relative_path = create_root_relative_path(
            file_system_object=root_file_system_object
        )

        populate_root_relative_path(
            root_relative_path=self.root_relative_path
        )

        populate_snapshot_sum_objects(
            root_relative_path=self.root_relative_path
        )

        self.file_system_snapshot_container_bie_id_profile = FileSystemSnapshotContainerBieIdProfiles(
            root_relative_path=self.root_relative_path
        )

        populate_root_relative_path_bie_signatures(
            bie_signature_registry=self.file_system_snapshot_container_bie_id_profile.root_bie_signature_registry,
            root_relative_path=self.root_relative_path,
        )

        self.file_system_snapshot_container_bie_id_profile.populate_signature_comparisons()

    def export_register_as_dictionary(
        self,
    ) -> dict:
        # TODO: to be replaced
        export_register_as_dictionary = create_fssu_registries_dataframes_dictionary(
            file_system_snapshot_universe_registry=self
        )

        return export_register_as_dictionary
