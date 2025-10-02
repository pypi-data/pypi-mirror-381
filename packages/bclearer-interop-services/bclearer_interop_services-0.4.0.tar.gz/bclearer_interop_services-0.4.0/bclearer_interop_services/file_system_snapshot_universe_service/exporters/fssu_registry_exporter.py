from pathlib import Path

from nf_common_base.b_source.common.configurations.b_configurations.b_configurations import (
    BConfigurations,
)
from nf_common_base.b_source.services.file_system_service.file_system_paths.constants.file_system_file_extensions import (
    FileSystemFileExtensions,
)
from nf_common_base.b_source.services.file_system_service.objects.folders import (
    Folders,
)
from nf_common_base.b_source.services.import_export_service.dataframes.export_to.databases.access.dataframes_dictionary_to_new_access_as_strings_writer import (
    write_dataframes_dictionary_to_new_access_as_strings,
)
from nf_common_base.b_source.services.import_export_service.dataframes.export_to.databases.sqlite.dataframes_dictionary_to_existing_sqlite_as_strings_writer import (
    write_dataframes_dictionary_to_existing_sqlite_as_strings,
)
from nf_common_base.b_source.services.import_export_service.sqlite.sqlite_database_creator import (
    create_sqlite_database,
)


# TODO: to move to the new utility instead? this should not be an unit tet helper - OXi: I think it should be a method
#  of the universe/registry, or at least a helper in the FSSU universe (not only the utility will use it, e.g.: the gash
#  Excel stuff will use it too)
def export_registry_dataframe_to_access_database(
    dataframes_dictionary_keyed_on_string: dict,
    output_folder: Folders,
    prefix_string: str = "",
    suffix_string: str = "",
) -> None:
    access_database_file_base_name = (
        prefix_string
        + "_"
        + BConfigurations.APP_RUN_TIME_AS_STRING
        + FileSystemFileExtensions.ACCDB.delimited_file_extension
    )

    access_database_file = output_folder.get_descendant_file_system_file(
        relative_path=Path(
            access_database_file_base_name
        )
    )

    write_dataframes_dictionary_to_new_access_as_strings(
        dataframes_dictionary_keyed_on_string=dataframes_dictionary_keyed_on_string,
        access_database_file=access_database_file,
    )


# TODO: to move to the new utility instead? this should not be an unit tet helper
def export_registry_dataframe_to_sqlite_database(
    dataframes_dictionary_keyed_on_string: dict,
    output_folder: Folders,
    prefix_string: str = "",
    suffix_string: str = "",
) -> None:
    sqlite_database_file_base_name = (
        prefix_string
        + "_"
        + BConfigurations.APP_RUN_TIME_AS_STRING
    )

    sqlite_database_file = create_sqlite_database(
        sqlite_database_folder=output_folder,
        sqlite_database_base_name=sqlite_database_file_base_name,
    )

    write_dataframes_dictionary_to_existing_sqlite_as_strings(
        dataframes_dictionary_keyed_on_string=dataframes_dictionary_keyed_on_string,
        sqlite_database_file=sqlite_database_file,
    )
