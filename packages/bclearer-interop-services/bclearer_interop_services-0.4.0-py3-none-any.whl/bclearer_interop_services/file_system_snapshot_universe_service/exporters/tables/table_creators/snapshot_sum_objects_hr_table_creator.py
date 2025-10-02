import pandas
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.datastructure.column_names.snapshot_sum_objects_column_names import (
    SnapshotSumObjectsColumnNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_creators.helpers.snapshots_table_with_sum_objects_table_merger import (
    merge_snapshots_table_with_sum_objects_table,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_creators.helpers.table_with_bie_objects_register_table_inner_joiner import (
    merge_table_with_bie_objects_register,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.bie_column_names import (
    BieColumnNames,
)
from pandas import DataFrame


def create_snapshot_sum_objects_hr_table(
    snapshots_table: DataFrame,
    bie_objects_register_table: DataFrame,
    snapshot_sum_objects_table: DataFrame,
) -> pandas.DataFrame:
    merged_snapshots = merge_snapshots_table_with_sum_objects_table(
        snapshots_table,
        snapshot_sum_objects_table,
        bie_objects_register_table,
    )

    first_join_snapshot_to_register = merge_table_with_bie_objects_register(
        merged_dataframes_as_table=merged_snapshots,
        register_as_table=bie_objects_register_table,
        left_key_name=SnapshotSumObjectsColumnNames.SUMMED_BIE_OBJECT_TYPE_IDS.b_enum_item_name,
        new_column_name=SnapshotSumObjectsColumnNames.SUMMED_OBJECT_TYPE_BIE_NAMES.b_enum_item_name,
    )

    second_join_snapshot_to_register = merge_table_with_bie_objects_register(
        merged_dataframes_as_table=first_join_snapshot_to_register,
        register_as_table=bie_objects_register_table,
        left_key_name=SnapshotSumObjectsColumnNames.DIRECTION_TYPE_IDS.b_enum_item_name,
        new_column_name=SnapshotSumObjectsColumnNames.DIRECTION_TYPE_BIE_NAMES.b_enum_item_name,
    )

    third_join_snapshot_to_register = merge_table_with_bie_objects_register(
        merged_dataframes_as_table=second_join_snapshot_to_register,
        register_as_table=bie_objects_register_table,
        left_key_name=SnapshotSumObjectsColumnNames.INCLUSIVITY_TYPE_IDS.b_enum_item_name,
        new_column_name=SnapshotSumObjectsColumnNames.INCLUSIVITY_TYPE_BIE_NAMES.b_enum_item_name,
    )

    snapshot_sum_objects_hr_table = __get_sorted_table_by_column(
        dataframe=third_join_snapshot_to_register,
        column_name=BieColumnNames.SUM_VALUE_BIE_IDS.b_enum_item_name,
    )

    return snapshot_sum_objects_hr_table


def __get_sorted_table_by_column(
    dataframe: DataFrame,
    column_name: str,
) -> DataFrame:
    sorted_dataframe = (
        dataframe.sort_values(
            by=column_name
        )
    )

    column_filtered_sorted_dataframe = (
        sorted_dataframe.copy()
    )

    column_filtered_sorted_dataframe[
        column_name
    ] = column_filtered_sorted_dataframe.pop(
        column_name
    )

    return (
        column_filtered_sorted_dataframe
    )
