# from nf_common_base.b_source.services.file_system_snapshot_universe_service.configurations.file_system_snapshot_configurations import \
#     FileSystemSnapshotConfigurations
# from nf_common_base.b_source.services.file_system_snapshot_universe_service.runners.file_system_snapshot_service_handler import \
#     handle_file_system_snapshot_service
# from nf_common_base.b_source.services.file_system_snapshot_universe_service.exporters.file_system_snapshot_universe_if_inspection_is_enabled_exporter import \
#     export_file_system_snapshot_universe_if_inspection_is_enabled
#
#
# # TODO: to be deprecated?? This function seems to be used only by the old single tests - double check usages, and
# #  replace them with the new function run_and_export_file_system_snapshot_universe()
# def process_single_file_system_snapshot_universe(
#         # test_container_bie_id_profile: TestFileSystemSnapshotContainerBieIdProfileWrappers
#         file_system_snapshot_configuration: FileSystemSnapshotConfigurations) \
#         -> None:
#     file_system_snapshot_universe = \
#         handle_file_system_snapshot_service(
#             file_system_snapshot_configuration=file_system_snapshot_configuration)
#
#     export_file_system_snapshot_universe_if_inspection_is_enabled(
#         file_system_snapshot_universe=file_system_snapshot_universe,
#         output_folder=file_system_snapshot_configuration.single_fssu_output_folder)
#
#     # test_container_bie_id_profile.set_profile(
#     #     file_system_snapshot_universe.file_system_snapshot_universe_registry.file_system_snapshot_container_bie_id_profile)
