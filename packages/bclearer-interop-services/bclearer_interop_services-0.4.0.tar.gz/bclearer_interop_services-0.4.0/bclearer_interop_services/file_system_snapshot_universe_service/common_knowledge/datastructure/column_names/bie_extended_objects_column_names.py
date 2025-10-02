from enum import auto

from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.bie_enums import (
    BieEnums,
)


# TODO: Note: do we want a ColumnNames between BieExtendedObjectsColumnNames
class BieExtendedObjectsColumnNames(
    BieEnums
):
    NOT_SET = auto()

    EXTENDED_OBJECT_TYPES = auto()

    OWNING_BIE_SNAPSHOT_IDS = auto()

    EXTENDED_OBJECT_BIE_ID_INT_VALUES = (
        auto()
    )

    OWNING_BIE_REGISTER_IDS = auto()
