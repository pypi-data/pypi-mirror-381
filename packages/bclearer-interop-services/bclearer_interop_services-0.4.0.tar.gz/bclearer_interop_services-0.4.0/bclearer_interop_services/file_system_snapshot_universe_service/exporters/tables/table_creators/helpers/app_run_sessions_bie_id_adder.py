from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.bie_column_names import (
    BieColumnNames,
)
from pandas import DataFrame


def add_app_run_sessions_bie_id(
    input_table: DataFrame,
    app_run_sessions: DataFrame,
) -> DataFrame:
    if len(app_run_sessions) != 1:
        raise ValueError(
            "app_run_sessions table contains more than one row"
        )

    app_run_session_bie_id = app_run_sessions[
        BieColumnNames.BIE_IDS.b_enum_item_name
    ].iloc[
        0
    ]

    # TODO: Replace dataframe column assignment with the recommended pandas practice to get rid of the warning - DONE
    updated_input_table = (
        input_table.copy(deep=True)
    )

    updated_input_table[
        "owning_bie_ app_run_session_id"
    ] = app_run_session_bie_id

    return updated_input_table
