# === Purpose:
# Tests the purge.py file.
#
# === File:
# test_purge.py
#
# === Author:
# Jeremy Morris
import shutil
import tempfile
import unittest
import os
from PurgeFiles import purge


class TestPurge(unittest.TestCase):
    """
    Tests that when a user inputs a valid file or directory; the program
    identifies it as valid. When input is incorrect, the input
    is identified as invalid.
    """
    def setUp(self):
        # Create a temporary directory.
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the temporary directory after the test.
        shutil.rmtree(self.test_dir)

    def test_delete_file(self):
        # Create a file in the temp directory.
        test_file = open(os.path.join(self.test_dir, 'test.txt'), 'test file')
        # Write some data to the file.
        test_file.write('May the force be with you.')
        # Verify that the file is deleted after using delete_file method.
        purge.File.delete_file(self.test_dir, test_file)
        self.assertTrue(self.test_dir, not os.path.exists(test_file), None)

    def test_delete_file(self):
        # Create a file in the temp directory.
        test_file = open(os.path.join(self.test_dir, 'test.txt'), 'test file')
        # Write some data to the file.
        test_file.write('May the force be with you.')
        # Verify that the file is deleted after using delete_file method.
        purge.File.delete_file(self.test_dir, test_file)

if __name__ == '__main__':
    unittest.main()