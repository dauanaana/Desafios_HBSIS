import unittest
from unittest.mock import Mock, patch, call

from app import Forca, ListaFrutas


class TestForca(unittest.TestCase):

    # jogar_forca
    @patch('app.jogo_forca.forca.choice')
    @patch('app.jogo_forca.forca.input')
    @patch('app.jogo_forca.forca.print')
    def test_if_mastermind_is_playing(self, mock_print, mock_input, mock_choice):
        mock_input.side_effect = ['b', 'a', 'n', 'a', 'n', 'a']
        banana = Mock()
        banana.get_name.return_value = 'banana'
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

    # sortear fruta
    @patch('app.jogo_forca.forca.choice')
    def test_se_esta_sorteando_uma_palavra_fruta(self, mock_choice):
        lista_frutas = Mock()
        Forca(lista_frutas)
        master = Forca(ListaFrutas([]))
        master.sortear_fruta()
        self.assertEqual(1, mock_choice.call_count)
        self.assertListEqual([call([])], mock_choice.mock_calls)
        # verificações do mock
        # print(mock_choice.mock_calls)
        # print(mock_choice.call_count)
        # print(mock_choice.called)
        # print(mock_choice.call_args_list)

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


    # receber input
    @patch('app.jogo_forca.forca.input')
    def test_se_esta_retornando_uma_letra(self, mock_input):
        with patch('app.jogo_forca.forca.print'):
            mock_input.side_effect = ('b')
            lista_frutas = Mock()
            jogo = Forca(lista_frutas)
            jogo.fruta_secreta = Mock()
            jogo.fruta_secreta.get_nome.return_value = 'b'
            jogo.dicas = ['__']
            resultado = jogo.receber_input()
            self.assertEqual(resultado, ('b'))

    # receber input
    @patch('app.jogo_forca.forca.input')
    def test_se_esta_retornando_uma_palavra(self, mock_input):
        with patch('app.jogo_forca.forca.print'):
            mock_input.side_effect = ['banana']
            lista_frutas = Mock()
            jogo = Forca(lista_frutas)
            jogo.fruta_secreta = Mock()
            jogo.fruta_secreta.get_nome.return_value = 'banana'
            jogo.chute = 'banana'
            resultado = jogo.receber_input()
            self.assertEqual(resultado, 'banana')

    #chute_letra_correta
    @patch('app.jogo_forca.forca.print')
    def test_tentativa_para_receber_letra_que_contem_na_fruta_sorteada(self, mock_print):
        with patch('app.jogo_forca.forca.print'):
            lista_frutas = Mock()
            jogo = Forca(lista_frutas)
            jogo.fruta_secreta = Mock()
            jogo.fruta_secreta.get_nome.return_value = 'banana'
            jogo.dicas = ['b']
            jogo.letras_corretas += 1
            jogo.chute = 'b'
            result = jogo.chute_letra_correta()
            self.assertEqual(result, 'b')

    #chute_letra_incorreta
    @patch('app.jogo_forca.forca.print')
    def test_tentativa_para_receber_letra_que_nao_contem_na_fruta_sorteada(self, mock_print):
        with patch('app.jogo_forca.forca.print'):
            lista_frutas = Mock()
            jogo = Forca(lista_frutas)
            jogo.fruta_secreta = Mock()
            jogo.fruta_secreta.get_nome.return_value = 'banana'
            jogo.chute = 'j'
            resultado = jogo.chute_letra_incorreta()
            self.assertNotIn(resultado, 'banana')

    #ganhou_se_acertou_todas_as_letras
    @patch('app.jogo_forca.forca.input')
    @patch('app.jogo_forca.forca.print')
    def test_se_acertou_todas_as_letras_e_ganhou(self, mock_print, mock_input):
        with patch('app.jogo_forca.forca.print'):
            mock_input.side_effect = ['b', 'a', 'n', 'a', 'n', 'a']
            lista_frutas = Mock()
            jogo = Forca(lista_frutas)
            jogo.fruta_secreta = Mock()
            jogo.fruta_secreta.get_nome.return_value = 'banana'
            jogo.dicas = ['__', '__', '__', '__', '__', '__' ]
            jogo.letras_corretas = 6
            jogo.ganhou_se_acertou_todas_as_letras()
            self.assertEqual(len(jogo.fruta_secreta.get_nome()), 6)

    # ganhou_se_acertou_chutando uma palavra
    @patch('app.jogo_forca.forca.input')
    @patch('app.jogo_forca.forca.print')
    def test_se_acertou_chutando_uma_palavra(self, mock_print, mock_input):
        with patch('app.jogo_forca.forca.print'):
            mock_input.side_effect = ['b', 'a', 'n', 'a', 'n', 'a']
            lista_frutas = Mock()
            jogo = Forca(lista_frutas)
            jogo.fruta_secreta = Mock()
            jogo.fruta_secreta.get_nome.return_value = 'banana'
            jogo.dicas = ['__', '__', '__', '__', '__', '__']
            jogo.chute = 'banana'
            jogo.ganhou_se_chutou_uma_palavra()
            self.assertEqual(jogo.fruta_secreta.get_nome(), 'banana')

    #se_errou_enforcou
    @patch('app.jogo_forca.forca.print')
    def test_se_perdeu(self, mock_print):
        lista_frutas = Mock()
        jogo = Forca(lista_frutas)
        jogo.fruta_secreta = Mock()
        jogo.letras_incorretas = 6
        jogo.se_errou_enforcou()
        mock_print.assert_called_once_with('VOCÊ PERDEU!!!')










































