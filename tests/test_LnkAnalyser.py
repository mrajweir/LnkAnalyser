import unittest
from LnkAnalyser import lnkanalyser

class TestLnkAnalyser(unittest.TestCase):

    def test_Init(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_shortcut(self):
            shortcut = lnkanalyser.go("Desktop.lnk")

            print(shortcut["header_size"])
            print(shortcut["link_class_id"])
            print(shortcut["link_flags"])
            print(shortcut["file_attributes"])
            print(shortcut["creation_time_of_link_target"])
            print(shortcut["access_time_of_link_target"])
            print(shortcut["write_time_of_link_target"])
            print(shortcut["target_file_size"])
            print(shortcut["icon_index"])
            print(shortcut["expected_window_state"])
            print(shortcut["hot_key"])
            print(shortcut["reserved_one"])
            print(shortcut["reserved_two"])
            print(shortcut["reserved_three"])
