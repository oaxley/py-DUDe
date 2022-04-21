#!/usr/bin/env python3

#
# This unit will test the /user-rights endpoint
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

    def test_create_userright(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')

        usr = self.client.createUser(team_id=tid, name='John', email='john@acme.com')
        rgt = self.client.createRight(team_id=tid, name='read')

        ret = self.client.createUserRight(user_id=usr, right_id=rgt)
        self.assertEqual(ret, 1)

    def test_create_userright_unkown_user(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')

        rgt = self.client.createRight(team_id=tid, name='read')

        with self.assertRaises(pyDUDe.exceptions.NotFound):
            ret = self.client.createUserRight(user_id=1, right_id=rgt)

    def test_create_userright_unkown_right(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')

        usr = self.client.createUser(team_id=tid, name='John', email='john@acme.com')

        with self.assertRaises(pyDUDe.exceptions.NotFound):
            self.client.createUserRight(user_id=usr, right_id=1)

    def test_create_userright_duplicate(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')

        usr = self.client.createUser(team_id=tid, name='John', email='john@acme.com')
        rgt = self.client.createRight(team_id=tid, name='read')

        ret = self.client.createUserRight(user_id=usr, right_id=rgt)
        self.assertEqual(ret, 1)

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.createUserRight(user_id=usr, right_id=rgt)

    def test_update_userright_with_unknown_user(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')

        usr = self.client.createUser(team_id=tid, name='John', email='john@acme.com')
        rgt = self.client.createRight(team_id=tid, name='read')

        ret = self.client.createUserRight(user_id=usr, right_id=rgt)

        with self.assertRaises(pyDUDe.exceptions.NotFound):
            self.client.updateSingleUserRight(userright_id=ret, user_id=10)

    def test_update_userright_with_unknown_right(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')

        usr = self.client.createUser(team_id=tid, name='John', email='john@acme.com')
        rgt = self.client.createRight(team_id=tid, name='read')

        ret = self.client.createUserRight(user_id=usr, right_id=rgt)

        with self.assertRaises(pyDUDe.exceptions.NotFound):
            self.client.updateSingleUserRight(userright_id=ret, right_id=10)

    def test_update_userright_user_different_team(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')

        tid1 = self.client.createTeam(unit_id=uid, name='Press')
        usr1 = self.client.createUser(team_id=tid1, name='John', email='john@acme.com')
        rgt1 = self.client.createRight(team_id=tid1, name='read')
        ret1 = self.client.createUserRight(user_id=usr1, right_id=rgt1)

        tid2 = self.client.createTeam(unit_id=uid, name='HR')
        usr2 = self.client.createUser(team_id=tid2, name='Sarah', email='sarah@acme.com')
        rgt2 = self.client.createRight(team_id=tid2, name='write')
        ret2 = self.client.createUserRight(user_id=usr2, right_id=rgt2)

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.updateSingleUserRight(userright_id=ret2, user_id=usr1)

    def test_update_userright_right_different_team(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')

        tid1 = self.client.createTeam(unit_id=uid, name='Press')
        usr1 = self.client.createUser(team_id=tid1, name='John', email='john@acme.com')
        rgt1 = self.client.createRight(team_id=tid1, name='read')
        ret1 = self.client.createUserRight(user_id=usr1, right_id=rgt1)

        tid2 = self.client.createTeam(unit_id=uid, name='HR')
        usr2 = self.client.createUser(team_id=tid2, name='Sarah', email='sarah@acme.com')
        rgt2 = self.client.createRight(team_id=tid2, name='write')
        ret2 = self.client.createUserRight(user_id=usr2, right_id=rgt2)

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.updateSingleUserRight(userright_id=ret2, right_id=rgt1)

