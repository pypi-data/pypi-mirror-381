from nf_common_base.b_source.services.b_dictionary_service.objects.table_b_dictionaries import (
    TableBDictionaries,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.objects.bie_ids import (
    BieIds,
)


def convert_table_b_dictionary_to_networkx_node_attributes_list(
    table_b_dictionary: TableBDictionaries,
    node_ids_column_name: str,
) -> list:
    networkx_node_attributes_list = (
        list()
    )

    for (
        row_b_dictionary
    ) in (
        table_b_dictionary.dictionary.values()
    ):
        node_attributes_dictionary = (
            dict()
        )

        for (
            attribute_name,
            attribute_value,
        ) in (
            row_b_dictionary.dictionary.items()
        ):
            if isinstance(
                attribute_value, BieIds
            ):
                node_attributes_dictionary[
                    attribute_name
                ] = str(
                    attribute_value
                )

            else:
                node_attributes_dictionary[
                    attribute_name
                ] = attribute_value

        current_bie_id = (
            row_b_dictionary.dictionary[
                node_ids_column_name
            ]
        )

        current_node_id = str(
            current_bie_id
        )

        networkx_node_attributes_list.append(
            (
                current_node_id,
                node_attributes_dictionary,
            )
        )

    return networkx_node_attributes_list
