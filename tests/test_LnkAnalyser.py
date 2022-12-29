import unittest

class TestLnkAnalyser(unittest.TestCase):

    def test_Init(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def travis_ci_test(self):
        self.assertEqual(1, 1)