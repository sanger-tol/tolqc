# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from main import application
from flask_testing import TestCase

from main.model import db, TolqcUser, TolqcRole, TolqcAllocation, \
                       TolqcCentre, TolqcLibrary, TolqcLibraryType, \
                       TolqcPlatform, TolqcProject, TolqcRun, \
                       TolqcSample, TolqcSeq, TolqcSpecies, \
                       TolqcSpecimen


class BaseTestCase(TestCase):

    api_key = "AnyThingBecAuseThIsIsATEST567890"

    def setUp(self):
        self.maxDiff = None
        db.create_all()
        user1 = TolqcUser(id=100,
                          name="test_user_admin",
                          email="test_user_admin@sanger.ac.uk",
                          organisation="Sanger Institute",
                          api_key=self.api_key)
        db.session.add(user1)
        role = TolqcRole(role="admin")
        role.user = user1
        db.session.add(role)
        db.session.commit()

    def tearDown(self):
        db.session.query(TolqcRole).delete()
        db.session.query(TolqcUser).delete()
        db.session.query(TolqcAllocation).delete()
        db.session.query(TolqcCentre).delete()
        db.session.query(TolqcLibrary).delete()
        db.session.query(TolqcLibraryType).delete()
        db.session.query(TolqcPlatform).delete()
        db.session.query(TolqcProject).delete()
        db.session.query(TolqcRun).delete()
        db.session.query(TolqcSample).delete()
        db.session.query(TolqcSeq).delete()
        db.session.query(TolqcSpecies).delete()
        db.session.query(TolqcSpecimen).delete()
        db.session.commit()

    def create_app(self):
        return application()
