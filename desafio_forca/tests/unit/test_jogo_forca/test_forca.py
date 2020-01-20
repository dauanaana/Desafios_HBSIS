import unittest
from unittest.mock import Mock, patch, call

from app import Forca, ListaFrutas


class TestForca(unittest.TestCase):

    ## jogar_forca
    @patch('app.jogo_forca.forca.choice')
    @patch('app.jogo_forca.forca.input')
    @patch('app.jogo_forca.forca.print')
    def test_if_mastermind_is_playing(self, mock_print, mock_input, mock_choice):
        mock_input.side_effect = ['b', 'a', 'n', 'a', 'n', 'a']
        banana = Mock()
        banana.get_name.return_value = 'banana'
        jabuticaba = Mock()
        jabuticaba.get_name.return_value = 'jabuticaba'
        pitanga = Mock()
        pitanga.get_name.return_value = 'pitanga'
        mirtilo = Mock()
        mirtilo.get_name.return_value = 'mirtilo'
        morango = Mock()
        morango.get_name.return_value = 'morango'
        abacaxi = Mock()
        abacaxi.get_name.return_value = 'abacaxi'
        cereja = Mock()
        cereja.get_name.return_value = 'cereja'

        mock_choice.lista_frutas = [banana]
        lista_frutas = Mock()
        master = Forca(lista_frutas)
        master.jogar_forca()

    # titulo
    @patch('app.jogo_forca.forca.print')
    def test_titulo(self, mock_print):
        master = Forca(Mock)
        method = master.mostrar_titulo()
        assert mock_print(method)

    #montar dica
    @patch('app.jogo_forca.forca.print')
    def test_se_esta_montando_dica(self, mock_print):
        with patch('app.jogo_forca.forca.print'):
            lista_frutas = Mock()
            banana = Mock()
            banana.get_nome.return_value = 'banana'
            lista_frutas.get_lista.return_value = [banana]
            f = Forca(lista_frutas)
            f.fruta_secreta = banana
            f.montar_dica()
            self.assertEqual(len(f.fruta_secreta.get_nome()), len(f.dicas))

    # sortear fruta
    @patch('app.jogo_forca.forca.choice')
    def test_se_esta_sorteando_uma_palavra_fruta(self, mock_choice):
        lista_frutas = Mock()
        Forca(lista_frutas)
        master = Forca(ListaFrutas([]))
        master.sortear_fruta()
        self.assertEqual(1, mock_choice.call_count)
        self.assertListEqual([call([])], mock_choice.mock_calls)

    #input
    @patch('app.jogo_forca.forca.input')
    def test_se_esta_pedindo_input(self, mock_input):
        jogo = Forca(Mock())
        b = jogo.digitar_algo = 'banana'
        assert mock_input.b('banana')

    # def test_tentativa(self):
    #     jogo = Forca(Mock)
    #     jogo.tentativa = 'bananna'
    #     jogo.fruta_secreta.get_nome = 'banana'





















