# Kellan Yamamoto
# kellany@uci.edu
# 28388886

import unittest
from unittest.mock import patch, mock_open, MagicMock
import ui


class TestOpenFile(unittest.TestCase):
    @patch('file_module.open', new_callable=mock_open)
    @patch('file_module.get_path')
    @patch('file_module.file_name')
    @patch('file_module.commands')
    def test_open_file_as_administrator(
            self,
            mock_commands,
            mock_file_name,
            mock_get_path,
            mock_open):
        ui.ADMINISTRATOR = True
        user_input = "open /path/to/adminfile.dsu"

        result = ui.open_file(user_input)

        mock_open.assert_called_once_with('/path/to/adminfile.dsu', 'a')
        self.assertEqual(result, '/path/to/adminfile.dsu')

    @patch('file_module.open', new_callable=mock_open)
    @patch('file_module.get_path')
    @patch('file_module.file_name')
    @patch('file_module.commands')
    def test_open_file_as_non_administrator(
            self,
            mock_commands,
            mock_file_name,
            mock_get_path,
            mock_open):
        ui.ADMINISTRATOR = False
        mock_get_path.return_value = '/path/to/'
        mock_file_name.return_value = 'userfile'

        result = ui.open_file('')

        mock_open.assert_called_once_with('/path/to/userfile.dsu', 'r+')
        self.assertEqual(result, '/path/to/userfile.dsu')
        mock_commands.assert_called_once()


if __name__ == '__main__':
    unittest.main()
