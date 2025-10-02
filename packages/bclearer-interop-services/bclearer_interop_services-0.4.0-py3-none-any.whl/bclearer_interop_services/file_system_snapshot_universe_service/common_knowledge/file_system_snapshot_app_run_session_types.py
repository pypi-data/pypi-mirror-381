from enum import auto

from nf_common_base.b_source.common.infrastructure.session.app_run_session.bie_app_run_session_types import (
    BieAppRunSessionTypes,
)


class FileSystemSnapshotAppRunSessionTypes(
    BieAppRunSessionTypes
):
    NOT_SET = auto()

    FILE_SYSTEM_SNAPSHOT_APP_RUN_SESSION = (
        auto()
    )
