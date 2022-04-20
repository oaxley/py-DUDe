#!/usr/bin/env python3

#
# This unit will test the /teams endpoint
#

import os
import time
import unittest

import pyDUDe


class TeamTest(unittest.TestCase):

    def setUp(self) -> None:
        self.client = pyDUDe.Client()
        self.client.config.hostname = 'localhost'
        self.client.config.root_ca = '../certs/root/root_ca.cert.pem'
        self.client.config.x_api_token = 'my-secret-key'

        # remove the file
        try:
            os.unlink(os.environ['DUDE_SERVER_DATABASE'])
        except FileNotFoundError:
            pass

        # restart the server
        os.kill(int(os.environ['DUDE_SERVER_PID']), 1)

        time.sleep(1)

    def test_create_team(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')
        self.assertEqual(tid, 1)

    def test_create_team_duplicate(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')
        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.createTeam(unit_id=uid, name='Press')

    def test_create_team_duplicate_two_unit(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')
        self.assertEqual(tid, 1)

        uid = self.client.createUnit(company_id=cid, name='HR')
        tid = self.client.createTeam(unit_id=uid, name='Press')
        self.assertEqual(tid, 2)

    def test_rename_team_no_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')
        ret = self.client.updateSingleTeam(team_id=tid, name='Social Media')
        self.assertTrue(ret)

    def test_rename_team_with_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        self.client.createTeam(unit_id=uid, name='Press')

        tid = self.client.createTeam(unit_id=uid, name='Social Media')
        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.updateSingleTeam(team_id=tid, name='Press')

    def test_move_team_between_unit_same_company_no_collision(self):
        cid = self.client.createCompany(name='ACME Corp')

        uid1 = self.client.createUnit(company_id=cid, name='Marketing')
        uid2 = self.client.createUnit(company_id=cid, name='HR')

        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        tid2 = self.client.createTeam(unit_id=uid2, name='Brand')

        ret = self.client.updateSingleTeam(team_id=tid2, unit_id=uid1)
        self.assertTrue(ret)

    def test_move_team_between_unit_same_company_with_collision(self):
        cid = self.client.createCompany(name='ACME Corp')

        uid1 = self.client.createUnit(company_id=cid, name='Marketing')
        uid2 = self.client.createUnit(company_id=cid, name='HR')

        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        tid2 = self.client.createTeam(unit_id=uid2, name='Press')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.updateSingleTeam(team_id=tid2, unit_id=uid1)

    def test_move_team_between_unit_different_company(self):
        cid1 = self.client.createCompany(name='ACME Corp')
        cid2 = self.client.createCompany(name='Chicken Co.')

        uid1 = self.client.createUnit(company_id=cid1, name='Marketing')
        uid2 = self.client.createUnit(company_id=cid2, name='HR')

        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        tid2 = self.client.createTeam(unit_id=uid2, name='Brand')

        with self.assertRaises(pyDUDe.exceptions.NotFound):
            self.client.updateSingleTeam(team_id=tid2, unit_id=uid1)

    def test_create_team_user_no_collision(self):
        cid1 = self.client.createCompany(name='ACME Corp')
        uid1 = self.client.createUnit(company_id=cid1, name='Marketing')
        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        usr1 = self.client.createTeamUser(team_id=tid1, name='John', email='John@acme.com')

        self.assertEqual(usr1, 1)

    def test_create_team_user_collision(self):
        cid1 = self.client.createCompany(name='ACME Corp')
        uid1 = self.client.createUnit(company_id=cid1, name='Marketing')
        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        usr1 = self.client.createTeamUser(team_id=tid1, name='John', email='John@acme.com')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.createTeamUser(team_id=tid1, name='John', email='John@acme.com')

    def test_create_team_right_no_collision(self):
        cid1 = self.client.createCompany(name='ACME Corp')
        uid1 = self.client.createUnit(company_id=cid1, name='Marketing')
        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        rgh1 = self.client.createTeamRight(team_id=tid1, name='read')

        self.assertEqual(rgh1, 1)

    def test_create_team_right_collision(self):
        cid1 = self.client.createCompany(name='ACME Corp')
        uid1 = self.client.createUnit(company_id=cid1, name='Marketing')
        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        rgh1 = self.client.createTeamRight(team_id=tid1, name='read')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.createTeamRight(team_id=tid1, name='read')

    def test_create_team_soft_no_collision(self):
        cid1 = self.client.createCompany(name='ACME Corp')
        uid1 = self.client.createUnit(company_id=cid1, name='Marketing')
        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        sft1 = self.client.createTeamSoftware(team_id=tid1, name='StoryBuilder')

        self.assertEqual(sft1, 1)

    def test_create_team_soft_collision(self):
        cid1 = self.client.createCompany(name='ACME Corp')
        uid1 = self.client.createUnit(company_id=cid1, name='Marketing')
        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        sft1 = self.client.createTeamSoftware(team_id=tid1, name='StoryBuilder')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.createTeamSoftware(team_id=tid1, name='StoryBuilder')
