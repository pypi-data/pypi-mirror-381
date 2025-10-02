#!/usr/bin/env python3
# vim: fileencoding=utf-8 ts=4
# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: © Copyright 2025 by Christian Dönges. All rights reserved.
# SPDXID: SPDXRef-test-utilities-file-birthtime-py

from datetime import datetime, timedelta, timezone
import os
from pathlib import Path
from shutil import rmtree
from tempfile import mkdtemp, mkstemp
from time import sleep

import pytest
from pymisclib.utilities import OsInfo, file_birthtime


@pytest.fixture
def cleanup():
    """Delete temporary files and directories."""
    paths_to_delete = []
    yield paths_to_delete
    for path in paths_to_delete:
        if os.path.exists(path):
            if os.path.isdir(path):
                rmtree(path)
            else:
                os.remove(path)


def os_dependent_use(path: os.PathLike,
                     tz: timezone|None,
                     fudge: bool) -> datetime|None:
    """Call `file_bithtime()` and interpret the result depending on the OS.

    :param os.PathLike path: Path to a filesystem object (e.g. file or directory.)
    :param timezone|None tz: Timezone used by the filesystem.
    :param bool fudge: If `False`, use only `st_birthtime`. If `True`, try more
        fields.
    :raise AttributeError: Unable to determine creation time without fudging on
        an OS where this is expected to work.
    :return: Creation time of the file or None.
    :rtype: datetime|None
    """
    if fudge:
        return file_birthtime(path, tz,True)
    os_info = OsInfo()
    if os_info.is_windows:
        # Windows has st_birthtime.
        return file_birthtime(path, tz,False)
    if os_info.is_macos or os_info.is_bsd:
        # macOS and some BSDs have st_birthtime.
        return file_birthtime(path, tz,False)
    if os_info.is_linux:
        # Linux does not have st_birthtime.
        with pytest.raises(AttributeError):
            file_birthtime(path, tz,False)
        return None
    # Unknown OS, just try it ...
    return file_birthtime(path, tz,False)


@pytest.mark.parametrize('fudge', [True, False])
def test_file_birthtime(cleanup, fudge):
    tz = datetime.now().astimezone().tzinfo
    max_delta = timedelta(seconds=1)  # this may need to be 2s on Windows with FAT
    ts_start = datetime.now(tz)
    (handle, path) = mkstemp()
    cleanup.append(path)
    ts_created = datetime.now(tz)
    assert ts_start <= ts_created
    os.close(handle)

    ts1 = os_dependent_use(path, tz, fudge)
    if ts1 is None and fudge == False:
        # If there is no st_birthtime, we can't do anything.
        return
    assert ts1 is not None
    # For some reason, on Linux ts1 can be before ts_start.
    # This makes the comparison a little more involved.
    if ts1 <= ts_start:
        assert ts_start - ts1 <= max_delta
    else:
        assert ts1 - ts_start <= max_delta
    if ts1 <= ts_created:
        assert ts_created - ts1 <= max_delta
    else:
        assert ts1 - ts_created <= max_delta
    sleep(2.5)
    ts2 = os_dependent_use(path, tz, fudge)
    assert ts2 is not None
    assert ts1 == ts2
    with open(path, "w+") as f:
        f.write(str(ts1))
    ts3 = file_birthtime(path, tz, fudge)
    if not fudge:
        assert ts1 == ts3
    else:
        assert ts1 <= ts3


@pytest.mark.parametrize('fudge', [True, False])
def test_directory_birthtime(cleanup, fudge):
    max_delta = timedelta(seconds=1)  # this may need to be 2s on Windows with FAT
    tz = datetime.now().astimezone().tzinfo
    ts_start = datetime.now(tz)
    path = mkdtemp()
    cleanup.append(path)
    ts_created = datetime.now(tz)
    assert ts_start <= ts_created
    ts1 = os_dependent_use(path, tz, fudge)
    if ts1 is None and fudge == False:
        # If there is no st_birthtime, we can't do anything.
        return
    assert ts1 is not None
    # For some reason, on Linux ts1 can be before ts_start.
    # This makes the comparison a little more involved.
    if ts1 <= ts_start:
        assert ts_start - ts1 <= max_delta
    else:
        assert ts1 - ts_start <= max_delta
    if ts1 <= ts_created:
        assert ts_created - ts1 <= max_delta
    else:
        assert ts1 - ts_created <= max_delta
    sleep(2.5)
    ts2 = os_dependent_use(path, tz, fudge)
    assert ts2 is not None
    assert ts1 == ts2
    with open(Path(path) / 'file.txt', "w") as f:
        f.write(str(ts1))
    ts3 = os_dependent_use(path, tz, fudge)
    assert ts3 is not None
    if not fudge:
        assert ts1 == ts3
    else:
        assert ts1 <= ts3


@pytest.mark.parametrize('fudge', [True, False])
def test_birthtime_missing_file(fudge: bool):
    """Ensure a missing file raises an exception."""
    with pytest.raises(FileNotFoundError):
        file_birthtime('nonexistent_file', fudge=fudge)
