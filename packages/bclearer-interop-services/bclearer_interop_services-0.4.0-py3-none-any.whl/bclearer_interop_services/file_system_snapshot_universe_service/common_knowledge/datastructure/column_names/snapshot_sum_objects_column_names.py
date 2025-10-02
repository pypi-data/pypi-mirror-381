from enum import auto

from nf_common_base.b_source.common.configurations.datastructure.b_enums import (
    BEnums,
)


class SnapshotSumObjectsColumnNames(
    BEnums
):
    NOT_SET = auto()

    DIRECTION_TYPE_IDS = auto()

    DIRECTION_TYPE_BIE_NAMES = auto()

    INCLUSIVITY_TYPE_IDS = auto()

    INCLUSIVITY_TYPE_BIE_NAMES = auto()

    SUMMED_BIE_OBJECT_TYPE_IDS = auto()

    OWNING_BIE_SNAPSHOT_IDS = auto()

    SUM_OBJECT_BIE_ID_INT_VALUES = (
        auto()
    )

    SUMMED_OBJECT_TYPE_BIE_NAMES = (
        auto()
    )
