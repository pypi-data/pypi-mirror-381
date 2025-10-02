from nf_common_base.b_source.services.b_dictionary_service.objects.row_b_dictionaries import (
    RowBDictionaries,
)
from nf_common_base.b_source.services.b_dictionary_service.objects.table_b_dictionaries import (
    TableBDictionaries,
)


def rename_table_b_dictionary_columns(
    table_b_dictionary: TableBDictionaries,
    column_renaming_dictionary: dict,
) -> None:
    for (
        row_b_dictionary_id_b_identity,
        row_b_dictionary,
    ) in (
        table_b_dictionary.dictionary.items()
    ):
        __rename_row_b_dictionary_columns(
            row_b_dictionary=row_b_dictionary,
            column_renaming_dictionary=column_renaming_dictionary,
        )


def __rename_row_b_dictionary_columns(
    row_b_dictionary: RowBDictionaries,
    column_renaming_dictionary: dict,
) -> None:
    renamed_row_b_dictionary_dictionary = (
        dict()
    )

    for (
        old_column_name,
        column_value,
    ) in (
        row_b_dictionary.dictionary.items()
    ):
        __rename_row_b_dictionary_column(
            column_renaming_dictionary=column_renaming_dictionary,
            old_column_name=old_column_name,
            column_value=column_value,
            renamed_row_b_dictionary_dictionary=renamed_row_b_dictionary_dictionary,
        )

    row_b_dictionary.dictionary = renamed_row_b_dictionary_dictionary


def __rename_row_b_dictionary_column(
    column_renaming_dictionary: dict,
    old_column_name: str,
    column_value,
    renamed_row_b_dictionary_dictionary: dict,
) -> None:
    new_column_name = old_column_name

    if (
        old_column_name
        in column_renaming_dictionary.keys()
    ):
        new_column_name = (
            column_renaming_dictionary[
                old_column_name
            ]
        )

    renamed_row_b_dictionary_dictionary[
        new_column_name
    ] = column_value
