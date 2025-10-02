from typing import Dict

from nf_common_base.b_source.common.infrastructure.nf.objects.registries.nf_multiverse_registries import (
    NfMultiverseRegistries,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.verses.file_system_snapshot_universes import (
    FileSystemSnapshotUniverses,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.objects.bie_ids import (
    BieIds,
)


class FileSystemSnapshotMultiverseRegistries(
    NfMultiverseRegistries
):
    def __init__(
        self,
        owning_file_system_snapshot_multiverse,
    ):
        super().__init__()

        from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshot_multiverse.verses.file_system_snapshot_multiverses import (
            FileSystemSnapshotMultiverses,
        )

        if not isinstance(
            owning_file_system_snapshot_multiverse,
            FileSystemSnapshotMultiverses,
        ):
            raise TypeError
        self.owning_multiverse = owning_file_system_snapshot_multiverse

        # TODO: Should register be of type ...Registers?
        self.file_system_snapshot_universes_register: Dict[
            BieIds,
            FileSystemSnapshotUniverses,
        ] = dict()

    # TODO: to be deprecated??
    def add_file_system_snapshot_universes_as_dictionary_to_registry(
        self,
        file_system_snapshot_universes_dictionary,
    ):
        self.file_system_snapshot_universes_register = file_system_snapshot_universes_dictionary

    def add_universe(
        self,
        file_system_snapshot_universe: FileSystemSnapshotUniverses,
    ):
        self.file_system_snapshot_universes_register[
            file_system_snapshot_universe.bie_id
        ] = file_system_snapshot_universe

    # TODO: added here as a placeholder for the HR queries - stage 2
    def export_multiverse_register_as_dictionary(
        self,
    ) -> dict:
        # TODO: to complete
        file_system_snapshot_multiverse_register_as_dictionary = (
            dict()
        )

        return file_system_snapshot_multiverse_register_as_dictionary
