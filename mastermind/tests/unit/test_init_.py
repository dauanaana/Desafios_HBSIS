
import unittest
from unittest.mock import patch, call

from app import start, MasterMind


class TestInit(unittest.TestCase):

    @patch('app.Color')
    @patch('app.ColorsList')
    @patch('app.MasterMind')
    def test_init(self, mastermind_mock, colorslist_mock, color_mock):

        start()

        color_calls = [
            call('Red'),
            call('Blue'),
            call('Green'),
            call('Orange'),
            call('Purple'),
            call('Yellow')
        ]

        self.assertListEqual(
            color_calls, color_mock.mock_calls
        )




