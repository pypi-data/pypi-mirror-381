from nf_common_base.b_source.common.bie.infrastructure.types.bie_common_column_names import (
    BieCommonColumnNames,
)
from nf_common_base.b_source.common.configurations.bie_configurations.bie_id_configurations import (
    BieIdConfigurations,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.bie_file_system_snapshot_domain_types import (
    BieFileSystemSnapshotDomainTypes,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.datastructure.column_names.bie_snapshots_column_names import (
    BieSnapshotsColumnNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.datastructure.column_names.snapshots_column_names import (
    SnapshotsColumnNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.extended.non_root_relative_paths import (
    NonRootRelativePaths,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.extended.relative_paths import (
    RelativePaths,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.snapshots.file_system_snapshot_objects import (
    FileSystemSnapshotObjects,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.snapshots.individual_file_system_snapshot_files import (
    IndividualFileSystemSnapshotFiles,
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


# TODO: to create using a query with source tables
def create_snapshots_hr_table(
    file_system_snapshot_universe_registry: FileSystemSnapshotUniverseRegistries,
) -> DataFrame:
    table_as_dictionary = {}

    __populate_snapshots_hr_dataframe(
        file_system_snapshot_universe_registry=file_system_snapshot_universe_registry,
        table_as_dictionary=table_as_dictionary,
    )

    table_as_dataframe = convert_table_as_dictionary_to_dataframe(
        table_as_dictionary=table_as_dictionary
    )

    return table_as_dataframe.astype(
        str
    )


def __populate_snapshots_hr_dataframe(
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
        IndividualFileSystemSnapshotFiles,
    ):
        __add_file_system_snapshot_file_to_dataframe(
            table_as_dictionary=table_as_dictionary,
            file_system_snapshot_file=file_system_snapshot_object,
        )

    elif isinstance(
        file_system_snapshot_object,
        IndividualFileSystemSnapshotFolders,
    ):
        __add_file_system_snapshot_folder_to_dataframe(
            table_as_dictionary=table_as_dictionary,
            file_system_snapshot_folder=file_system_snapshot_object,
        )

        relative_path = file_system_snapshot_object.extended_objects[
            BieFileSystemSnapshotDomainTypes.BIE_RELATIVE_PATHS
        ]

        if not isinstance(
            relative_path, RelativePaths
        ):
            raise TypeError

        for (
            child_relative_path_object
        ) in (
            relative_path.relative_path_children
        ):
            if not isinstance(
                child_relative_path_object,
                RelativePaths,
            ):
                raise TypeError

            __add_file_system_snapshot_object_to_dataframe(
                table_as_dictionary=table_as_dictionary,
                file_system_snapshot_object=child_relative_path_object.snapshot,
            )


def __add_file_system_snapshot_file_to_dataframe(
    table_as_dictionary: dict,
    file_system_snapshot_file: IndividualFileSystemSnapshotFiles,
) -> None:
    whole_bie_ids = set()

    if file_system_snapshot_file.wholes:
        for (
            whole
        ) in (
            file_system_snapshot_file.wholes
        ):
            whole_bie_ids.add(
                whole.bie_id
            )

    part_bie_ids = set()

    if file_system_snapshot_file.parts:
        for (
            part
        ) in (
            file_system_snapshot_file.parts
        ):
            part_bie_ids.add(
                part.bie_id
            )

    bie_relative_path = file_system_snapshot_file.extended_objects[
        BieFileSystemSnapshotDomainTypes.BIE_RELATIVE_PATHS
    ]

    if isinstance(
        bie_relative_path,
        NonRootRelativePaths,
    ):
        bie_relative_path_parent_id = str(
            bie_relative_path.relative_path_parent.bie_id
        )

        relative_path_parent = str(
            bie_relative_path.relative_path_parent.relative_path
        )

    else:
        bie_relative_path_parent_id = (
            str()
        )

        relative_path_parent = str()

    __add_snapshot_hr_object_row(
        table_as_dictionary=table_as_dictionary,
        file_system_snapshot_object=file_system_snapshot_file,
        whole_bie_ids=whole_bie_ids,
        part_bie_ids=part_bie_ids,
        bie_relative_path_parent_id=bie_relative_path_parent_id,
        relative_path_parent=relative_path_parent,
    )


def __add_file_system_snapshot_folder_to_dataframe(
    table_as_dictionary: dict,
    file_system_snapshot_folder: IndividualFileSystemSnapshotFolders,
) -> None:
    relative_path = file_system_snapshot_folder.extended_objects[
        BieFileSystemSnapshotDomainTypes.BIE_RELATIVE_PATHS
    ]

    if isinstance(
        relative_path,
        NonRootRelativePaths,
    ):
        bie_relative_path_parent_id = str(
            relative_path.relative_path_parent.bie_id
        )

        relative_path_parent = str(
            relative_path.relative_path_parent.relative_path
        )

    else:
        bie_relative_path_parent_id = (
            str()
        )

        relative_path_parent = str()

    whole_bie_ids = set()

    if (
        file_system_snapshot_folder.wholes
    ):
        for (
            whole
        ) in (
            file_system_snapshot_folder.wholes
        ):
            whole_bie_ids.add(
                whole.bie_id
            )

    part_bie_ids = set()

    if (
        file_system_snapshot_folder.parts
    ):
        for (
            part
        ) in (
            file_system_snapshot_folder.parts
        ):
            part_bie_ids.add(
                part.bie_id
            )

    __add_snapshot_hr_object_row(
        table_as_dictionary=table_as_dictionary,
        file_system_snapshot_object=file_system_snapshot_folder,
        whole_bie_ids=whole_bie_ids,
        part_bie_ids=part_bie_ids,
        bie_relative_path_parent_id=bie_relative_path_parent_id,
        relative_path_parent=relative_path_parent,
    )


def __add_snapshot_hr_object_row(
    table_as_dictionary: dict,
    file_system_snapshot_object: IndividualFileSystemSnapshotObjects,
    whole_bie_ids: set,
    part_bie_ids: set,
    bie_relative_path_parent_id: str,
    relative_path_parent: str,
) -> None:
    if (
        BieFileSystemSnapshotDomainTypes.BIE_FILE_BYTE_CONTENTS
        in file_system_snapshot_object.inclusive_descendant_sum_objects
    ):
        descendent_sum_content_bie_id_int_value = file_system_snapshot_object.inclusive_descendant_sum_objects[
            BieFileSystemSnapshotDomainTypes.BIE_FILE_BYTE_CONTENTS
        ].bie_id.int_value

    else:
        descendent_sum_content_bie_id_int_value = (
            0
        )

    if (
        BieFileSystemSnapshotDomainTypes.BIE_FILE_BYTE_CONTENTS
        in file_system_snapshot_object.inclusive_ancestor_sum_objects
    ):
        ancestor_sum_content_bie_id_int_value = file_system_snapshot_object.inclusive_ancestor_sum_objects[
            BieFileSystemSnapshotDomainTypes.BIE_FILE_BYTE_CONTENTS
        ].bie_id.int_value

    else:
        ancestor_sum_content_bie_id_int_value = (
            0
        )

    relative_path = file_system_snapshot_object.extended_objects[
        BieFileSystemSnapshotDomainTypes.BIE_RELATIVE_PATHS
    ]

    if not isinstance(
        relative_path, RelativePaths
    ):
        raise TypeError

    snapshot_hr_object_row = {
        BieColumnNames.BIE_IDS.b_enum_item_name: file_system_snapshot_object.bie_id,
        BieCommonColumnNames.BASE_HR_NAMES.b_enum_item_name: file_system_snapshot_object.get_file_system_object().base_name,
        BieCommonColumnNames.BIE_DOMAIN_TYPE_IDS.b_enum_item_name: file_system_snapshot_object.bie_type.item_bie_identity,
        BieSnapshotsColumnNames.BIE_STAGE_OF_FILE_REFERENCE_NUMBER_IDS.b_enum_item_name: file_system_snapshot_object.extended_objects[
            BieFileSystemSnapshotDomainTypes.BIE_FILE_REFERENCE_NUMBERS
        ].bie_id,
        BieSnapshotsColumnNames.BIE_STAGE_OF_RELATIVE_PATH_IDS.b_enum_item_name: file_system_snapshot_object.extended_objects[
            BieFileSystemSnapshotDomainTypes.BIE_RELATIVE_PATHS
        ].bie_id,
        BieSnapshotsColumnNames.BIE_STAGE_OF_OBJECT_CONTENT_BIE_IDS.b_enum_item_name: file_system_snapshot_object.extended_objects[
            BieFileSystemSnapshotDomainTypes.BIE_FILE_BYTE_CONTENTS
        ].bie_id,
        SnapshotsColumnNames.STAGE_OF_RELATIVE_PATH_RELATIVE_PATHS.b_enum_item_name: relative_path.relative_path,
        BieCommonColumnNames.BIE_WHOLE_IDS.b_enum_item_name: (
            whole_bie_ids
            if whole_bie_ids
            else {}
        ),
        BieCommonColumnNames.BIE_PART_IDS.b_enum_item_name: (
            part_bie_ids
            if part_bie_ids
            else {}
        ),
        BieSnapshotsColumnNames.BIE_RELATIVE_PATH_PARENT_IDS.b_enum_item_name: bie_relative_path_parent_id,
        SnapshotsColumnNames.RELATIVE_PATH_PARENTS.b_enum_item_name: relative_path_parent,
    }

    if (
        BieIdConfigurations.EXPORT_INT_VALUE_COLUMNS
    ):
        snapshot_hr_object_row.update(
            {
                SnapshotsColumnNames.CONTENT_BIE_ID_INT_VALUES.b_enum_item_name: str(
                    file_system_snapshot_object.extended_objects[
                        BieFileSystemSnapshotDomainTypes.BIE_FILE_BYTE_CONTENTS
                    ].bie_id.int_value
                ),
                SnapshotsColumnNames.DESCENDENT_SUM_CONTENT_BIE_ID_INT_VALUES.b_enum_item_name: str(
                    descendent_sum_content_bie_id_int_value
                ),
                SnapshotsColumnNames.ANCESTOR_SUM_CONTENT_BIE_ID_INT_VALUES.b_enum_item_name: str(
                    ancestor_sum_content_bie_id_int_value
                ),
            }
        )

    table_as_dictionary[
        len(table_as_dictionary)
    ] = snapshot_hr_object_row
