import unittest

from app import Password


class TestPassword(unittest.TestCase):
    def test_se_password_e_instancia_da_classe_password(self):
        #Arrange
        pas = Password('esseyy5##')
        #Action - Só pode ser uma ação
        #Assert
        self.assertIsInstance(pas, Password)

    def test_se_get_value_retorna_password(self):
        pas = Password('verificar')

        retorno = pas.get_value()

        self.assertEqual(retorno, 'verificar')
