# import pathlib
# from nf_common_base.b_source.common.constants.standard_constants import NAME_COMPONENT_DIVIDER
# from nf_common_base.b_source.services.file_system_service.objects.folders import Folders
# from nf_common_base.b_source.services.file_system_snapshot_universe_service.file_system_snapshot_multiverse.common_knowledge.file_system_snapshot_multiverses_folder_names import \
#     FileSystemSnapshotMultiversesOutputFolderNames
# from nf_common_base.b_source.services.file_system_snapshot_universe_service.configurations.file_system_snapshot_configurations import \
#     FileSystemSnapshotConfigurations
#
#
# # TODO: to be deprecated
# def setup_file_system_snapshot_configuration(
#         single_file_system_snapshot_universe_runs_folder: Folders,
#         iteration_index: int,
#         input_snapshot_container_folder: Folders) \
#         -> FileSystemSnapshotConfigurations:
#     # TODO: Move to outside the loop - affected by the if choice - MOVED OUT
#     single_file_system_snapshot_universe_output_folder = \
#         single_file_system_snapshot_universe_runs_folder.get_descendant_file_system_folder(
#             relative_path=pathlib.Path(
#                 FileSystemSnapshotMultiversesOutputFolderNames.FSSU_RUN.b_enum_item_name
#                 + NAME_COMPONENT_DIVIDER + str(iteration_index)))
#
#     file_system_snapshot_configuration = \
#         FileSystemSnapshotConfigurations(
#             single_fssu_output_folder=single_file_system_snapshot_universe_output_folder,
#             input_snapshot_container_folder=input_snapshot_container_folder,
#             remove_temporary_root_folder=False)
#
#     return \
#         file_system_snapshot_configuration
