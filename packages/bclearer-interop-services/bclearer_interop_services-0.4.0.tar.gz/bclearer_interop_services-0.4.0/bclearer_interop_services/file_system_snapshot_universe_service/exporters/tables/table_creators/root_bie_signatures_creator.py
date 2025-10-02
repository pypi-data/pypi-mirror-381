from nf_common_base.b_source.common.bie.infrastructure.types.bie_common_column_names import (
    BieCommonColumnNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.common_knowledge.bie_file_system_snapshot_domain_types import (
    BieFileSystemSnapshotDomainTypes,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.verses.file_system_snapshot_universe_registries import (
    FileSystemSnapshotUniverseRegistries,
)
from nf_common_base.b_source.services.identification_services.b_identity_ecosystem.objects.bie_signatures import (
    BieSignatures,
)
from nf_common_base.b_source.services.table_as_dictionary_service.table_as_dictionary_to_dataframe_converter import (
    convert_table_as_dictionary_to_dataframe,
)
from pandas import DataFrame


def create_root_bie_signatures_table(
    file_system_snapshot_universe_registry: FileSystemSnapshotUniverseRegistries,
) -> DataFrame:
    table_as_dictionary = {}

    __populate_root_bie_signatures_dataframe(
        file_system_snapshot_universe_registry=file_system_snapshot_universe_registry,
        table_as_dictionary=table_as_dictionary,
    )

    table_as_dataframe = convert_table_as_dictionary_to_dataframe(
        table_as_dictionary=table_as_dictionary
    )

    return table_as_dataframe.astype(
        str
    )


def __populate_root_bie_signatures_dataframe(
    file_system_snapshot_universe_registry: FileSystemSnapshotUniverseRegistries,
    table_as_dictionary: dict,
) -> None:
    file_system_snapshot_object_bie_id_signatures = (
        file_system_snapshot_universe_registry.file_system_snapshot_container_bie_id_profile.root_bie_signature_registry.file_system_snapshot_object_bie_id_signatures
    )

    for (
        bie_type,
        bie_signature,
    ) in (
        file_system_snapshot_object_bie_id_signatures.items()
    ):
        __add_bie_signature_to_dataframe(
            table_as_dictionary=table_as_dictionary,
            bie_type=bie_type,
            bie_signature=bie_signature,
        )


def __add_bie_signature_to_dataframe(
    table_as_dictionary: dict,
    bie_type: BieFileSystemSnapshotDomainTypes,
    bie_signature: BieSignatures,
) -> None:
    bie_signature_row = {
        BieCommonColumnNames.BIE_DOMAIN_TYPE_IDS.b_enum_item_name: bie_type.item_bie_identity,
        BieCommonColumnNames.BIE_SIGNATURE_SUM_IDS.b_enum_item_name: bie_signature.signature_sum_bie_id,
    }

    table_as_dictionary[
        len(table_as_dictionary)
    ] = bie_signature_row
