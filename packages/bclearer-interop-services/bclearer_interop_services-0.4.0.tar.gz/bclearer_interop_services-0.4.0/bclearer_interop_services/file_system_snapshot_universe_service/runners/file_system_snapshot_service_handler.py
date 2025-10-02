from nf_common_base.b_source.services.file_system_snapshot_universe_service.configurations.file_system_snapshot_configurations import (
    FileSystemSnapshotConfigurations,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.verses.file_system_snapshot_universes import (
    FileSystemSnapshotUniverses,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.processors.reporters.signature_vs_sum_discordances_reporter import (
    report_signature_vs_sum_discordances,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.runners.file_system_snapshot_universe_getter import (
    get_file_system_snapshot_universe,
)
from nf_common_base.b_source.services.reporting_service.wrappers.run_and_log_function_wrapper import (
    run_and_log_function,
)


# TODO: Find all calls and move here
@run_and_log_function()
def handle_file_system_snapshot_service(
    file_system_snapshot_configuration: FileSystemSnapshotConfigurations,
) -> FileSystemSnapshotUniverses:
    # TODO: Create app session object and pass it in?
    file_system_snapshot_universe = get_file_system_snapshot_universe(
        file_system_snapshot_configuration=file_system_snapshot_configuration
    )

    report_signature_vs_sum_discordances(
        file_system_snapshot_universe=file_system_snapshot_universe
    )

    return file_system_snapshot_universe
