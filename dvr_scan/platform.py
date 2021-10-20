# -*- coding: utf-8 -*-
#
#       DVR-Scan: Find & Export Motion Events in Video Footage
#   --------------------------------------------------------------
#     [  Site: https://github.com/Breakthrough/DVR-Scan/   ]
#     [  Documentation: http://dvr-scan.readthedocs.org/   ]
#
# This file contains all platform/library specific code, intended to improve
# compatibility of DVR-Scan with a wider array of software versions.
#
# Copyright (C) 2016-2021 Brandon Castellano <http://www.bcastell.com>.
#
# DVR-Scan is licensed under the BSD 2-Clause License; see the included
# LICENSE file or visit one of the following pages for details:
#  - https://github.com/Breakthrough/DVR-Scan/
#
# This software uses Numpy and OpenCV; see the LICENSE-NUMPY and
# LICENSE-OPENCV files or visit the above URL for details.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#

""" ``dvr_scan.platform`` Module

This file contains all platform/library/OS-specific compatibility fixes,
intended to improve the systems that are able to run DVR-Scan, and allow
for maintaining backwards compatibility with existing libraries going forwards.

For OpenCV 2.x, the scenedetect.platform module also makes a copy of the
OpenCV VideoCapture property constants from the cv2.cv namespace directly
to the cv2 namespace.  This ensures that the cv2 API is consistent
with those changes made to it in OpenCV 3.0 and above.

TODO: Replace with PySceneDetect's platform module to reduce code duplication
across both projects.
"""

# Third-Party Library Imports
import cv2

def cnt_is_available():
    try:
        return 'createBackgroundSubtractorCNT' in dir(cv2.bgsegm)
    except AttributeError:
        return False
