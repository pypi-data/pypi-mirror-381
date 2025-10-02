from enum import auto

from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.bie_enums import (
    BieEnums,
)


class FileSystemSnapshotUniverseRegistryTableNames(
    BieEnums
):
    NOT_SET = auto()

    # TODO: to check
    SNAPSHOTS_HR_ORIGINAL = auto()

    SNAPSHOTS_HR = auto()

    SNAPSHOTS = auto()

    EXTENDED_OBJECTS = auto()

    SNAPSHOT_WHOLES_PARTS_BREAKDOWN = (
        auto()
    )

    SNAPSHOT_DOMAIN_UNIVERSES = auto()

    # TODO: Moved to the common SessionObjectColumnNames. Should it be deleted from here?
    APP_RUN_SESSIONS = auto()

    SNAPSHOT_SUM_OBJECTS = auto()

    # TODO: to check
    ROOT_BIE_SIGNATURE_SUMS = auto()
