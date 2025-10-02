from nf_common_base.b_source.services.b_dictionary_service.objects.row_b_dictionaries import (
    RowBDictionaries,
)
from nf_common_base.b_source.services.b_dictionary_service.objects.table_b_dictionaries import (
    TableBDictionaries,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.bie_id_creation_module.bie_id_creation_facade import (
    BieIdCreationFacade,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.objects.bie_ids import (
    BieIds,
)
from pandas import DataFrame


def convert_dataframe_to_table_b_dictionary(
    dataframe: DataFrame,
    table_name: str,
    bie_table_id: BieIds,
) -> TableBDictionaries:
    table_as_dictionary = (
        dataframe.fillna(str())
        .transpose()
        .to_dict()
    )

    table_b_dictionary = (
        TableBDictionaries(
            table_name=table_name,
            bie_table_id=bie_table_id,
        )
    )

    for (
        key,
        dictionary,
    ) in table_as_dictionary.items():
        row_b_dictionary = (
            RowBDictionaries(
                dictionary=dictionary
            )
        )

        bie_row_id = BieIdCreationFacade.create_order_sensitive_bie_id_for_multiple_objects(
            input_objects=[
                table_b_dictionary.table_name,
                str(key),
            ]
        )

        table_b_dictionary.add_new_row_b_dictionary(
            bie_row_id=bie_row_id,
            row_b_dictionary=row_b_dictionary,
        )

    return table_b_dictionary
