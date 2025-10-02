from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.datastructure.table_names.file_system_snapshot_universe_registry_table_names import (
    FileSystemSnapshotUniverseRegistryTableNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_creators.extended_objects_table_creator import (
    create_extended_objects_table,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_creators.root_bie_signatures_creator import (
    create_root_bie_signatures_table,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_creators.snapshot_sum_objects_table_creator import (
    create_snapshot_sum_objects_table,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_creators.snapshot_wholes_parts_table_creator import (
    create_snapshot_wholes_parts_table,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_creators.snapshots_hr_table_creator import (
    create_snapshots_hr_table,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_creators.snapshots_table_creator import (
    create_snapshots_table,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.tables.table_creators.universes_table_creator import (
    create_universes_table,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.verses.file_system_snapshot_universe_registries import (
    FileSystemSnapshotUniverseRegistries,
)


def create_fssu_registry_dataframes_dictionary(
    file_system_snapshot_universe_registry: FileSystemSnapshotUniverseRegistries,
) -> dict:
    snapshot_universes_table = create_universes_table(
        file_system_snapshot_universe_registry=file_system_snapshot_universe_registry
    )

    snapshots_hr_table = create_snapshots_hr_table(
        file_system_snapshot_universe_registry=file_system_snapshot_universe_registry
    )

    snapshots_table = create_snapshots_table(
        file_system_snapshot_universe_registry=file_system_snapshot_universe_registry
    )

    extended_objects_table = create_extended_objects_table(
        file_system_snapshot_universe_registry=file_system_snapshot_universe_registry
    )

    wholes_parts_table = create_snapshot_wholes_parts_table(
        file_system_snapshot_universe_registry=file_system_snapshot_universe_registry
    )

    snapshot_sum_objects_table = create_snapshot_sum_objects_table(
        file_system_snapshot_universe_registry=file_system_snapshot_universe_registry
    )

    dataframes_dictionary_keyed_on_string = {
        FileSystemSnapshotUniverseRegistryTableNames.SNAPSHOT_DOMAIN_UNIVERSES.b_enum_item_name: snapshot_universes_table,
        FileSystemSnapshotUniverseRegistryTableNames.SNAPSHOTS_HR_ORIGINAL.b_enum_item_name: snapshots_hr_table,
        FileSystemSnapshotUniverseRegistryTableNames.SNAPSHOTS.b_enum_item_name: snapshots_table,
        FileSystemSnapshotUniverseRegistryTableNames.EXTENDED_OBJECTS.b_enum_item_name: extended_objects_table,
        FileSystemSnapshotUniverseRegistryTableNames.SNAPSHOT_WHOLES_PARTS_BREAKDOWN.b_enum_item_name: wholes_parts_table,
        FileSystemSnapshotUniverseRegistryTableNames.SNAPSHOT_SUM_OBJECTS.b_enum_item_name: snapshot_sum_objects_table,
    }

    root_bie_signatures_table = create_root_bie_signatures_table(
        file_system_snapshot_universe_registry=file_system_snapshot_universe_registry
    )

    if (
        not root_bie_signatures_table.empty
    ):
        dataframes_dictionary_keyed_on_string[
            FileSystemSnapshotUniverseRegistryTableNames.ROOT_BIE_SIGNATURE_SUMS.b_enum_item_name
        ] = root_bie_signatures_table

    return dataframes_dictionary_keyed_on_string
