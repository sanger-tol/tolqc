# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

import pytest

from test.core import BaseTestCase

from main.resource.base import BaseNamespace, \
                                BaseDetailResource, \
                                MissingResourceClassVariableException


class ResourceDeclarationTest(BaseTestCase):
    def test_missing_class_variables(self):
        class ResourceMissingClassVariables(BaseDetailResource):
            pass
        namespace = BaseNamespace('test')
        with pytest.raises(MissingResourceClassVariableException):
            namespace.add_resource(ResourceMissingClassVariables)
