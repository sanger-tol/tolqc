# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import logging
import subprocess
import sys

def get_output(cmd, **kwargs):
    try:
        output = subprocess.check_output(cmd, **kwargs, stderr=subprocess.STDOUT)
        return output.decode().strip()
    except subprocess.CalledProcessError as err:
        error = err.output.decode().strip()
        return None
    except FileNotFoundError as err:
        return None