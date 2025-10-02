from nf_common_base.b_source.services.b_dictionary_service.objects.row_b_dictionaries import (
    RowBDictionaries,
)
from nf_common_base.b_source.services.b_dictionary_service.objects.table_b_dictionaries import (
    TableBDictionaries,
)


def convert_table_b_dictionary_to_networkx_edges_dictionary(
    table_b_dictionary: TableBDictionaries,
    source_nodes_column_name: str,
    target_node_column_name: str,
    edge_attributes_column_names: list,
) -> dict:
    networkx_edges_dictionary = dict()

    for (
        row_b_dictionary_b_identity,
        row_b_dictionary,
    ) in (
        table_b_dictionary.dictionary.items()
    ):
        __add_edge_to_dictionary(
            networkx_edges_dictionary=networkx_edges_dictionary,
            row_b_dictionary=row_b_dictionary,
            source_nodes_column_name=source_nodes_column_name,
            target_node_column_name=target_node_column_name,
            edge_attributes_column_names=edge_attributes_column_names,
        )

    return networkx_edges_dictionary


def __add_edge_to_dictionary(
    networkx_edges_dictionary: dict,
    row_b_dictionary: RowBDictionaries,
    source_nodes_column_name: str,
    target_node_column_name: str,
    edge_attributes_column_names: list,
):
    edge_attributes_dictionary = dict()

    for (
        edge_attribute_column_name
    ) in edge_attributes_column_names:
        edge_attributes_dictionary[
            edge_attribute_column_name
        ] = row_b_dictionary.dictionary[
            edge_attribute_column_name
        ]

    target_bie_id = (
        row_b_dictionary.dictionary[
            target_node_column_name
        ]
    )

    target_node_id = str(target_bie_id)

    target_node_dictionary = {
        target_node_id: edge_attributes_dictionary
    }

    source_bie_id = (
        row_b_dictionary.dictionary[
            source_nodes_column_name
        ]
    )

    source_node_id = str(source_bie_id)

    if (
        source_bie_id
        in networkx_edges_dictionary.keys()
    ):
        existent_target_node_dictionary = networkx_edges_dictionary[
            source_node_id
        ]

        target_node_dictionary.update(
            existent_target_node_dictionary
        )

    networkx_edges_dictionary[
        source_node_id
    ] = target_node_dictionary
