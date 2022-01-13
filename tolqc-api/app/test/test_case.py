# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_testing import TestCase as FlaskTestCase

from main.model import db, TolqcUser, TolqcRole, TolqcAllocation, \
                       TolqcCentre, TolqcLibrary, TolqcLibraryType, \
                       TolqcPlatform, TolqcProject, TolqcRun, \
                       TolqcSample, TolqcSeq, TolqcSpecies, \
                       TolqcSpecimen
from test.base.models import A_ModelRelationship, B_ModelRelationship, \
                             C_ModelWithNullableColumn, \
                             D_ModelWithNonNullableColumn, \
                             E_ModelRelationship, F_ModelWithExtField


class TestCase(FlaskTestCase):

    api_key = "AnyThingBecAuseThIsIsATEST567890"

    def setUp(self):
        # general
        self.maxDiff = None
        db.create_all()
        db.session.commit()

        # ToLQC tests
        user1 = TolqcUser(id=100,
                          name="test_user_admin",
                          email="test_user_admin@sanger.ac.uk",
                          organisation="Sanger Institute",
                          api_key=self.api_key)
        db.session.add(user1)
        role = TolqcRole(role="admin")
        role.user = user1
        db.session.add(role)

    def tearDown(self):
        db.session.rollback()

        # base models
        db.session.query(E_ModelRelationship).delete()
        db.session.query(B_ModelRelationship).delete()
        db.session.query(A_ModelRelationship).delete()
        db.session.query(C_ModelWithNullableColumn).delete()
        db.session.query(D_ModelWithNonNullableColumn).delete()
        db.session.query(F_ModelWithExtField).delete()

        # ToLQC models
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
        db.session.query(TolqcRole).delete()
        db.session.query(TolqcUser).delete()

        db.session.commit()

    def assert201(self, response, *args):
        self.assertEqual(response.status_code, 201)
