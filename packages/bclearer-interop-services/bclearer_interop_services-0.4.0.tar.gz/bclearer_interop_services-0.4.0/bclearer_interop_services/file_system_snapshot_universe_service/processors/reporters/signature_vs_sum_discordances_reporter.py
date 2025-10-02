from nf_common_base.b_source.common.configurations.datastructure.logging_inspection_level_b_enums import (
    LoggingInspectionLevelBEnums,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.verses.file_system_snapshot_universes import (
    FileSystemSnapshotUniverses,
)
from nf_common_base.b_source.services.reporting_service.reporters.inspection_message_logger import (
    log_inspection_message,
)


def report_signature_vs_sum_discordances(
    file_system_snapshot_universe: FileSystemSnapshotUniverses,
) -> None:
    fssu_bie_profile = (
        file_system_snapshot_universe.file_system_snapshot_universe_registry.file_system_snapshot_container_bie_id_profile
    )

    if (
        fssu_bie_profile.are_root_bie_signature_sums_and_descendant_sums_bie_ids_all_equal
    ):
        return

    log_inspection_message(
        message="SIGNATURE VS SUM BIE IDS DISCORDANCE",
        logging_inspection_level_b_enum=LoggingInspectionLevelBEnums.INFO,
    )

    if (
        not fssu_bie_profile.is_root_bie_file_byte_content_signature_sum_and_descendant_sum_bie_ids_equal
    ):
        log_inspection_message(
            message="Type: file byte content\n"
            "ROOT BIE FILE BYTE CONTENT SIGNATURE SUM: {}\n"
            "ROOT BIE FILE BYTE CONTENT DESCENDANT SUM: {}".format(
                fssu_bie_profile.root_bie_file_byte_content_signature_sum_bie_id,
                fssu_bie_profile.root_bie_file_byte_content_descendant_sum_bie_id,
            ),
            logging_inspection_level_b_enum=LoggingInspectionLevelBEnums.INFO,
        )

    if (
        not fssu_bie_profile.is_root_bie_file_reference_number_signature_sum_and_descendant_sum_bie_ids_equal
    ):
        log_inspection_message(
            message="Type: file reference number\n"
            "ROOT BIE FILE REFERENCE NUMBER SIGNATURE SUM: {}\n"
            "ROOT BIE FILE REFERENCE NUMBER DESCENDANT SUM: {}".format(
                fssu_bie_profile.root_bie_file_reference_number_signature_sum_bie_id,
                fssu_bie_profile.root_bie_file_reference_number_descendant_sum_bie_id,
            ),
            logging_inspection_level_b_enum=LoggingInspectionLevelBEnums.WARNING,
        )

    if (
        not fssu_bie_profile.is_root_bie_relative_path_signature_sum_and_descendant_sum_bie_ids_equal
    ):
        log_inspection_message(
            message="Type: relative path\n"
            "ROOT BIE RELATIVE PATH SIGNATURE SUM: {}\n"
            "ROOT BIE RELATIVE PATH DESCENDANT SUM: {}".format(
                fssu_bie_profile.root_bie_relative_path_signature_sum_bie_id,
                fssu_bie_profile.root_bie_relative_path_descendant_sum_bie_id,
            ),
            logging_inspection_level_b_enum=LoggingInspectionLevelBEnums.WARNING,
        )
