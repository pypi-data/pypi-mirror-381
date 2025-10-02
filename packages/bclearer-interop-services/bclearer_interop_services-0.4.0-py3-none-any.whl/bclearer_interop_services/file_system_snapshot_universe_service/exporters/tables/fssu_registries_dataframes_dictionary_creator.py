from nf_common_base.b_source.common.infrastructure.session.dataframes_dictionary.session_dataframes_dictionary_creator import (
    create_session_dataframes_dictionary,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_collection_creators.fssu_hr_dataframes_dictionary_creator import (
    create_fssu_hr_dataframes_dictionary,
)


# TODO: Should we add all of these (or specific ones) dataframes to the registry, the same way it's being done for the
#  parallel_bie_universe? the root signatures/sums hr tables would be useful when adding the snapshot universes to the
#  multiverse - need to discuss with team
def create_fssu_registries_dataframes_dictionary(
    file_system_snapshot_universe_registry,
) -> dict:
    session_dataframes_dictionary = create_session_dataframes_dictionary(
        app_run_session_object=file_system_snapshot_universe_registry.owning_universe.app_run_session_object
    )

    from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_collection_creators.fssu_registry_dataframes_dictionary_creator import (
        create_fssu_registry_dataframes_dictionary,
    )

    fssu_registry_dataframes_dictionary = create_fssu_registry_dataframes_dictionary(
        file_system_snapshot_universe_registry=file_system_snapshot_universe_registry
    )

    from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_collection_creators.parallel_bie_dataframes_dictionary_creator import (
        create_parallel_bie_dataframes_dictionary,
    )

    bie_dataframes_dictionary = create_parallel_bie_dataframes_dictionary(
        file_system_snapshot_universe_registry=file_system_snapshot_universe_registry
    )

    fssu_hr_dataframes_dictionary = create_fssu_hr_dataframes_dictionary(
        session_dataframes_dictionary=session_dataframes_dictionary,
        fssu_registry_dataframes_dictionary=fssu_registry_dataframes_dictionary,
        bie_dataframes_dictionary=bie_dataframes_dictionary,
    )

    export_register_as_dictionary = {
        **session_dataframes_dictionary,
        **fssu_registry_dataframes_dictionary,
        **bie_dataframes_dictionary,
        **fssu_hr_dataframes_dictionary,
    }

    export_register_as_dictionary_without_raw_objects = __exclude_raw_object_columns(
        export_register_as_dictionary=export_register_as_dictionary
    )

    return export_register_as_dictionary_without_raw_objects


def __exclude_raw_object_columns(
    export_register_as_dictionary: dict,
) -> dict:
    export_register_as_dictionary_without_raw_objects = (
        {}
    )

    for (
        table_name,
        table,
    ) in (
        export_register_as_dictionary.items()
    ):
        cleaned_table = table.loc[
            :,
            ~table.columns.str.startswith(
                "_raw_"
            ),
        ]

        export_register_as_dictionary_without_raw_objects[
            table_name
        ] = cleaned_table

    return export_register_as_dictionary_without_raw_objects
