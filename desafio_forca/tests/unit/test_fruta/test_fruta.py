import unittest

from app.fruta.fruta import Fruta


class MyTestFruta(unittest.TestCase):
    def test_se_fruta_retorna_com_nome_da_fruta(self):
        f = Fruta('banana')
        self.assertEqual(f.get_nome(), 'banana')