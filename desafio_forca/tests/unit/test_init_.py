import unittest
from unittest.mock import patch

from app import start


class TestInit(unittest.TestCase):

    @patch('app.jogo_forca.forca.input')
    def test_init(self, mock_input):
        with patch('app.jogo_forca.forca.print'):
            start()
