from nf_common_base.b_source.common.bie.infrastructure.types.bie_common_column_names import (
    BieCommonColumnNames,
)
from nf_common_base.b_source.services.dataframe_service.dataframe_mergers import (
    inner_merge_dataframes,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_creators.helpers.app_run_sessions_bie_id_adder import (
    add_app_run_sessions_bie_id,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.bie_column_names import (
    BieColumnNames,
)
from pandas import DataFrame


def create_root_bie_signature_sums_hr_table(
    root_bie_signature_sums_table: DataFrame,
    bie_objects_register_table: DataFrame,
    app_run_sessions: DataFrame,
) -> DataFrame:
    foreign_key_dataframe_other_column_rename_dictionary = {
        BieColumnNames.BIE_NAMES.b_enum_item_name: BieCommonColumnNames.BIE_DOMAIN_TYPE_NAMES.b_enum_item_name
    }

    root_bie_signature_sums_hr_table = inner_merge_dataframes(
        master_dataframe=root_bie_signature_sums_table,
        master_dataframe_key_columns=[
            BieCommonColumnNames.BIE_DOMAIN_TYPE_IDS.b_enum_item_name
        ],
        merge_suffixes=[str()],
        foreign_key_dataframe=bie_objects_register_table,
        foreign_key_dataframe_fk_columns=[
            BieColumnNames.BIE_IDS.b_enum_item_name
        ],
        foreign_key_dataframe_other_column_rename_dictionary=foreign_key_dataframe_other_column_rename_dictionary,
    )

    root_bie_signature_sums_hr_table = add_app_run_sessions_bie_id(
        input_table=root_bie_signature_sums_hr_table,
        app_run_sessions=app_run_sessions,
    )

    return (
        root_bie_signature_sums_hr_table
    )
