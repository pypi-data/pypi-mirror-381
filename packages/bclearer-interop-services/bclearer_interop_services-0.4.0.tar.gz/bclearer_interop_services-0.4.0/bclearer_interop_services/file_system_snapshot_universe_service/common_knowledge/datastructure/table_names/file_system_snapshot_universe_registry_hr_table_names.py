from enum import auto

from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.bie_enums import (
    BieEnums,
)


class FileSystemSnapshotUniverseRegistryHrTableNames(
    BieEnums
):
    NOT_SET = auto()

    ROOT_BIE_SIGNATURE_SUMS_HR = auto()

    SNAPSHOT_SUM_OBJECTS_HR = auto()

    ROOT_SNAPSHOT_SUM_OBJECTS_HR = (
        auto()
    )
