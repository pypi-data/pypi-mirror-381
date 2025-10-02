from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.snapshots.file_system_snapshot_objects import (
    FileSystemSnapshotObjects,
)


def add_file_system_snapshot_object_to_root_bie_signature_registry(
    root_bie_signature_registry: "RunContainerBieSignatureRegistries",
    file_system_snapshot_object: FileSystemSnapshotObjects,
) -> None:
    from nf_common_base.b_source.services.file_system_snapshot_universe_service.objects.verses.root_relative_path_bie_signature_registries import (
        RootRelativePathBieSignatureRegistries,
    )

    if not isinstance(
        root_bie_signature_registry,
        RootRelativePathBieSignatureRegistries,
    ):
        raise TypeError

    root_bie_signature_registry.add_bie_id_to_signature_by_type(
        bie_id=file_system_snapshot_object.bie_id,
        bie_id_type=file_system_snapshot_object.bie_type,
    )

    for (
        bie_id_type,
        extended_object,
    ) in (
        file_system_snapshot_object.extended_objects.items()
    ):
        root_bie_signature_registry.add_bie_id_to_signature_by_type(
            bie_id=extended_object.bie_id,
            bie_id_type=bie_id_type,
        )
