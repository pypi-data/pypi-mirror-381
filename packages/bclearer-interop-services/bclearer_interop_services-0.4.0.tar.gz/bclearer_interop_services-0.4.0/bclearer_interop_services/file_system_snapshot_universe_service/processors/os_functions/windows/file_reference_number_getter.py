import win32file


def get_file_reference_number(
    file_path_as_string: str,
):
    handle = win32file.CreateFile(
        file_path_as_string,
        win32file.GENERIC_READ,
        win32file.FILE_SHARE_READ
        | win32file.FILE_SHARE_WRITE
        | win32file.FILE_SHARE_DELETE,
        None,
        win32file.OPEN_EXISTING,
        win32file.FILE_FLAG_BACKUP_SEMANTICS,
        None,
    )

    info = win32file.GetFileInformationByHandle(
        handle
    )

    handle.Close()

    n_file_index_high = info[8]

    n_file_index_low = info[9]

    file_reference_number = (
        n_file_index_high << 32
    ) | n_file_index_low

    return file_reference_number
