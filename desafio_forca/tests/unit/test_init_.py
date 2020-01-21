
import unittest
from unittest.mock import patch, call

from app import start, Forca


class TestInit(unittest.TestCase):

    @patch('app.Fruta')
    @patch('app.ListaFrutas')
    @patch('app.Forca')
    def test_init(self, forca_mock, lista_frutas_mock, fruta_mock, fruta_calls=None):

        start()

        fruta_calls = [
            call('banana'),
            call('jabuticaba'),
            call('pitanga'),
            call('mirtilo'),
            call('morango'),
            call('abacaxi'),
            call('cereja'),

        ]

        self.assertListEqual(
            fruta_calls, fruta_mock.mock_calls
        )
