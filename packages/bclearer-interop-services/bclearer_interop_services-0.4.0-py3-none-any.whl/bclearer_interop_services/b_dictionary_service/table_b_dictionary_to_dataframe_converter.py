from nf_common_base.b_source.services.b_dictionary_service.objects.table_b_dictionaries import (
    TableBDictionaries,
)
from nf_common_base.b_source.services.table_as_dictionary_service.table_as_dictionary_to_dataframe_converter import (
    convert_table_as_dictionary_to_dataframe,
)
from pandas import DataFrame


def convert_table_b_dictionary_to_dataframe(
    table_b_dictionary: TableBDictionaries,
) -> DataFrame:
    table_as_dictionary = dict()

    for (
        row_b_dictionary_id_b_identity,
        row_b_dictionary,
    ) in (
        table_b_dictionary.dictionary.items()
    ):
        table_as_dictionary[
            row_b_dictionary_id_b_identity
        ] = row_b_dictionary.dictionary

    table_as_dataframe = convert_table_as_dictionary_to_dataframe(
        table_as_dictionary=table_as_dictionary
    )

    return table_as_dataframe
