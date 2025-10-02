from enum import auto

from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.bie_domain_types import (
    BieDomainTypes,
)


# TODO: split into separate snapshot_universe_service
class BieFileSystemSnapshotDomainTypes(
    BieDomainTypes
):
    NOT_SET = auto()

    BIE_FILE_SYSTEM_SNAPSHOT_FOLDERS = (
        auto()
    )

    BIE_FILE_SYSTEM_SNAPSHOT_FILES = (
        auto()
    )

    BIE_FILE_SYSTEM_SNAPSHOT_BASE_SYSTEM_BIE_IDS = (
        auto()
    )

    BIE_FILE_SYSTEM_SNAPSHOT_BASE_SNAPSHOT_BIE_IDS = (
        auto()
    )

    BIE_RELATIVE_PATHS = auto()

    BIE_FILE_REFERENCE_NUMBERS = auto()

    BIE_INDIVIDUAL_FILE_SYSTEM_SNAPSHOT_OBJECTS = (
        auto()
    )

    BIE_INDIVIDUAL_FILE_SYSTEM_SNAPSHOT_FOLDERS = (
        auto()
    )

    BIE_INDIVIDUAL_FILE_SYSTEM_SNAPSHOT_FILES = (
        auto()
    )

    # TODO: move up to snapshots
    BIE_INDIVIDUAL_RUN_SNAPSHOTS = (
        auto()
    )

    BIE_RUN_SNAPSHOT_FUSIONS = auto()

    BIE_OBJECT_CONTENTS = auto()

    BIE_FILE_BYTE_CONTENTS = auto()

    SUM_OBJECTS = auto()

    ANCESTORS = auto()

    DESCENDENTS = auto()

    INCLUSIVE = auto()

    EXCLUSIVE = auto()
