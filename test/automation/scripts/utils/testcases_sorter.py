# SPDX-FileCopyrightText: 2023 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from collections import defaultdict
import re
import sys

module_list = [
    'HomePage'
]

modules = dict()
current_case = list()
current_case_module = None
with open(sys.argv[1], 'r', encoding='utf-8') as file:
    for line in file.readlines():
        if line.startswith('#'):
            continue

        if line.strip() and not re.match(r'^\s+.+$', line):
            if len(current_case):
                modules[current_case_module] = [
                    *modules.get(current_case_module, []), current_case]
            current_case_module = "Uncategorized"
            current_case = list([line])
        else:
            current_case.append(line)
            if line.strip().startswith('[Tags]'):
                current_case_module = next(
                    (name for name in module_list if name.lower() in line.lower()), None)
    file.close()

with open('data.csv', 'w+', encoding='utf-8') as file:
    for module, testcases in modules.items():
        for case in testcases:
            name = re.sub(r'\r?\n', '', case[0])
            file.write(f"{name},{module}\n")
    file.close()
