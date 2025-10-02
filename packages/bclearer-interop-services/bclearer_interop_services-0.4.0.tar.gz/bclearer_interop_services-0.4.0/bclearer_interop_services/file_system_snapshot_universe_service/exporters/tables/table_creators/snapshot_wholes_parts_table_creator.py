from nf_common_base.b_source.common.bie.infrastructure.types.bie_common_column_names import (
    BieCommonColumnNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.snapshots.file_system_snapshot_objects import (
    FileSystemSnapshotObjects,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.snapshots.individual_file_system_snapshot_folders import (
    IndividualFileSystemSnapshotFolders,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.verses.file_system_snapshot_universe_registries import (
    FileSystemSnapshotUniverseRegistries,
)
from nf_common_base.b_source.services.table_as_dictionary_service.table_as_dictionary_to_dataframe_converter import (
    convert_table_as_dictionary_to_dataframe,
)
from pandas import DataFrame


def create_snapshot_wholes_parts_table(
    file_system_snapshot_universe_registry: FileSystemSnapshotUniverseRegistries,
) -> DataFrame:
    table_as_dictionary = {}

    __populate_snapshot_whole_parts_dataframe(
        file_system_snapshot_universe_registry=file_system_snapshot_universe_registry,
        table_as_dictionary=table_as_dictionary,
    )

    if table_as_dictionary:
        table_as_dataframe = convert_table_as_dictionary_to_dataframe(
            table_as_dictionary=table_as_dictionary
        )

    else:
        table_as_dataframe = DataFrame(
            columns=[
                BieCommonColumnNames.BIE_WHOLE_IDS.b_enum_item_name,
                BieCommonColumnNames.BIE_PART_IDS.b_enum_item_name,
            ]
        )
    return table_as_dataframe.astype(
        str
    )


def __populate_snapshot_whole_parts_dataframe(
    file_system_snapshot_universe_registry: FileSystemSnapshotUniverseRegistries,
    table_as_dictionary: dict,
) -> None:
    __add_file_system_snapshot_object_to_dataframe(
        table_as_dictionary=table_as_dictionary,
        file_system_snapshot_object=file_system_snapshot_universe_registry.root_relative_path.snapshot,
    )


def __add_file_system_snapshot_object_to_dataframe(
    table_as_dictionary: dict,
    file_system_snapshot_object: FileSystemSnapshotObjects,
) -> None:
    if isinstance(
        file_system_snapshot_object,
        IndividualFileSystemSnapshotFolders,
    ):
        for (
            snapshot_part
        ) in (
            file_system_snapshot_object.parts
        ):
            __add_snapshot_object_row(
                table_as_dictionary=table_as_dictionary,
                whole_file_system_snapshot_object=file_system_snapshot_object,
                part_file_system_snapshot_object=snapshot_part,
            )

            __add_file_system_snapshot_object_to_dataframe(
                table_as_dictionary=table_as_dictionary,
                file_system_snapshot_object=snapshot_part,
            )


def __add_snapshot_object_row(
    table_as_dictionary: dict,
    whole_file_system_snapshot_object: FileSystemSnapshotObjects,
    part_file_system_snapshot_object: FileSystemSnapshotObjects,
) -> None:
    snapshot_object_row = {
        BieCommonColumnNames.BIE_WHOLE_IDS.b_enum_item_name: whole_file_system_snapshot_object.bie_id,
        BieCommonColumnNames.BIE_PART_IDS.b_enum_item_name: part_file_system_snapshot_object.bie_id,
    }

    table_as_dictionary[
        len(table_as_dictionary)
    ] = snapshot_object_row
