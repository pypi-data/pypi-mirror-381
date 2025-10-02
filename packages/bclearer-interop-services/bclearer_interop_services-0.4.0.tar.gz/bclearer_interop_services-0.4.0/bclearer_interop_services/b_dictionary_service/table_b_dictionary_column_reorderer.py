from nf_common_base.b_source.services.b_dictionary_service.objects.row_b_dictionaries import (
    RowBDictionaries,
)
from nf_common_base.b_source.services.b_dictionary_service.objects.table_b_dictionaries import (
    TableBDictionaries,
)


def reorder_table_b_dictionary_columns(
    table_b_dictionary: TableBDictionaries,
    column_names_in_order: list,
) -> None:
    for (
        row_b_dictionary_id_b_identity,
        row_b_dictionary,
    ) in (
        table_b_dictionary.dictionary.items()
    ):
        __reorder_table_b_dictionary_row_by_column(
            row_b_dictionary=row_b_dictionary,
            column_names_in_order=column_names_in_order,
        )


def __reorder_table_b_dictionary_row_by_column(
    row_b_dictionary: RowBDictionaries,
    column_names_in_order: list,
) -> None:
    reordered_row_dictionary = {
        column_name: row_b_dictionary.dictionary[
            column_name
        ]
        for column_name in column_names_in_order
    }

    row_b_dictionary.dictionary = (
        reordered_row_dictionary
    )
