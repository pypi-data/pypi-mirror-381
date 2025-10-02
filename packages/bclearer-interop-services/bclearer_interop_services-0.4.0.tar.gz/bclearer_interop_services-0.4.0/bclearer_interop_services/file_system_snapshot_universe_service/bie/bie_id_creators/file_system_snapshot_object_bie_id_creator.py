from nf_common_base.b_source.common.infrastructure.session.app_run_session.app_run_session_objects import (
    AppRunSessionObjects,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.bie_file_system_snapshot_domain_types import (
    BieFileSystemSnapshotDomainTypes,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.file_system_snapshot_app_run_session_types import (
    FileSystemSnapshotAppRunSessionTypes,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.bie_id_creation_module.bie_id_creation_facade import (
    BieIdCreationFacade,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.objects.bie_ids import (
    BieIds,
)


def create_file_system_snapshot_object_bie_id(
    base_system_object_bie_id: BieIds,
) -> BieIds:
    # TODO: this needs to be passed in. It should be the AppRunSessionObjects of the run.
    app_run_session_object = AppRunSessionObjects(
        bie_app_run_session_type=FileSystemSnapshotAppRunSessionTypes.FILE_SYSTEM_SNAPSHOT_APP_RUN_SESSION
    )

    input_objects = [
        BieFileSystemSnapshotDomainTypes.BIE_FILE_SYSTEM_SNAPSHOT_BASE_SNAPSHOT_BIE_IDS.item_bie_identity,
        app_run_session_object.bie_id,
        base_system_object_bie_id,
    ]

    file_system_snapshot_object_base_snapshot_object_bie_id = BieIdCreationFacade.create_order_sensitive_bie_id_for_multiple_objects(
        input_objects=input_objects
    )

    return file_system_snapshot_object_base_snapshot_object_bie_id
