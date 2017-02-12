# === Purpose:
# Tests the purge.py file.
#
# === File:
# testPurge.py
#
# === Author:
# Jeremy Morris
import unittest
import os
import PurgeFiles.purge

class TestUserInput(unittest.TestCase):
    """
    Tests that when a user inputs a valid file or directory; the program
    identifies this as valid. When input is incorrect, the input
    is identified as invalid.
    """
    # def test_get_path_true(self):
    #     self.assertTrue(True, os.path.isfile('/home/Desktop/'))
    #
    # def test_get_path_false(self):
    #     self.assertFalse(False, os.path.isfile('invalid path'))
    # def test_get_path(self, test_input):
    #     self.test_input = '/home/Desktop/'
    #
    # def test_is_valid_true(self):
    #     user_input = '/home/Desktop'
    #     self.assertTrue(True, PurgeFiles.purge.UserInput.is_valid(user_input))
    #
    # def test_is_valid_false(self):
    #     self.assertFalse(False, PurgeFiles.purge.UserInput.is_valid('invalid path'))

if __name__ == '__main__':
    unittest.main()