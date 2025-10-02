from enum import auto

from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.bie_enums import (
    BieEnums,
)


# Note: do we want a ColumnNames between BieExtendedObjectsColumnNames
class BieUniverseColumnNames(BieEnums):
    NOT_SET = auto()

    BIE_ROOT_RELATIVE_PATH_IDS = auto()

    BIE_APP_RUN_SESSION_IDS = auto()
