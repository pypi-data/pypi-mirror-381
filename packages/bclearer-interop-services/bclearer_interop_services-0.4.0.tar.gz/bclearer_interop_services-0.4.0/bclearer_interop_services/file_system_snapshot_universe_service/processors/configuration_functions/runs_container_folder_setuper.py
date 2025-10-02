from pathlib import Path

from nf_common_base.b_source.common.configurations.b_configurations.b_configurations import (
    BConfigurations,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshot_multiverse.common_knowledge.file_system_snapshot_multiverses_folder_names import (
    FileSystemSnapshotMultiversesOutputFolderNames,
)


def setup_runs_container_folder(
    file_system_snapshot_multiverse,
):
    if (
        file_system_snapshot_multiverse.is_null_file_system_snapshot_multiverse()
    ):
        runs_container_folder = (
            BConfigurations.APP_RUN_OUTPUT_FOLDER
        )

    else:
        runs_container_folder = BConfigurations.APP_RUN_OUTPUT_FOLDER.get_descendant_file_system_folder(
            relative_path=Path(
                FileSystemSnapshotMultiversesOutputFolderNames.SINGLE_FSSU_RUNS.b_enum_item_name
            )
        )

        runs_container_folder.make_me_on_disk()

    return runs_container_folder
