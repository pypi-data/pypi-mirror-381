from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.verses.file_system_snapshot_universe_registries import (
    FileSystemSnapshotUniverseRegistries,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.datastructure.bie_registries_registers_types import (
    BieRegistriesRegistersTypes,
)
from nf_common_base.b_source.services.table_as_dictionary_service.table_as_dictionary_to_dataframe_converter import (
    convert_table_as_dictionary_to_dataframe,
)


def create_parallel_bie_dataframes_dictionary(
    file_system_snapshot_universe_registry: FileSystemSnapshotUniverseRegistries,
) -> dict:
    bie_objects_register = file_system_snapshot_universe_registry.owning_universe.parallel_bie_universe.bie_infrastructure_registry.get_bie_register(
        bie_register_type_enum=BieRegistriesRegistersTypes.BIE_OBJECTS_REGISTER
    )

    bie_objects_dataframe = bie_objects_register.get_bie_register_dataframe().astype(
        str
    )

    bie_relations_rows = {}

    bie_relations_register = file_system_snapshot_universe_registry.owning_universe.parallel_bie_universe.bie_infrastructure_registry.get_bie_register(
        bie_register_type_enum=BieRegistriesRegistersTypes.BIE_RELATIONS_REGISTER
    )

    for (
        index,
        row,
    ) in (
        bie_relations_register.get_bie_register_dataframe().iterrows()
    ):
        if row["bie_place_2_ids"]:
            bie_relations_rows[
                index
            ] = {
                "bie_place_1_ids": row[
                    "bie_place_1_ids"
                ],
                "bie_place_2_ids": row[
                    "bie_place_2_ids"
                ],
                "bie_relation_type_ids": row[
                    "bie_relation_type_ids"
                ],
            }

    bie_relations_dataframe = convert_table_as_dictionary_to_dataframe(
        table_as_dictionary=bie_relations_rows
    ).astype(
        str
    )

    bie_dataframes_dictionary = {
        BieRegistriesRegistersTypes.BIE_OBJECTS_REGISTER.b_enum_item_name: bie_objects_dataframe,
        BieRegistriesRegistersTypes.BIE_RELATIONS_REGISTER.b_enum_item_name: bie_relations_dataframe,
    }

    return bie_dataframes_dictionary
