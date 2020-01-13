import unittest
from unittest.mock import Mock, patch

from app import Forca

class TestForca(unittest.TestCase):

    @patch('app.jogo_forca.forca.print')
    def test_se_esta_montando_dica(self, mock_print):
        with patch('app.jogo_forca.forca.print'):
            lista_frutas = Mock()
            banana = Mock()
            banana.get_nome.return_value = 'banana'
            lista_frutas.get_lista.return_value = [banana]
            f = Forca(lista_frutas)
            f.p_secreta = banana
            f.montar_dica()
            self.assertEqual(len(f.p_secreta.get_nome()), len(f.dicas))



















