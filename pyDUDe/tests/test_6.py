#!/usr/bin/env python3

#
# This unit will test the /rights endpoint
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

    def test_create_right(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')
        rgt = self.client.createRight(team_id=tid, name='read')

        self.assertEqual(rgt, 1)

    def test_create_right_duplicate(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')
        rgt = self.client.createRight(team_id=tid, name='read')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.createRight(team_id=tid, name='read')

    def test_create_right_duplicate_two_teams(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')

        tid1 = self.client.createTeam(unit_id=uid, name='Press')
        rgt1 = self.client.createRight(team_id=tid1, name='read')
        self.assertEqual(rgt1, 1)

        tid2 = self.client.createTeam(unit_id=uid, name='Social Media')
        rgt2 = self.client.createRight(team_id=tid2, name='read')
        self.assertEqual(rgt2, 2)

    def test_rename_right_no_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')

        tid1 = self.client.createTeam(unit_id=uid, name='Press')
        rgt1 = self.client.createRight(team_id=tid1, name='read')

        ret = self.client.updateSingleRight(right_id=rgt1, name='write')
        self.assertTrue(ret)

        values = self.client.getSingleRight(right_id=rgt1)
        self.assertEqual(values['name'], 'write')

    def test_rename_right_with_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')

        tid1 = self.client.createTeam(unit_id=uid, name='Press')
        rgt1 = self.client.createRight(team_id=tid1, name='read')

        rgt2 = self.client.createRight(team_id=tid1, name='write')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.updateSingleRight(right_id=rgt2, name='read')
