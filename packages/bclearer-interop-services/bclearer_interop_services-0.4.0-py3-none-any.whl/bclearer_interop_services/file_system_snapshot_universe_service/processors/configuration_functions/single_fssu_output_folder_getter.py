from pathlib import Path

from nf_common_base.b_source.common.constants.standard_constants import (
    NAME_COMPONENT_DIVIDER,
)
from nf_common_base.b_source.services.file_system_service.objects.folders import (
    Folders,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshot_multiverse.common_knowledge.file_system_snapshot_multiverses_folder_names import (
    FileSystemSnapshotMultiversesOutputFolderNames,
)
from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshot_multiverse.verses.file_system_snapshot_multiverses import (
    FileSystemSnapshotMultiverses,
)


def get_single_fssu_output_folder(
    file_system_snapshot_multiverse: FileSystemSnapshotMultiverses,
    single_universe_runs_container_folder: Folders,
    iteration_index: int,
) -> Folders:
    if (
        file_system_snapshot_multiverse.is_null_file_system_snapshot_multiverse()
    ):
        single_fssu_output_folder = single_universe_runs_container_folder

    else:
        single_fssu_output_folder = __get_single_fssu_output_folder_for_multiple_cardinality_configuration(
            single_universe_runs_container_folder=single_universe_runs_container_folder,
            iteration_index=iteration_index,
        )

    return single_fssu_output_folder


def __get_single_fssu_output_folder_for_multiple_cardinality_configuration(
    single_universe_runs_container_folder: Folders,
    iteration_index: int,
) -> Folders:
    single_fssu_output_folder = single_universe_runs_container_folder.get_descendant_file_system_folder(
        relative_path=Path(
            FileSystemSnapshotMultiversesOutputFolderNames.FSSU_RUN.b_enum_item_name
            + NAME_COMPONENT_DIVIDER
            + str(iteration_index)
        )
    )

    return single_fssu_output_folder
