import unittest

from app import ListaFrutas


class TestListaFrutas(unittest.TestCase):
    def test_se_retorna_a_lista_de_frutas(self):
        f = ListaFrutas(['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja'])
        self.assertEqual(f.lista, ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja'])
