#! /usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests for all Marvin actions
"""

import json
import re
import unittest

import marvin_actions

class ActionTest(unittest.TestCase):
    """Test Marvin actions"""
    strings = {}

    @classmethod
    def setUpClass(cls):
        with open("marvin_strings.json", encoding="utf-8") as f:
            cls.strings = json.load(f)


    def assertActionOutput(self, action, message, expectedOutput):
        """Call an action on message and assert expected output"""
        row = re.sub('[,.?:]', ' ', message).strip().lower().split()

        actualOutput = action(set(row), row, message)

        self.assertEqual(actualOutput, expectedOutput)


    def assertActionSilent(self, action, message):
        """Call an action with provided message and assert no output"""
        self.assertActionOutput(action, message, None)


    def assertStringsOutput(self, action, message, expectedoutputKey, subkey=None):
        """Call an action with provided message and assert the output is equal to DB"""
        if subkey:
            expectedOutput = self.strings.get(expectedoutputKey).get(subkey)
        else:
            expectedOutput = self.strings.get(expectedoutputKey)

        self.assertActionOutput(action, message, expectedOutput)


    def testWhois(self):
        """Test that marvin responds to whois"""
        self.assertStringsOutput(marvin_actions.marvinWhoIs, "vem är marvin?", "whois")
        self.assertActionSilent(marvin_actions.marvinWhoIs, "vemär")

