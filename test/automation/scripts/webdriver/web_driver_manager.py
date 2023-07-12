# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

# -*- coding: utf-8 -*-

import re
import abc
import sys
import shutil
import urllib3
import tarfile
import gzip
import zipfile
import platform
import requests
import os
from pathlib import Path

class WebDriverManagerBase:
    """Abstract Base Class for the different web driver downloaders"""

    __metaclass__ = abc.ABCMeta
    __browser_name__ = 'Generic'
    fallback_url = None
    driver_filenames = None
    bitness = '64'

    def __init__(self, webdriver_root, version=None, bitness=None):
        """
        Initializer for the class.  Accepts two optional parameters.

        :param download_root: Path where the web driver binaries will be downloaded.  If running as root in macOS or
                              Linux, the default will be '/usr/local/webdriver', otherwise python appdirs module will
                              be used to determine appropriate location if no value given.
        :param link_path: Path where the link to the web driver binaries will be created.  If running as root in macOS
                          or Linux, the default will be 'usr/local/bin', otherwise appdirs python module will be used
                          to determine appropriate location if no value give. If set "AUTO", link will be created into
                          first writeable directory in PATH. If set "SKIP", no link will be created.
        """
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        self.os_name = self.get_os_name()
        self.download_root = webdriver_root
        self.version = version if version else self.get_compatible_version()
        if not bitness:
            self.bitness = "64" if sys.maxsize > 2 ** 32 else "32"  # noqa: KEK100
        else:
            self.bitness = bitness


    def get_os_name(self):
        platform_name = platform.system()
        namelist = {"Darwin": "mac", "Windows": "win", "Linux": "linux"}
        if "CYGWIN" in platform_name:
            return "win"

        return namelist[platform_name]

    @abc.abstractmethod
    def get_download_path(self, version="latest"):
        """
        Method for getting the download path for a web driver binary.

        :param version: String representing the version of the web driver binary to download.  For example, "2.38".
                        Default if no version is specified is "latest".  The version string should match the version
                        as specified on the download page of the webdriver binary.

        :returns: The download path of the web driver binary.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_download_url(self, version="latest"):
        """
        Method for getting the download URL for a web driver binary.

        :param version: String representing the version of the web driver binary to download.  For example, "2.38".
                        Default if no version is specified is "latest".  The version string should match the version
                        as specified on the download page of the webdriver binary.
        :returns: The download URL for the web driver binary.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_latest_version(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get_compatible_version(self):
        raise NotImplementedError

    def get_driver_filename(self):
        return self.driver_filenames[self.os_name]

    def _parse_version(self, version):
        method = version.strip().lower()

        # Attempt to match webdriver to current browser version, if supported
        if method == "compatible":
            try:
                return self.get_compatible_version()
            except NotImplementedError:
                pass
            except Exception as exc:
                raise Exception("Failed to parse compatible version: %s", exc)
            method = "latest"

        if method == "latest":
            return self.get_latest_version()
        else:
            return version

    def download(self, download_path, version):
        (download_url, filename) = self.get_download_url(version)

        print('Downloading {} webdriver version {}'.format(self.__browser_name__, version))

        if not os.path.exists(download_path):
            os.makedirs(download_path)

        filename_with_path =  os.path.join(download_path, filename)

        data = requests.get(download_url, stream=True, verify=False)

        if data.status_code == 200:
            with open(filename_with_path, mode="wb") as fileobj:
                chunk_size = 1024
                for chunk in data.iter_content(chunk_size):
                        fileobj.write(chunk)
            return filename_with_path, filename

        raise Exception(f"Error downloading file {filename}, got status code: {data.status_code}")
        return None

    @staticmethod
    def _generate_archive_details(dl_path, filename):
        if filename.lower().endswith(".tar.gz"):
            return (os.path.join(dl_path), 1)
        elif filename.lower().endswith(".zip"):
            return (os.path.join(dl_path), 2)
        elif filename.lower().endswith(".exe"):
            return (os.path.join(dl_path), 3)
        else:
            (f"Unknown archive format: {filename}")

    def download_and_install(self):
        archive_type = 0
        downloaded_file_path = ""

        driver_filename = self.get_driver_filename()
        download_path = self.get_download_path()

        if driver_filename is None:
            raise Exception(f"Error, unable to find appropriate drivername for {self.os_name}.")

        for _ in range(0, 2):
            downloaded_file_path, filename = self.download(version=self.version, download_path=download_path)

            (extract_dir, archive_type) = self._generate_archive_details(download_path, filename)

            if not os.path.exists(extract_dir):
                os.makedirs(extract_dir, exist_ok=True)

            try:
                if archive_type == 1:
                    with tarfile.open(downloaded_file_path, mode="r:*") as tar:
                        tar.extractall(extract_dir)
                elif archive_type == 2:
                    with zipfile.ZipFile(downloaded_file_path, mode="r") as driver_zipfile:
                        driver_zipfile.extractall(extract_dir)
                        # TODO: Get filenames and log debug
                elif archive_type == 3:
                    shutil.copy2(downloaded_file_path, extract_dir / filename)
                print('Webdriver saved as {}'.format(driver_filename))
            except (gzip.BadGzipFile, tarfile.TarError, zipfile.BadZipFile):
                continue
            break

        if downloaded_file_path != "":
            os.remove(downloaded_file_path)

        driver_path = os.path.join(download_path, driver_filename)
        if self.get_os_name() == 'linux':
            os.system(f'chmod +x {driver_path}')
        return driver_path