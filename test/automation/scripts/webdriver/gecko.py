# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

# -*- coding: utf-8 -*-
import requests
import os
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from scripts.utils.system import get_output
from scripts.webdriver.web_driver_manager import WebDriverManagerBase


class GeckoDriverManager(WebDriverManagerBase):
    """Class for downloading the Gecko (Mozilla Firefox) WebDriver."""

    __browser_name__ = 'Firefox'
    gecko_driver_releases_url = "https://api.github.com/repos/mozilla/geckodriver/releases/"
    fallback_url = "https://github.com/mozilla/geckodriver/releases/"

    driver_filenames = {
        "win": "geckodriver.exe",
        "mac": "geckodriver",
        "linux": "geckodriver",
    }

    firefox_version_pattern = r"(\d+)(\.\d+)"
    firefox_version_commands = {
        "win": [
            ["reg", "query", r"HKEY_LOCAL_MACHINE\Software\Mozilla\Mozilla Firefox",
                "/v", "CurrentVersion"],
            ["reg", "query", r"HKEY_CURRENT_USER\Software\Mozilla\Mozilla Firefox",
                "/v", "CurrentVersion"],
        ],
        "linux": [
            ["firefox", "--version", "--headless"],
        ],
        "mac": [
            ["/Applications/Firefox.app/Contents/MacOS/firefox-bin",
                "--version", "--headless"],
        ],
    }

    def get_download_path(self, version=None):
        version = self._parse_version(version if version else self.version)
        return os.path.join(self.download_root, self.__browser_name__, version)

    def get_download_url(self, version="latest"):
        """
        Method for getting the download URL for the Gecko (Mozilla Firefox) driver binary.

        :param version: String representing the version of the web driver binary to download.  For example, "v0.20.1".
                        Default if no version is specified is "latest".  The version string should match the version
                        as specified on the download page of the webdriver binary.
        :returns: The download URL for the Gecko (Mozilla Firefox) driver binary.
        """
        version = self._parse_version(version)
        releases_url = f"{self.gecko_driver_releases_url}tags/{version}"
        
        response = requests.get(releases_url, verify=False)
        if response.status_code == 200:
            url = self._parse_github_api_response(version, response)
        elif response.status_code == 403:
            url = self._parse_github_page(version)
        else:
            raise Exception(
                f"Error, unable to get info for gecko driver {version} release. Status code: {response.status_code}. Error message: {response.text}"  # NOQA: C812
            )
        return (url, os.path.split(urlparse(url).path)[1])

    def get_latest_version(self):
        return self._get_latest_version_with_github_page_fallback(self.gecko_driver_releases_url, self.fallback_url, "latest")

    def get_compatible_version(self):
        # Map browser version to webdriver version
        # https://firefox-source-docs.mozilla.org/testing/geckodriver/Support.html
        browser_version = self._get_browser_version()
        version_map = [(60, "v0.29.0"), (57, "v0.25.0"),
                       (55, "v0.20.1"), (53, "v0.18.0"), (52, "v0.17.0")]

        for browser_minimum, driver_version in version_map:
            if browser_version >= browser_minimum:
                return driver_version

        raise Exception(f"Unsupported Firefox version: {browser_version}")

    def _get_browser_version(self):
        commands = self.firefox_version_commands.get(self.os_name)
        if not commands:
            raise NotImplementedError("Unsupported system: %s", self.os_name)

        for cmd in commands:
            output = get_output(cmd)
            if not output:
                continue

            version = re.search(self.firefox_version_pattern, output)
            if not version:
                continue

            return int(version.group(1))

        raise Exception(
            "Error, browser version does not match known pattern")
    
    def _parse_github_api_response(self, version, response):
        filenames = [asset["name"] for asset in response.json()["assets"]]
        filename = [name for name in filenames if self.os_name in name]
        if not filename:
            raise Exception(f"Error, unable to find a download for os: {self.os_name}")

        if len(filename) > 1:
            filename = [name for name in filenames if self.os_name + self.bitness in name and not name.endswith(".asc")]
            if len(filename) != 1:
                raise Exception(f"Error, unable to determine correct filename for {self.bitness}bit {self.os_name}")

        filename = filename[0]

        url = response.json()["assets"][filenames.index(filename)]["browser_download_url"]
        return url
    
    def _parse_github_page(self, version):
        if version == "latest":
            release_url = f"{self.fallback_url}latest"
            matcher = r".*\/releases\/download\/.*{}".format(self.os_name)
        else:
            release_url = f"{self.fallback_url}tag/{version}"
            matcher = r".*\/releases\/download\/{}\/.*{}".format(version, self.os_name)

        response = requests.get(release_url)
        if response.status_code != 200:
            return None

        tree = BeautifulSoup(response.text, "html.parser")
        links = tree.find_all("a", href=re.compile(matcher))
        if len(links) == 2:
            matcher = f"{matcher}.*{self.bitness}"
            links = tree.find_all("a", href=re.compile(matcher))

        if links:
            return f"https://github.com{links[0]['href']}"

        return None
