import unittest
import os
from LnkAnalyser import lnkanalyser

class TestLnkAnalyser(unittest.TestCase):

    def test_Init(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_shortcut(self):
        # Intentionally breaking the unit test
        self.assertEqual(True, False)
        shortcut = lnkanalyser.go(
            "{0}/Desktop.lnk".format(os.path.dirname(os.path.realpath(__file__)))
        )