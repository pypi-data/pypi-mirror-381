from nf_common_base.b_source.common.bie.infrastructure.types.bie_common_column_names import (
    BieCommonColumnNames,
)
from nf_common_base.b_source.common.configurations.bie_configurations.bie_id_configurations import (
    BieIdConfigurations,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.bie_file_system_snapshot_domain_types import (
    BieFileSystemSnapshotDomainTypes,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.datastructure.column_names.snapshot_sum_objects_column_names import (
    SnapshotSumObjectsColumnNames,
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
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.common_knowledge.bie_column_names import (
    BieColumnNames,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.objects.bie_ids import (
    BieIds,
)
from nf_common_base.b_source.services.snapshot_universe_service.objects.sum_objects import (
    SumObjects,
)
from nf_common_base.b_source.services.table_as_dictionary_service.table_as_dictionary_to_dataframe_converter import (
    convert_table_as_dictionary_to_dataframe,
)
from pandas import DataFrame


def create_snapshot_sum_objects_table(
    file_system_snapshot_universe_registry: FileSystemSnapshotUniverseRegistries,
) -> DataFrame:
    table_as_dictionary = {}

    __populate_snapshots_sum_objects_as_dataframe(
        file_system_snapshot_universe_registry=file_system_snapshot_universe_registry,
        table_as_dictionary=table_as_dictionary,
    )

    table_as_dataframe = convert_table_as_dictionary_to_dataframe(
        table_as_dictionary=table_as_dictionary
    )

    return table_as_dataframe.astype(
        str
    )


def __populate_snapshots_sum_objects_as_dataframe(
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
    __add_file_system_snapshot_file_sum_to_dataframe(
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


def __add_file_system_snapshot_file_sum_to_dataframe(
    table_as_dictionary: dict,
    file_system_snapshot_object: FileSystemSnapshotObjects,
) -> None:
    for (
        sum_object
    ) in (
        file_system_snapshot_object.inclusive_ancestor_sum_objects.values()
    ):
        __add_sum_object_to_dataframe(
            table_as_dictionary=table_as_dictionary,
            sum_object=sum_object,
            inclusivity_type=BieFileSystemSnapshotDomainTypes.INCLUSIVE,
            owning_file_system_snapshot_object_bie_id=file_system_snapshot_object.bie_id,
        )

    for (
        sum_object
    ) in (
        file_system_snapshot_object.inclusive_descendant_sum_objects.values()
    ):
        __add_sum_object_to_dataframe(
            table_as_dictionary=table_as_dictionary,
            sum_object=sum_object,
            inclusivity_type=BieFileSystemSnapshotDomainTypes.INCLUSIVE,
            owning_file_system_snapshot_object_bie_id=file_system_snapshot_object.bie_id,
        )

    for (
        sum_object
    ) in (
        file_system_snapshot_object.exclusive_ancestor_sum_objects.values()
    ):
        __add_sum_object_to_dataframe(
            table_as_dictionary=table_as_dictionary,
            sum_object=sum_object,
            inclusivity_type=BieFileSystemSnapshotDomainTypes.EXCLUSIVE,
            owning_file_system_snapshot_object_bie_id=file_system_snapshot_object.bie_id,
        )

    for (
        sum_object
    ) in (
        file_system_snapshot_object.exclusive_descendant_sum_objects.values()
    ):
        __add_sum_object_to_dataframe(
            table_as_dictionary=table_as_dictionary,
            sum_object=sum_object,
            inclusivity_type=BieFileSystemSnapshotDomainTypes.EXCLUSIVE,
            owning_file_system_snapshot_object_bie_id=file_system_snapshot_object.bie_id,
        )


def __add_sum_object_to_dataframe(
    table_as_dictionary: dict,
    sum_object: SumObjects,
    inclusivity_type: BieFileSystemSnapshotDomainTypes,
    owning_file_system_snapshot_object_bie_id: BieIds,
) -> None:
    sum_object_row = {
        SnapshotSumObjectsColumnNames.OWNING_BIE_SNAPSHOT_IDS.b_enum_item_name: owning_file_system_snapshot_object_bie_id,
        BieCommonColumnNames.BASE_HR_NAMES.b_enum_item_name: sum_object.base_hr_name,
        BieCommonColumnNames.BIE_DOMAIN_TYPE_IDS.b_enum_item_name: sum_object.bie_type.item_bie_identity,
        SnapshotSumObjectsColumnNames.INCLUSIVITY_TYPE_IDS.b_enum_item_name: inclusivity_type.item_bie_identity,
        SnapshotSumObjectsColumnNames.DIRECTION_TYPE_IDS.b_enum_item_name: sum_object.direction_type.item_bie_identity,
        SnapshotSumObjectsColumnNames.SUMMED_BIE_OBJECT_TYPE_IDS.b_enum_item_name: sum_object.bie_summed_type.item_bie_identity,
        BieColumnNames.SUM_VALUE_BIE_IDS.b_enum_item_name: sum_object.bie_id,
    }

    if (
        BieIdConfigurations.EXPORT_INT_VALUE_COLUMNS
    ):
        sum_object_row.update(
            {
                SnapshotSumObjectsColumnNames.SUM_OBJECT_BIE_ID_INT_VALUES.b_enum_item_name: sum_object.bie_id.int_value
            }
        )

    table_as_dictionary[
        len(table_as_dictionary)
    ] = sum_object_row
