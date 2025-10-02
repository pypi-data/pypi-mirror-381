from nf_common_base.b_source.services.b_dictionary_service.objects.table_b_dictionaries import (
    TableBDictionaries,
)


def add_column_with_constant_value_to_table_b_dictionary(
    table_b_dictionary: TableBDictionaries,
    new_column_name: str,
    new_column_value,
) -> None:
    for (
        row_b_dictionary
    ) in (
        table_b_dictionary.dictionary.values()
    ):
        row_b_dictionary.dictionary.update(
            {
                new_column_name: new_column_value
            }
        )
