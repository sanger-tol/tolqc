# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

# -*- coding: utf-8 -*-
from sys import prefix
import requests
import re
import os
from bs4 import BeautifulSoup
from pathlib import Path
from scripts.utils.system import get_output
from scripts.webdriver.web_driver_manager import WebDriverManagerBase

class EdgeChromiumDriverManager(WebDriverManagerBase):
    """Class for downloading Edge Chromium WebDriver."""
    __browser_name__ = 'Edge'
    edgechromium_driver_base_url = (
        "https://msedgedriver.azureedge.net/"
    )
    edgechromium_driver_base_download_url = (
        "https://msedgewebdriverstorage.blob.core.windows.net"
    )
    _drivers = None
    _versions = None
    driver_filenames = {
        "win": "msedgedriver.exe",
        "mac": "msedgedriver",
        "linux": "msedgedriver",
    }
    edge_version_pattern = r"(\d+\.\d+\.\d+\.\d+)"
    edge_version_commands = {
        "win": [
            ["reg", "query", r"HKEY_CURRENT_USER\Software\Microsoft\Edge\BLBeacon", "/v", "version"],
        ],
        "linux": [
            ["edge", "--version"],
        ],
        "mac": [
            [r'/Applications/Microsoft\ Edge.app/Contents/MacOS/Microsoft\ Edge --version'],
        ],
    }

    def versiontuple(self, v):
        return tuple(map(int, (v.split("."))))

    def get_download_path(self, version="latest"):
        version = self._parse_version(version)
        return os.path.join(self.download_root, self.__browser_name__, version)

    def get_download_url(self, version="latest"):
        """
        Method for getting the download URL for the Google Chome driver binary.

        :param version: String representing the version of the web driver binary to download.  For example, "2.39".
                        Default if no version is specified is "latest".  The version string should match the version
                        as specified on the download page of the webdriver binary.
        :returns: The download URL for the Internet Explorer driver binary.
        """
        version = self._parse_version(version)

        file_name = f'edgedriver_{self.os_name}{self.bitness}.zip'
        url = f'{self.edgechromium_driver_base_download_url}/edgewebdriver/{version}/{file_name}'
        return (url, file_name)

    def get_latest_version(self):
        resp = requests.get(self.edgechromium_driver_base_url + 'LATEST_STABLE')
        if resp.status_code == 200:
            return resp.text.rstrip()
        else:
            raise Exception('Unable to find lastest driver version for Edge')

    def get_compatible_version(self):
        return self._get_browser_version()

    def _get_browser_version(self):
        commands = self.edge_version_commands.get(self.os_name)
        if not commands:
            raise NotImplementedError("Unsupported system: %s", self.os_name)

        for cmd in commands:
            output = get_output(cmd)
            if not output:
                continue

            version = re.search(self.edge_version_pattern, output)
            if not version:
                continue

            return version.group(1)

        raise RuntimeError("Unable to find Edge on this system, please install it first!")