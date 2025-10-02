from nf_common_base.b_source.common.bie.infrastructure.types.bie_common_column_names import (
    BieCommonColumnNames,
)
from nf_common_base.b_source.services.dataframe_service.dataframe_mergers import (
    inner_merge_dataframes,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.datastructure.column_names.snapshot_sum_objects_column_names import (
    SnapshotSumObjectsColumnNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.datastructure.column_names.snapshots_column_names import (
    SnapshotsColumnNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_creators.helpers.table_with_bie_objects_register_table_inner_joiner import (
    merge_table_with_bie_objects_register,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.bie_column_names import (
    BieColumnNames,
)
from pandas import DataFrame


def merge_snapshots_table_with_sum_objects_table(
    snapshots: DataFrame,
    snapshot_sum_objects: DataFrame,
    bie_objects_register_table: DataFrame,
) -> DataFrame:
    del snapshot_sum_objects[
        BieCommonColumnNames.BASE_HR_NAMES.b_enum_item_name
    ]

    columns_to_rename_as_dictionary = {
        BieCommonColumnNames.BIE_DOMAIN_TYPE_IDS.b_enum_item_name: BieCommonColumnNames.BIE_SNAPSHOT_TYPE_IDS.b_enum_item_name
    }

    renamed_snapshots = snapshots.rename(
        columns=columns_to_rename_as_dictionary
    )

    column_filtered_snapshots = renamed_snapshots[
        [
            BieColumnNames.BIE_IDS.b_enum_item_name,
            BieCommonColumnNames.BASE_HR_NAMES.b_enum_item_name,
            SnapshotsColumnNames.ROOT_RELATIVE_PATH_NAMES.b_enum_item_name,
            BieCommonColumnNames.BIE_SNAPSHOT_TYPE_IDS.b_enum_item_name,
        ]
    ]

    snapshots_column_rename_dictionary = {
        BieCommonColumnNames.BASE_HR_NAMES.b_enum_item_name: BieCommonColumnNames.BASE_HR_NAMES.b_enum_item_name,
        SnapshotsColumnNames.ROOT_RELATIVE_PATH_NAMES.b_enum_item_name: SnapshotsColumnNames.ROOT_RELATIVE_PATH_NAMES.b_enum_item_name,
        BieCommonColumnNames.BIE_SNAPSHOT_TYPE_IDS.b_enum_item_name: BieCommonColumnNames.BIE_SNAPSHOT_TYPE_IDS.b_enum_item_name,
    }

    merged = inner_merge_dataframes(
        master_dataframe=snapshot_sum_objects,
        master_dataframe_key_columns=[
            SnapshotSumObjectsColumnNames.OWNING_BIE_SNAPSHOT_IDS.b_enum_item_name
        ],
        merge_suffixes=[str()],
        foreign_key_dataframe=column_filtered_snapshots,
        foreign_key_dataframe_fk_columns=[
            BieColumnNames.BIE_IDS.b_enum_item_name
        ],
        foreign_key_dataframe_other_column_rename_dictionary=snapshots_column_rename_dictionary,
    )

    merged = merge_table_with_bie_objects_register(
        merged_dataframes_as_table=merged,
        register_as_table=bie_objects_register_table,
        left_key_name=BieCommonColumnNames.BIE_SNAPSHOT_TYPE_IDS.b_enum_item_name,
        new_column_name=BieCommonColumnNames.BIE_SNAPSHOT_TYPE_NAMES.b_enum_item_name,
    )

    merged.drop(
        [
            BieCommonColumnNames.BIE_SNAPSHOT_TYPE_IDS.b_enum_item_name
        ],
        axis=1,
        inplace=True,
    )

    return merged
