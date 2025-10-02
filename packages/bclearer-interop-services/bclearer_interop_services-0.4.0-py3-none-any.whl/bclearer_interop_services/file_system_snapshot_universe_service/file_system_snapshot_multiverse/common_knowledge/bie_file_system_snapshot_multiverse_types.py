from enum import auto

from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.bie_infrastructure_types import (
    BieInfrastructureTypes,
)


# TODO: should this be a new object? maybe reuse?
class FileSystemSnapshotMultiverseTypes(
    BieInfrastructureTypes
):
    NOT_SET = auto()

    FILE_SYSTEM_SNAPSHOT_MULTIVERSE = (
        auto()
    )
