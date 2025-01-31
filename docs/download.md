
<h1>Obtaining DVR-Scan</h1>

DVR-Scan is completely free software, and can be downloaded from the links below.  See the [license and copyright information](copyright.md) page for details.  If you have trouble running DVR-Scan, ensure that you have all the required dependencies listed on the [Installing & Updating](guide/installing.md) page.

**Important:** The minimum required Python version for DVR-Scan is now 3.7.  DVR-Scan v1.4 was the last release compatible with both Python 2 and 3.

------------------------------------------------

## Download and Installation

### Install via pip &nbsp; <span class="wy-text-neutral"><span class="fa fa-windows"></span> &nbsp; <span class="fa fa-linux"></span> &nbsp; <span class="fa fa-apple"></span></span></h3>

<div class="important">
<h4 class="wy-text-neutral"><span class="fa fa-angle-double-down wy-text-info"></span> Including OpenCV (recommended):</h4>
<h3 class="wy-text-neutral"><tt>pip install --upgrade dvr-scan[opencv]</tt></h3>
<h4 class="wy-text-neutral"><span class="fa fa-angle-down wy-text-info"></span> Including Headless OpenCV (servers):</h4>
<h3 class="wy-text-neutral"><tt>pip install --upgrade dvr-scan[opencv-headless]</tt></h3>
</div>

DVR-Scan is available via `pip` as [the `dvr-scan` package](https://pypi.org/project/dvr-scan/).


### Windows Build (64-bit Only) &nbsp; <span class="wy-text-neutral"><span class="fa fa-windows"></span></span>

<div class="important">
<h3 class="wy-text-neutral"><span class="fa fa-forward wy-text-info"></span> Latest Release: <b class="wy-text-neutral">v1.5.1</b></h3>
<h4 class="wy-text-neutral"><span class="fa fa-calendar wy-text-info"></span>&nbsp; Release Date:&nbsp; <b>August 15, 2022</b></h4>
<a href="https://github.com/Breakthrough/DVR-Scan/releases/download/v1.5.1-release/dvr-scan-1.5.1-win64.msi" class="btn btn-info" style="margin-bottom:8px;" role="button"><span class="fa fa-download"></span>&nbsp; <b>Installer MSI</b></a> &nbsp;&nbsp;&nbsp;&nbsp; <a href="https://github.com/Breakthrough/DVR-Scan/releases/download/v1.5.1-release/dvr-scan-1.5.1-win64.zip" class="btn btn-info" style="margin-bottom:8px;" role="button"><span class="fa fa-download"></span>&nbsp; <b>Portable ZIP</b></a> &nbsp;&nbsp;&nbsp;&nbsp; <a href="https://github.com/Breakthrough/DVR-Scan/releases/download/v1.5.1-release/dvr-scan-1.5.1-win64-cuda.zip" class="btn btn-info" style="margin-bottom:8px;" role="button"><span class="fa fa-download"></span>&nbsp; <b>Nvidia CUDA® Build (Experimental)</b></a> &nbsp;&nbsp;&nbsp;&nbsp; <a href="../guide/quickstart/" class="btn btn-success" style="margin-bottom:8px;" role="button"><span class="fa fa-book"></span>&nbsp; <b>Getting Started</b></a>
</div>

Due to a change in the installer format, you must uninstall previous versions of DVR-Scan before installing v1.5.1.  Windows builds including Nvidia CUDA® support require a GTX 900-series or higher GPU.  These builds are still experimental, and are not code signed.

### Python Distribution &nbsp; <span class="wy-text-neutral"><span class="fa fa-windows"></span> &nbsp; <span class="fa fa-linux"></span> &nbsp; <span class="fa fa-apple"></span></span>

<div class="important">
<h4 class="wy-text-neutral"><span class="fa fa-forward wy-text-info"></span> Latest Release: <b class="wy-text-neutral">v1.5.1</b></h4>
<h4 class="wy-text-neutral"><span class="fa fa-calendar wy-text-info"></span>&nbsp; Release Date:&nbsp; <b>August 15, 2022</b></h4>
<a href="https://github.com/Breakthrough/DVR-Scan/releases/download/v1.5.1-release/dvr_scan-1.5.1-py3-none-any.whl" class="btn btn-info" style="margin-bottom:8px;" role="button"><span class="fa fa-download"></span>&nbsp; <b>Wheel</b>&nbsp;&nbsp;.whl</a> &nbsp;&nbsp;&nbsp;&nbsp; <a href="https://github.com/Breakthrough/DVR-Scan/releases/download/v1.5.1-release/dvr-scan-1.5.1.tar.gz" class="btn btn-info" style="margin-bottom:8px;" role="button"><span class="fa fa-download"></span>&nbsp; <b>Source</b>&nbsp;&nbsp;.tar.gz</a> &nbsp;&nbsp;&nbsp;&nbsp; <a href="../guide/quickstart/" class="btn btn-success" style="margin-bottom:8px;" role="button"><span class="fa fa-book"></span>&nbsp; <b>Getting Started</b></a>
</div>

To install from source, download and extract the latest release to a location of your choice, and make sure you have the appropriate [system requirements](guide/installing.md) installed before continuing.  DVR-Scan can be built by running the following command:

```md
python -m build
```

DVR-Scan can then be installed from the built package using `pip`.

See the section [Installing & Updating](guide/installing.md) for instructions on installing DVR-Scan and the required system dependencies.  The source distribution is the recommended download for Linux and Mac users.  Although source installation is possible on Windows, the installer and portable versions are the recommended downloads for Windows users, as all required dependencies come bundled with these distributions.

### Code Signing Policy

Windows EXE/MSI Builds: Free code signing provided by [SignPath.io](https://signpath.io/), certificate by [SignPath Foundation](https://signpath.org/).
