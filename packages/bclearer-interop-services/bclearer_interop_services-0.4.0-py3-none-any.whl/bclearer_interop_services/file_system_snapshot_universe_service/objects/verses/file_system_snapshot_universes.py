from nf_common_base.b_source.common.constants.standard_constants import (
    HR_DATE_TIME_FORMAT,
    HR_NAME_COMPONENT_DIVIDER,
)
from nf_common_base.b_source.common.infrastructure.nf.objects.verses.nf_universes import (
    NfUniverses,
)
from nf_common_base.b_source.common.infrastructure.session.app_run_session.app_run_session_objects import (
    AppRunSessionObjects,
)
from nf_common_base.b_source.services.file_system_service.objects.file_system_objects import (
    FileSystemObjects,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.bie.bie_file_system_snapshot_universes import (
    BieFileSystemSnapshotUniverses,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.file_system_snapshot_app_run_session_types import (
    FileSystemSnapshotAppRunSessionTypes,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.file_system_snapshot_universe_types import (
    FileSystemSnapshotUniverseTypes,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.verses.file_system_snapshot_universe_registries import (
    FileSystemSnapshotUniverseRegistries,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.bie_id_creation_module.bie_id_creation_facade import (
    BieIdCreationFacade,
)


class FileSystemSnapshotUniverses(
    NfUniverses
):
    def __init__(
        self,
        parallel_bie_universe: BieFileSystemSnapshotUniverses,
        root_file_system_object: FileSystemObjects,
    ):
        super().__init__()

        self.file_system_snapshot_universe_registry = FileSystemSnapshotUniverseRegistries(
            owning_file_system_snapshot_universe=self,
            root_file_system_object=root_file_system_object,
        )

        # TODO: unused code for FSSO tests (use cases and export) - to be implemented
        self.parallel_bie_universe = (
            parallel_bie_universe
        )

        self.app_run_session_object = AppRunSessionObjects(
            bie_app_run_session_type=FileSystemSnapshotAppRunSessionTypes.FILE_SYSTEM_SNAPSHOT_APP_RUN_SESSION
        )

        self.bie_id = BieIdCreationFacade.create_order_sensitive_bie_id_for_multiple_objects(
            input_objects=[
                FileSystemSnapshotUniverseTypes.FILE_SYSTEM_SNAPSHOT_UNIVERSE.item_bie_identity,
                self.app_run_session_object.bie_id,
            ]
        )

        self.base_hr_name = (
            FileSystemSnapshotUniverseTypes.FILE_SYSTEM_SNAPSHOT_UNIVERSE.b_enum_item_name
            + HR_NAME_COMPONENT_DIVIDER
            + self.app_run_session_object.app_run_session_date_time.strftime(
                format=HR_DATE_TIME_FORMAT
            )
        )
