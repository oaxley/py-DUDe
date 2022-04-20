#!/usr/bin/env python3

#
# This unit will test the /companies endpoint
#

import os
import time
import unittest

import pyDUDe


class CompanyTest(unittest.TestCase):

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

        # wait for the server to start
        time.sleep(1)


    def test_create_company(self):
        cid = self.client.createCompany(name='ACME Corp')
        self.assertEqual(cid, 1)

    def test_create_company_duplicate(self):
        self.client.createCompany(name='ACME Corp')
        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.createCompany(name='ACME Corp')

    def test_rename_company_no_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        ret = self.client.updateSingleCompany(company_id=cid, name='Chicken Co.')
        self.assertTrue(ret)

    def test_rename_company_with_collision(self):
        cid1 = self.client.createCompany(name='ACME Corp')
        cid2 = self.client.createCompany(name='Chicken Co.')
        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.updateSingleCompany(company_id=cid2, name='ACME Corp')

    def test_create_company_unit_no_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createCompanyUnit(company_id=cid, name='Marketing')
        self.assertEqual(uid, 1)

    def test_create_company_unit_with_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createCompanyUnit(company_id=cid, name='Marketing')
        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.createCompanyUnit(company_id=cid, name='Marketing')
