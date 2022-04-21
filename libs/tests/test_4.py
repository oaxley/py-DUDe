#!/usr/bin/env python3

#
# This unit will test the /users endpoint
#

import os
import time
import unittest

import pyDUDe


class UserTest(unittest.TestCase):

    def setUp(self) -> None:
        self.client = pyDUDe.Client()
        self.client.config.readFile()

        # remove the file
        try:
            os.unlink(os.environ['DUDE_SERVER_DATABASE'])
        except FileNotFoundError:
            pass

        # restart the server
        os.kill(int(os.environ['DUDE_SERVER_PID']), 1)
        time.sleep(float(os.environ['DUDE_SERVER_WAIT_TIME']))

    def test_create_user(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')
        usr = self.client.createUser(team_id=tid, name='John', email='john@acme.com')
        self.assertEqual(usr, 1)

    def test_create_user_duplicate(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')
        usr = self.client.createUser(team_id=tid, name='John', email='john@acme.com')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.createUser(team_id=tid, name='John', email='john@acme.com')

    def test_create_user_duplicate_two_team(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')

        tid1 = self.client.createTeam(unit_id=uid, name='Press')
        self.client.createUser(team_id=tid1, name='John', email='john@acme.com')

        tid2 = self.client.createTeam(unit_id=uid, name='Social Media')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.createUser(team_id=tid2, name='John', email='john@acme.com')

    def test_rename_user_name_no_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')

        tid1 = self.client.createTeam(unit_id=uid, name='Press')
        usr1 = self.client.createUser(team_id=tid1, name='John', email='john@acme.com')

        ret = self.client.updateSingleUser(user_id=usr1, name='John DOE')
        self.assertTrue(ret)

        values = self.client.getSingleUser(user_id=uid)
        self.assertEqual(values['name'], "John DOE")

    def test_rename_user_name_with_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')

        tid1 = self.client.createTeam(unit_id=uid, name='Press')
        usr1 = self.client.createUser(team_id=tid1, name='John', email='john@acme.com')
        usr2 = self.client.createUser(team_id=tid1, name='Sarah', email='Sarah@acme.com')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.updateSingleUser(user_id=usr2, name='John')

    def test_rename_user_email_no_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')

        tid1 = self.client.createTeam(unit_id=uid, name='Press')
        usr1 = self.client.createUser(team_id=tid1, name='John', email='john@acme.com')

        ret = self.client.updateSingleUser(user_id=usr1, email='john.doe@acme.com')
        self.assertTrue(ret)

        values = self.client.getSingleUser(user_id=usr1)
        self.assertEqual(values['email'], "john.doe@acme.com")

    def test_rename_user_email_with_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')

        tid1 = self.client.createTeam(unit_id=uid, name='Press')
        usr1 = self.client.createUser(team_id=tid1, name='John', email='john@acme.com')
        usr2 = self.client.createUser(team_id=tid1, name='Sarah', email='sarah@acme.com')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.updateSingleUser(user_id=usr2, email='john@acme.com')

    def test_move_user_between_teams_same_unit_same_company(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')

        tid1 = self.client.createTeam(unit_id=uid, name='Press')
        tid2 = self.client.createTeam(unit_id=uid, name='Social Media')

        usr = self.client.createUser(team_id=tid1, name='John', email='john@acme.com')

        ret = self.client.updateSingleUser(user_id=usr, team_id=tid2)
        self.assertTrue(ret)

        values = self.client.getSingleUser(user_id=usr)
        self.assertEqual(int(values['team_id']), tid2)

    def test_move_user_between_teams_different_units_same_company(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid1 = self.client.createUnit(company_id=cid, name='Marketing')
        uid2 = self.client.createUnit(company_id=cid, name='HR')

        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        tid2 = self.client.createTeam(unit_id=uid2, name='Social Media')

        usr1 = self.client.createUser(team_id=tid1, name='John', email='john@acme.com')
        self.client.updateSingleUser(user_id=usr1, team_id=tid2)

    def test_move_user_between_teams_different_units_different_company(self):
        cid1 = self.client.createCompany(name='ACME Corp')
        uid1 = self.client.createUnit(company_id=cid1, name='Marketing')
        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        usr1 = self.client.createUser(team_id=tid1, name='John', email='john@acme.com')

        cid2 = self.client.createCompany(name='Chicken Co.')
        uid2 = self.client.createUnit(company_id=cid2, name='HR')
        tid2 = self.client.createTeam(unit_id=uid2, name='Payroll')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.updateSingleUser(user_id=usr1, team_id=tid2)
