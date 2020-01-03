import unittest
from unittest.mock import Mock

from app import Requerimentos


class TestRequerimentos(unittest.TestCase):
    def test_se_requerimentos_e_instancia_de_requerimentos(self):
        #arrange
        password = Mock()
        re = Requerimentos(password)

        #assert
        self.assertIsInstance(re, Requerimentos)

    def test_verificar_retorno_pontos_retorna_corretamente(self):
        #arrange
        password = Mock()
        re = Requerimentos(password)
        re.pontos = 10

        #action
        retorno = re.mostar_pontos()

        #assert
        self.assertEqual(retorno, 10)







