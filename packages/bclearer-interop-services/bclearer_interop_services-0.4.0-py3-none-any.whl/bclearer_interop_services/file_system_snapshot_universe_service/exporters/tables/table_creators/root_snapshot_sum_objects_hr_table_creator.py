import pathlib

from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.datastructure.column_names.snapshot_sum_objects_column_names import (
    SnapshotSumObjectsColumnNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.datastructure.column_names.snapshots_column_names import (
    SnapshotsColumnNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_creators.helpers.app_run_sessions_bie_id_adder import (
    add_app_run_sessions_bie_id,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.bie_column_names import (
    BieColumnNames,
)
from pandas import DataFrame


def create_root_snapshot_sum_objects_hr_table(
    snapshots_table: DataFrame,
    snapshot_sum_objects_hr_table: DataFrame,
    app_run_sessions: DataFrame,
) -> DataFrame:
    root_snapshot_table = snapshots_table[
        snapshots_table[
            SnapshotsColumnNames.ROOT_RELATIVE_PATH_NAMES.b_enum_item_name
        ]
        == str(pathlib.Path(str()))
    ]

    root_snapshot_bie_id = root_snapshot_table[
        BieColumnNames.BIE_IDS.b_enum_item_name
    ].iloc[
        0
    ]

    root_snapshot_sum_objects_hr_table = snapshot_sum_objects_hr_table[
        snapshot_sum_objects_hr_table[
            SnapshotSumObjectsColumnNames.OWNING_BIE_SNAPSHOT_IDS.b_enum_item_name
        ]
        == root_snapshot_bie_id
    ]

    root_snapshot_sum_objects_hr_table = add_app_run_sessions_bie_id(
        input_table=root_snapshot_sum_objects_hr_table,
        app_run_sessions=app_run_sessions,
    )

    return root_snapshot_sum_objects_hr_table
