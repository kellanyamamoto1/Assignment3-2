'''
RUN THIS FILE TO RUN THE UNIT TESTS
'''
# Kellan Yamamoto
# kellany@uci.edu
# 28388886

import unittest
from unittest.mock import patch, mock_open
from pathlib import Path
import ui

class TestOpenFile(unittest.TestCase):
    """
    open file unittest class
    """
    @patch('ui.open', new_callable=mock_open)
    @patch('ui.get_path')
    @patch('ui.file_name')
    @patch('ui.commands')
    def test_open_file_as_admin(
            self,
            mock_open):
        """
        Unittest to test open file function in admin mode
        """

        ui.ADMINISTRATOR = True
        user_input = "O /path/to/adminfile.dsu"

        result = ui.open_file(user_input)

        mock_open.assert_called_once_with(' ', 'a')
        self.assertEqual(result, ' ')

    @patch('ui.open', new_callable=mock_open)
    @patch('ui.get_path')
    @patch('ui.file_name')
    @patch('ui.commands')
    def test_open_file_as_user(
            self,
            mock_commands,
            mock_file_name,
            mock_get_path,
            mock_open):
        """
        Unittest to test open file function in user mode
        """

        ui.ADMINISTRATOR = False
        mock_get_path.return_value = '/path/to/'
        mock_file_name.return_value = 'userfile'

        result = ui.open_file('')

        mock_open.assert_called_once_with('/path/to/userfile.dsu', 'r+')
        self.assertEqual(result, '/path/to/userfile.dsu')
        mock_commands.assert_called_once()


class TestCreateFile(unittest.TestCase):
    '''
    Create file unittest class
    '''
    @patch('builtins.input',
           side_effect=["testuser",
                        "testpassword",
                        "testbio"])
    @patch('ui.commands')
    @patch('ui.Profile.save_profile')
    @patch('ui.open', new_callable=mock_open)
    def test_create_file_as_admin(
            self,
            mock_open,
            mock_save_profile):
        """
        Unittest to test create file as admin
        """
        ui.ADMINISTRATOR = True
        user_input = ["create", "/path/to", "-n", "testfile"]

        result = ui.create_file(user_input)

        expected_path = Path("/path/to/testfile.dsu")
        mock_open.assert_any_call(expected_path, 'a')
        self.assertEqual(mock_open.call_count, 2)
        mock_save_profile.assert_called_once_with(path=expected_path)
        self.assertEqual(result, expected_path)


if __name__ == '__main__':
    unittest.main()
