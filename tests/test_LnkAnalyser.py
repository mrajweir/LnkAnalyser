import unittest
from LnkAnalyser import lnkanalyser

class TestLnkAnalyser(unittest.TestCase):

    def test_Init(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_shortcut(self):
        shortcut = lnkanalyser.go("Desktop.lnk")