import pathlib

from nf_common_base.b_source.common.configurations.b_configurations.b_configurations import (
    BConfigurations,
)
from nf_common_base.b_source.services.file_system_service.objects.folders import (
    Folders,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.fssu_registry_exporter import (
    export_registry_dataframe_to_access_database,
    export_registry_dataframe_to_sqlite_database,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.verses.file_system_snapshot_universes import (
    FileSystemSnapshotUniverses,
)

SNAPSHOT_UNIVERSE_DOMAIN_NAME = (
    "snapshot_universe_domain"
)


# TODO: Move out of the test/ folder, otherwise it will cause problems when imported from other repository
def export_file_system_snapshot_universe_if_inspection_is_enabled(
    file_system_snapshot_universe: FileSystemSnapshotUniverses,
    output_folder: Folders,
) -> None:
    # TODO: this variable has to be created and added a by-default value to TRUE - DONE
    if (
        not BConfigurations.ENABLE_DATABASE_INSPECTION
    ):
        return

    test_case_output_folder = output_folder.get_descendant_file_system_folder(
        relative_path=pathlib.Path(
            SNAPSHOT_UNIVERSE_DOMAIN_NAME
        )
    )

    test_case_output_folder.make_me_on_disk()

    dataframes_dictionary_keyed_on_string = (
        file_system_snapshot_universe.file_system_snapshot_universe_registry.export_register_as_dictionary()
    )

    # TODO: these should be called from the universe.
    if (
        BConfigurations.ENABLE_MS_ACCESS_DATABASE_INSPECTION
    ):
        export_registry_dataframe_to_access_database(
            dataframes_dictionary_keyed_on_string=dataframes_dictionary_keyed_on_string,
            output_folder=test_case_output_folder,
            prefix_string=SNAPSHOT_UNIVERSE_DOMAIN_NAME,
            suffix_string=str(),
        )

    if (
        BConfigurations.ENABLE_SQLITE_DATABASE_INSPECTION
    ):
        export_registry_dataframe_to_sqlite_database(
            dataframes_dictionary_keyed_on_string=dataframes_dictionary_keyed_on_string,
            output_folder=test_case_output_folder,
            prefix_string=SNAPSHOT_UNIVERSE_DOMAIN_NAME,
            suffix_string=str(),
        )
