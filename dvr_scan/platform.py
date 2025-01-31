# -*- coding: utf-8 -*-
#
#      DVR-Scan: Video Motion Event Detection & Extraction Tool
#   --------------------------------------------------------------
#       [  Site: https://github.com/Breakthrough/DVR-Scan/   ]
#       [  Documentation: http://dvr-scan.readthedocs.org/   ]
#
# Copyright (C) 2014-2022 Brandon Castellano <http://www.bcastell.com>.
# PySceneDetect is licensed under the BSD 2-Clause License; see the
# included LICENSE file, or visit one of the above pages for details.
#
"""``dvr_scan.platform`` Module

Contains platform, library, or OS-specific compatibility helpers.
"""

import logging
import os
import subprocess
import sys
from typing import AnyStr, Optional

try:
    import screeninfo
except ImportError:
    screeninfo = None

from scenedetect.platform import get_and_create_path


def get_min_screen_bounds():
    """ Safely attempts to get the minimum screen resolution of all monitors
    using the `screeninfo` package. Returns the minimum of all monitor's heights
    and widths with 10% padding."""
    if screeninfo is not None:
        try:
            monitors = screeninfo.get_monitors()
            return (int(0.9 * min(m.height for m in monitors)),
                    int(0.9 * min(m.width for m in monitors)))
        except screeninfo.common.ScreenInfoError as ex:
            pass
    logging.getLogger('dvr_scan').warning("Unable to get screen resolution: %s", ex)
    return None


def is_ffmpeg_available(ffmpeg_path: AnyStr = 'ffmpeg'):
    """ Is ffmpeg Available: Gracefully checks if ffmpeg command is available.

    Returns:
        True if `ffmpeg` can be invoked, False otherwise.
    """
    ret_val = None
    try:
        ret_val = subprocess.call([ffmpeg_path, '-v', 'quiet'])
    except OSError:
        return False
    if ret_val is not None and ret_val != 1:
        return False
    return True


def init_logger(log_level: int = logging.INFO,
                show_stdout: bool = False,
                log_file: Optional[str] = None):
    """Initializes logging for DVR-SCan. The logger instance used is named 'dvr_scan'.
    By default the logger has no handlers to suppress output. All existing log handlers
    are replaced every time this function is invoked.

    Arguments:
        log_level: Verbosity of log messages. Should be one of [logging.INFO, logging.DEBUG,
            logging.WARNING, logging.ERROR, logging.CRITICAL].
        show_stdout: If True, add handler to show log messages on stdout (default: False).
        log_file: If set, add handler to dump log messages to given file path.
    """
    # Format of log messages depends on verbosity.
    format_str = '[DVR-Scan] %(message)s'
    if log_level == logging.DEBUG:
        format_str = '%(levelname)s: %(module)s.%(funcName)s(): %(message)s'
    # Get the named logger and remove any existing handlers.
    logger_instance = logging.getLogger('dvr_scan')
    logger_instance.handlers = []
    logger_instance.setLevel(log_level)
    # Add stdout handler if required.
    if show_stdout:
        handler = logging.StreamHandler(stream=sys.stdout)
        handler.setLevel(log_level)
        handler.setFormatter(logging.Formatter(fmt=format_str))
        logger_instance.addHandler(handler)
    # Add file handler if required.
    if log_file:
        log_file = get_and_create_path(log_file)
        handler = logging.FileHandler(log_file)
        handler.setLevel(log_level)
        handler.setFormatter(logging.Formatter(fmt=format_str))
        logger_instance.addHandler(handler)


def get_filename(path: AnyStr, include_extension: bool) -> AnyStr:
    """Get filename of the given path, optionally excluding extension."""
    filename = os.path.basename(path)
    if not include_extension:
        dot_position = filename.rfind('.')
        if dot_position > 0:
            filename = filename[:dot_position]
    return filename
