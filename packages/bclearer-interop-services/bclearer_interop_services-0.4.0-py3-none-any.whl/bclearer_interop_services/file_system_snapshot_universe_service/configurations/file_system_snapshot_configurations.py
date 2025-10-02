from nf_common_base.b_source.services.file_system_service.objects.folders import (
    Folders,
)


class FileSystemSnapshotConfigurations:
    def __init__(
        self,
        single_fssu_output_folder: Folders,
        input_snapshot_container_folder: Folders,
        remove_temporary_root_folder: bool = True,
    ):
        # TODO: line below will be deprecated - to check
        self.remove_temporary_root_folder = (
            remove_temporary_root_folder
        )

        self.single_fssu_output_folder: (
            Folders
        ) = single_fssu_output_folder

        self.input_snapshot_container_folder: (
            Folders
        ) = input_snapshot_container_folder
