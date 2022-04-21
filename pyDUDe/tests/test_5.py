#!/usr/bin/env python3

#
# This unit will test the /software endpoint
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

    def test_create_software(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')
        sft = self.client.createSoftware(team_id=tid, name='StoryBuilder')

        self.assertEqual(sft, 1)

    def test_create_software_duplicate(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')
        tid = self.client.createTeam(unit_id=uid, name='Press')
        sft = self.client.createSoftware(team_id=tid, name='StoryBuilder')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.createSoftware(team_id=tid, name='StoryBuilder')

    def test_create_software_duplicate_two_teams(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')

        tid1 = self.client.createTeam(unit_id=uid, name='Press')
        sft1 = self.client.createSoftware(team_id=tid1, name='StoryBuilder')
        self.assertEqual(sft1, 1)

        tid2 = self.client.createTeam(unit_id=uid, name='Social Media')
        sft2 = self.client.createSoftware(team_id=tid2, name='StoryBuilder')
        self.assertEqual(sft2, 2)

    def test_rename_software_no_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')

        tid1 = self.client.createTeam(unit_id=uid, name='Press')
        sft1 = self.client.createSoftware(team_id=tid1, name='StoryBuilder')

        ret = self.client.updateSingleSoftware(software_id=sft1, name='StoryCreator')
        self.assertTrue(ret)

        values = self.client.getSingleSoftware(software_id=sft1)
        self.assertEqual(values['name'], 'StoryCreator')

    def test_rename_software_with_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid = self.client.createUnit(company_id=cid, name='Marketing')

        tid1 = self.client.createTeam(unit_id=uid, name='Press')
        sft1 = self.client.createSoftware(team_id=tid1, name='StoryBuilder')

        sft2 = self.client.createSoftware(team_id=tid1, name='StoryCreator')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.updateSingleSoftware(software_id=sft2, name='StoryBuilder')

    def test_move_soft_between_team_same_unit_same_company_no_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid1 = self.client.createUnit(company_id=cid, name='Marketing')
        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        tid2 = self.client.createTeam(unit_id=uid1, name='Brand')

        sft1 = self.client.createSoftware(team_id=tid1, name='StoryBuilder')
        ret = self.client.updateSingleSoftware(software_id=sft1, team_id=tid2)
        self.assertTrue(ret)

    def test_move_soft_between_team_same_unit_same_company_with_collision(self):
        cid = self.client.createCompany(name='ACME Corp')
        uid1 = self.client.createUnit(company_id=cid, name='Marketing')
        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        tid2 = self.client.createTeam(unit_id=uid1, name='Brand')

        sft1 = self.client.createSoftware(team_id=tid1, name='StoryBuilder')
        sft2 = self.client.createSoftware(team_id=tid2, name='StoryBuilder')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.updateSingleSoftware(software_id=sft1, team_id=tid2)

    def test_move_soft_between_team_different_unit_same_company_no_collision(self):
        cid = self.client.createCompany(name='ACME Corp')

        uid1 = self.client.createUnit(company_id=cid, name='Marketing')
        uid2 = self.client.createUnit(company_id=cid, name='HR')

        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        tid2 = self.client.createTeam(unit_id=uid2, name='Brand')

        sft1 = self.client.createSoftware(team_id=tid1, name='StoryBuilder')

        ret = self.client.updateSingleSoftware(software_id=sft1, team_id=tid2)
        self.assertTrue(ret)

    def test_move_soft_between_team_different_unit_same_company_with_collision(self):
        cid = self.client.createCompany(name='ACME Corp')

        uid1 = self.client.createUnit(company_id=cid, name='Marketing')
        uid2 = self.client.createUnit(company_id=cid, name='HR')

        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        tid2 = self.client.createTeam(unit_id=uid2, name='Brand')

        sft1 = self.client.createSoftware(team_id=tid1, name='StoryBuilder')
        sft2 = self.client.createSoftware(team_id=tid2, name='StoryBuilder')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.updateSingleSoftware(software_id=sft1, team_id=tid2)

    def test_move_soft_between_team_different_unit_different_company(self):
        cid1 = self.client.createCompany(name='ACME Corp')
        uid1 = self.client.createUnit(company_id=cid1, name='Marketing')
        tid1 = self.client.createTeam(unit_id=uid1, name='Press')
        sft1 = self.client.createSoftware(team_id=tid1, name='StoryBuilder')

        cid2 = self.client.createCompany(name='Chicken')
        uid2 = self.client.createUnit(company_id=cid2, name='HR')
        tid2 = self.client.createTeam(unit_id=uid2, name='Brand')
        sft2 = self.client.createSoftware(team_id=tid2, name='StoryBuilder')

        with self.assertRaises(pyDUDe.exceptions.BadRequest):
            self.client.updateSingleSoftware(software_id=sft2, team_id=tid1)
