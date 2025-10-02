from enum import auto

from nf_common_base.b_source.common.configurations.datastructure.b_enums import (
    BEnums,
)


class SnapshotsColumnNames(BEnums):
    NOT_SET = auto()

    FILE_SYSTEM_SNAPSHOT_DOMAIN_TYPES = (
        auto()
    )

    STAGE_OF_RELATIVE_PATH_RELATIVE_PATHS = (
        auto()
    )

    RELATIVE_PATH_PARENTS = auto()

    FULL_NAME = auto()

    ROOT_RELATIVE_PATH_NAMES = auto()

    EXTENSION = auto()

    LENGTH = auto()

    CHILD_COUNT = auto()

    CREATION_TIME = auto()

    LAST_ACCESS_TIME = auto()

    LAST_WRITE_TIME = auto()

    CONTENT_BIE_ID_INT_VALUES = auto()

    DESCENDENT_SUM_CONTENT_BIE_ID_INT_VALUES = (
        auto()
    )

    ANCESTOR_SUM_CONTENT_BIE_ID_INT_VALUES = (
        auto()
    )
