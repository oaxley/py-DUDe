#!/usr/bin/env python3

#
# This unit will test the /units endpoint
#

import os
import time
import unittest

import pyDUDe


class UnitTest(unittest.TestCase):

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

    def test_create_unit(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        self.assertEqual(uid, 1)

    def test_create_unit_duplicate(self):
        cid = self.client.createCompany(name='ACME Corp')
        self.client.createUnit(company_id=cid, name='Marketing')
        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.createUnit(company_id=cid, name='Marketing')

    def test_create_unit_duplicate_two_companies(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        self.assertEqual(uid, 1)

        cid = self.client.createCompany(name='Chicken Co.')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        self.assertEqual(uid, 2)

    def test_rename_unit_no_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        ret = self.client.updateSingleUnit(unit_id=uid, name='HR')
        self.assertTrue(ret)

    def test_rename_unit_with_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        self.client.createUnit(company_id=cid, name='Marketing')

        uid = self.client.createUnit(company_id=cid, name='HR')
        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.updateSingleUnit(unit_id=uid, name='Marketing')

    def test_create_unit_team_no_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createUnitTeam(unit_id=uid, name='Press')
        self.assertEqual(tid, 1)

    def test_create_unit_team_with_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        self.client.createUnitTeam(unit_id=uid, name='Press')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.createUnitTeam(unit_id=uid, name='Press')
