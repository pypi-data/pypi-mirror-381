from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshot_multiverse.processors.file_system_snapshot_multiverse_analyser import (
    analyse_file_system_snapshot_multiverse,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshots_service_handler import (
    handle_file_system_snapshots_service,
)
from nf_common_base.b_source.services.reporting_service.wrappers.run_and_log_function_wrapper import (
    run_and_log_function,
)


@run_and_log_function()
def run_file_system_snapshots_and_analysis_b_application() -> (
    None
):
    file_system_snapshot_multiverse = (
        handle_file_system_snapshots_service()
    )

    if (
        not file_system_snapshot_multiverse.is_null_file_system_snapshot_multiverse()
    ):
        analyse_file_system_snapshot_multiverse(
            file_system_snapshot_multiverse=file_system_snapshot_multiverse
        )
