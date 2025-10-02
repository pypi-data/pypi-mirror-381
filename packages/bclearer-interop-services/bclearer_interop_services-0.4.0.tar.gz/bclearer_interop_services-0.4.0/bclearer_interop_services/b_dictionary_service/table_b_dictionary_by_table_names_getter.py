from nf_common_base.b_source.services.b_dictionary_service.objects.table_registers import (
    TableRegisters,
)


def get_table_register_table_b_dictionaries_by_table_names(
    table_register: TableRegisters,
    table_names: list,
) -> dict:
    requested_table_b_dictionaries = (
        dict()
    )

    for table_name in table_names:
        __add_table_register_table_b_dictionary_to_output(
            requested_table_b_dictionaries=requested_table_b_dictionaries,
            table_register=table_register,
            table_name=table_name,
        )

    return (
        requested_table_b_dictionaries
    )


def __add_table_register_table_b_dictionary_to_output(
    requested_table_b_dictionaries: dict,
    table_register: TableRegisters,
    table_name: str,
) -> None:
    for (
        table_b_dictionary
    ) in (
        table_register.dictionary.values()
    ):
        if (
            table_name
            == table_b_dictionary.table_name
        ):
            requested_table_b_dictionaries[
                table_name
            ] = table_b_dictionary
