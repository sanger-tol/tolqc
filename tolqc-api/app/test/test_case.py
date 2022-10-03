# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from flask_testing import TestCase as FlaskTestCase

from main.model import db, TolqcUser, TolqcRole, TolqcAllocation, \
                       TolqcCentre, TolqcLibrary, TolqcLibraryType, \
                       TolqcPlatform, TolqcProject, TolqcRun, \
                       TolqcSample, TolqcSpecies, TolqcSpecimen, \
                       TolqcData, TolqcFile, TolqcSex, \
                       TolqcSoftwareVersion, TolqcStatus, TolqcStatusDict, \
                       TolqcQcDict, TolqcMilestoneDict, TolqcAccession, \
                       TolqcAccessionTypeDict, TolqcDataset, TolqcSet, \
                       TolqcPacbioRunMetrics, TolqcAssembly, \
                       TolqcAssemblyComponent, TolqcGenomescopeMetrics, \
                       TolqcAssemblyMetrics, TolqcBuscoLineage, \
                       TolqcBuscoMetrics, TolqcMerquryMetrics

from test.base.models import A_ModelRelationship, B_ModelRelationship, \
                             C_ModelWithNullableColumn, \
                             D_ModelWithNonNullableColumn, \
                             E_ModelRelationship, F_ModelWithExtField, \
                             G_ModelWithFilterableFields, \
                             H_ModelLog, I_ModelEnum, J_ModelEnumDependent


class TestCase(FlaskTestCase):

    api_key_1 = "AnyThingBecAuseThIsIsATEST567890"
    api_key_2 = "SomethingElse"

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
                          api_key=self.api_key_1)
        db.session.add(user1)
        role_admin = TolqcRole(role="admin")
        role_admin.user = user1
        db.session.add(role_admin)

        user2 = TolqcUser(id=101,
                          name="test_user_other",
                          email="test_user_other@sanger.ac.uk",
                          organisation="Sanger Institute",
                          api_key=self.api_key_2)
        db.session.add(user2)
        role_other = TolqcRole(role="other")
        role_other.user = user2
        db.session.add(role_other)

    def tearDown(self):
        db.session.rollback()

        # base models
        db.session.query(E_ModelRelationship).delete()
        db.session.query(B_ModelRelationship).delete()
        db.session.query(A_ModelRelationship).delete()
        db.session.query(C_ModelWithNullableColumn).delete()
        db.session.query(D_ModelWithNonNullableColumn).delete()
        db.session.query(F_ModelWithExtField).delete()
        db.session.query(G_ModelWithFilterableFields).delete()
        db.session.query(H_ModelLog).delete()
        db.session.query(J_ModelEnumDependent).delete()
        db.session.query(I_ModelEnum).delete()

        # ToLQC models
        # TODO delete this all by cascade
        db.session.query(TolqcMerquryMetrics).delete()
        db.session.query(TolqcBuscoMetrics).delete()
        db.session.query(TolqcBuscoLineage).delete()
        db.session.query(TolqcAssemblyMetrics).delete()
        db.session.query(TolqcAssembly).delete()
        db.session.query(TolqcGenomescopeMetrics).delete()
        db.session.query(TolqcSoftwareVersion).delete()
        db.session.query(TolqcSet).delete()
        db.session.query(TolqcDataset).delete()
        db.session.query(TolqcData).delete()
        db.session.query(TolqcPacbioRunMetrics).delete()
        db.session.query(TolqcRun).delete()
        db.session.query(TolqcFile).delete()
        db.session.query(TolqcLibrary).delete()
        db.session.query(TolqcCentre).delete()
        db.session.query(TolqcPlatform).delete()
        db.session.query(TolqcLibraryType).delete()
        db.session.query(TolqcSample).delete()
        db.session.query(TolqcAllocation).delete()
        db.session.query(TolqcSpecimen).delete()
        db.session.query(TolqcSex).delete()
        db.session.query(TolqcSpecies).delete()
        db.session.query(TolqcProject).delete()
        db.session.query(TolqcAccessionTypeDict).delete()
        db.session.query(TolqcAccession).delete()
        db.session.query(TolqcAssemblyComponent).delete()
        db.session.query(TolqcStatus).delete()
        db.session.query(TolqcStatusDict).delete()
        db.session.query(TolqcMilestoneDict).delete()
        db.session.query(TolqcQcDict).delete()
        db.session.query(TolqcRole).delete()
        db.session.query(TolqcUser).delete()
        db.session.commit()

    def assert201(self, response, *args):
        self.assertEqual(response.status_code, 201)
