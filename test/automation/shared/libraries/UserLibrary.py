# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from robot.api import logger


class UserLibrary:
    def example_python_keyword(self):
        logger.info("This is Python from Shared library!")
