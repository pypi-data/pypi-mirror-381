from nf_common_base.b_source.common.infrastructure.session.os_user_session.enums.session_object_column_names import (
    SessionObjectColumnNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.datastructure.table_names.file_system_snapshot_universe_registry_hr_table_names import (
    FileSystemSnapshotUniverseRegistryHrTableNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.datastructure.table_names.file_system_snapshot_universe_registry_table_names import (
    FileSystemSnapshotUniverseRegistryTableNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_creators.root_bie_signature_sums_hr_table_creator import (
    create_root_bie_signature_sums_hr_table,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_creators.root_snapshot_sum_objects_hr_table_creator import (
    create_root_snapshot_sum_objects_hr_table,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_creators.snapshot_sum_objects_hr_table_creator import (
    create_snapshot_sum_objects_hr_table,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.datastructure.bie_registries_registers_types import (
    BieRegistriesRegistersTypes,
)


def create_fssu_hr_dataframes_dictionary(
    session_dataframes_dictionary: dict,
    fssu_registry_dataframes_dictionary: dict,
    bie_dataframes_dictionary: dict,
) -> dict:
    dataframes_dictionary_keyed_on_string = (
        {}
    )

    root_bie_signature_sums_hr_table = create_root_bie_signature_sums_hr_table(
        root_bie_signature_sums_table=fssu_registry_dataframes_dictionary[
            FileSystemSnapshotUniverseRegistryTableNames.ROOT_BIE_SIGNATURE_SUMS.b_enum_item_name
        ],
        bie_objects_register_table=bie_dataframes_dictionary[
            BieRegistriesRegistersTypes.BIE_OBJECTS_REGISTER.b_enum_item_name
        ],
        app_run_sessions=session_dataframes_dictionary[
            SessionObjectColumnNames.APP_RUN_SESSIONS.b_enum_item_name
        ],
    )

    snapshot_sum_objects_hr_table = create_snapshot_sum_objects_hr_table(
        snapshots_table=fssu_registry_dataframes_dictionary[
            FileSystemSnapshotUniverseRegistryTableNames.SNAPSHOTS.b_enum_item_name
        ],
        bie_objects_register_table=bie_dataframes_dictionary[
            BieRegistriesRegistersTypes.BIE_OBJECTS_REGISTER.b_enum_item_name
        ],
        snapshot_sum_objects_table=fssu_registry_dataframes_dictionary[
            FileSystemSnapshotUniverseRegistryTableNames.SNAPSHOT_SUM_OBJECTS.b_enum_item_name
        ],
    )

    root_snapshot_sum_objects_hr_table = create_root_snapshot_sum_objects_hr_table(
        snapshots_table=fssu_registry_dataframes_dictionary[
            FileSystemSnapshotUniverseRegistryTableNames.SNAPSHOTS.b_enum_item_name
        ],
        snapshot_sum_objects_hr_table=snapshot_sum_objects_hr_table,
        app_run_sessions=session_dataframes_dictionary[
            SessionObjectColumnNames.APP_RUN_SESSIONS.b_enum_item_name
        ],
    )

    if (
        not root_bie_signature_sums_hr_table.empty
    ):
        dataframes_dictionary_keyed_on_string[
            FileSystemSnapshotUniverseRegistryHrTableNames.ROOT_BIE_SIGNATURE_SUMS_HR.b_enum_item_name
        ] = root_bie_signature_sums_hr_table

    if (
        not snapshot_sum_objects_hr_table.empty
    ):
        dataframes_dictionary_keyed_on_string[
            FileSystemSnapshotUniverseRegistryHrTableNames.SNAPSHOT_SUM_OBJECTS_HR.b_enum_item_name
        ] = snapshot_sum_objects_hr_table

    if (
        not root_snapshot_sum_objects_hr_table.empty
    ):
        dataframes_dictionary_keyed_on_string[
            FileSystemSnapshotUniverseRegistryHrTableNames.ROOT_SNAPSHOT_SUM_OBJECTS_HR.b_enum_item_name
        ] = root_snapshot_sum_objects_hr_table

    return dataframes_dictionary_keyed_on_string
