from nf_common_base.b_source.services.dataframe_service.dataframe_mergers import (
    inner_merge_dataframes,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.bie_column_names import (
    BieColumnNames,
)
from pandas import DataFrame


def merge_table_with_bie_objects_register(
    merged_dataframes_as_table: DataFrame,
    register_as_table: DataFrame,
    left_key_name: str,
    new_column_name: str,
) -> DataFrame:
    column_filtered_register = register_as_table[
        [
            BieColumnNames.BIE_IDS.b_enum_item_name,
            BieColumnNames.BIE_NAMES.b_enum_item_name,
        ]
    ]

    register_column_rename_dictionary = {
        BieColumnNames.BIE_NAMES.b_enum_item_name: new_column_name
    }

    merged_dataframes_as_table = inner_merge_dataframes(
        master_dataframe=merged_dataframes_as_table,
        master_dataframe_key_columns=[
            left_key_name
        ],
        merge_suffixes=[str()],
        foreign_key_dataframe=column_filtered_register,
        foreign_key_dataframe_fk_columns=[
            BieColumnNames.BIE_IDS.b_enum_item_name
        ],
        foreign_key_dataframe_other_column_rename_dictionary=register_column_rename_dictionary,
    )

    return merged_dataframes_as_table
