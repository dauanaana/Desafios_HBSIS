import unittest
from unittest.mock import patch

import app


class TestInit(unittest.TestCase):
    @patch('app.print')
    def test_start(self, mock_print):
        app.start()
