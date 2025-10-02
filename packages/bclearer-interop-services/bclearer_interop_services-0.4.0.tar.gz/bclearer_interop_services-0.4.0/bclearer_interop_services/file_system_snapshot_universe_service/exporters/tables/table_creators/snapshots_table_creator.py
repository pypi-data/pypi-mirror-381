from nf_common_base.b_source.common.bie.infrastructure.types.bie_common_column_names import (
    BieCommonColumnNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.bie_file_system_snapshot_domain_types import (
    BieFileSystemSnapshotDomainTypes,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.datastructure.column_names.snapshots_column_names import (
    SnapshotsColumnNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.snapshots.individual_file_system_snapshot_folders import (
    IndividualFileSystemSnapshotFolders,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.snapshots.individual_file_system_snapshot_objects import (
    IndividualFileSystemSnapshotObjects,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.verses.file_system_snapshot_universe_registries import (
    FileSystemSnapshotUniverseRegistries,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.bie_column_names import (
    BieColumnNames,
)
from nf_common_base.b_source.services.table_as_dictionary_service.table_as_dictionary_to_dataframe_converter import (
    convert_table_as_dictionary_to_dataframe,
)
from pandas import DataFrame


def create_snapshots_table(
    file_system_snapshot_universe_registry: FileSystemSnapshotUniverseRegistries,
) -> DataFrame:
    table_as_dictionary = {}

    __populate_snapshots_dataframe(
        file_system_snapshot_universe_registry=file_system_snapshot_universe_registry,
        table_as_dictionary=table_as_dictionary,
    )

    table_as_dataframe = convert_table_as_dictionary_to_dataframe(
        table_as_dictionary=table_as_dictionary
    )

    return table_as_dataframe.astype(
        str
    )


def __populate_snapshots_dataframe(
    file_system_snapshot_universe_registry: FileSystemSnapshotUniverseRegistries,
    table_as_dictionary: dict,
) -> None:
    __add_file_system_snapshot_object_to_dataframe(
        table_as_dictionary=table_as_dictionary,
        file_system_snapshot_object=file_system_snapshot_universe_registry.root_relative_path.snapshot,
    )


def __add_file_system_snapshot_object_to_dataframe(
    table_as_dictionary: dict,
    file_system_snapshot_object: IndividualFileSystemSnapshotObjects,
) -> None:
    __add_file_system_snapshot_file_to_dataframe(
        table_as_dictionary=table_as_dictionary,
        file_system_snapshot_object=file_system_snapshot_object,
    )

    if isinstance(
        file_system_snapshot_object,
        IndividualFileSystemSnapshotFolders,
    ):
        for (
            snapshot_part
        ) in (
            file_system_snapshot_object.parts
        ):
            __add_file_system_snapshot_object_to_dataframe(
                table_as_dictionary=table_as_dictionary,
                file_system_snapshot_object=snapshot_part,
            )


def __add_file_system_snapshot_file_to_dataframe(
    table_as_dictionary: dict,
    file_system_snapshot_object: IndividualFileSystemSnapshotObjects,
) -> None:
    # TODO: added new column temporarily: SnapshotsColumnNames.ROOT_RELATIVE_PATH_NAME - needs proper design
    root_relative_path = file_system_snapshot_object.extended_objects[
        BieFileSystemSnapshotDomainTypes.BIE_RELATIVE_PATHS
    ].relative_path

    root_relative_path_name = str(
        root_relative_path
    )

    file_system_snapshot_file_row = {
        BieColumnNames.BIE_IDS.b_enum_item_name: file_system_snapshot_object.bie_id,
        BieCommonColumnNames.BASE_HR_NAMES.b_enum_item_name: file_system_snapshot_object.base_hr_name,
        BieCommonColumnNames.BIE_DOMAIN_TYPE_IDS.b_enum_item_name: file_system_snapshot_object.bie_type.item_bie_identity,
        SnapshotsColumnNames.FULL_NAME.b_enum_item_name: file_system_snapshot_object.get_file_system_object().absolute_path_string,
        SnapshotsColumnNames.ROOT_RELATIVE_PATH_NAMES.b_enum_item_name: root_relative_path_name,
        SnapshotsColumnNames.EXTENSION.b_enum_item_name: file_system_snapshot_object.file_system_object_properties.extension,
        SnapshotsColumnNames.LENGTH.b_enum_item_name: file_system_snapshot_object.file_system_object_properties.length,
        SnapshotsColumnNames.CHILD_COUNT.b_enum_item_name: file_system_snapshot_object.get_children_count(),
        SnapshotsColumnNames.CREATION_TIME.b_enum_item_name: file_system_snapshot_object.file_system_object_properties.creation_time,
        SnapshotsColumnNames.LAST_ACCESS_TIME.b_enum_item_name: file_system_snapshot_object.file_system_object_properties.last_access_time,
        SnapshotsColumnNames.LAST_WRITE_TIME.b_enum_item_name: file_system_snapshot_object.file_system_object_properties.last_write_time,
        "_raw_file_system_snapshot_object": file_system_snapshot_object,
    }

    table_as_dictionary[
        len(table_as_dictionary)
    ] = file_system_snapshot_file_row
