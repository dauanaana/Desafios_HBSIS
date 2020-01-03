import unittest
from unittest.mock import Mock, patch

from app import Aditivos, Password


class TestAditivos(unittest.TestCase):
    #validar
    def test_se_realemte_esta_valido_sem_todas_exigencias(self):
        #arrange
        pasw = Mock()
        pasw.password = 'dauana'
        ad = Aditivos(pasw)
        #action
        retorno = ad.validar()
        #assert
        self.assertEqual(retorno, ad.pontos)

    def test_se_realmente_esta_validando_com_todas_exigencias(self):
        pasw = Mock()
        pasw.password = '122HMRFTjsubhyad@#$#'
        ad = Aditivos(pasw)
        retorno = ad.validar()
        self.assertEqual(retorno, ad.pontos)

    def test_se_realmente_esta_validando_maiucsulas_nas_exigencias(self):
        pasw = Mock()
        pasw.password = '122djjjkjd@#$#'
        ad = Aditivos(pasw)
        retorno = ad.validar()
        self.assertEqual(retorno, ad.pontos)

    def test_se_realmente_esta_validando_minusculas_nas_exigencias(self):
        pasw = Mock()
        pasw.password = '12RFVHBJN@#$#'
        ad = Aditivos(pasw)
        retorno = ad.validar()
        self.assertEqual(retorno, ad.pontos)

    #mostar aditivos
    @patch('app.requerimentos.aditivos.print')
    def test_para_mostar_aditivos(self, mock_print):
        pasw = Mock()
        pasw.password = '12RFVHBJN@#$#'
        ad = Aditivos(pasw)
        ad.mostrar_aditivos()

    #validar caracteres
    def test_se_realmente_esta_validando_o_tamamho_da_senha(self):
        pasw = Mock()
        pasw.password = '123456789'
        ad = Aditivos(pasw)
        retorno = ad.validar_numeros_caracteres()
        # print(retorno['count'])
        # print(retorno['value'])
        self.assertEqual(retorno['count'], 9)
        self.assertEqual(retorno['value'], 36)

    #test validar maiusculas
    def test_se_realmente_tem_letras_maiusculas(self):
        pasw = Mock()
        pasw.password = 'ASDER124FRE'
        ad = Aditivos(pasw)
        retorno = ad.validar_maiusculas()
        # print(retorno)
        self.assertEqual(retorno['count'], 8)
        self.assertEqual(retorno['value'], 6)

    def test_se_nao_tem_letra_maiuscula(self):
        pasw = Mock()
        pasw.password = 'ass124'
        ad = Aditivos(pasw)
        retorno = ad.validar_maiusculas()
        self.assertEqual(retorno['count'], 0)
        self.assertEqual(retorno['value'], 0)

    #teste validar minusculas
    def test_se_realmete_tem_letras_minusculas(self):
        pasw = Mock()
        pasw.password = 'bababa$%12'
        ad = Aditivos(pasw)
        retorno = ad.validar_minusculas()
        self.assertEqual(retorno['count'], 6)
        self.assertEqual(retorno['value'], 8)

    def test_se_nao_tem_letras_minusculas(self):
        pasw = Mock()
        pasw.password = 'BABABA124@CFRD'
        ad = Aditivos(pasw)
        retorno = ad.validar_minusculas()
        self.assertEqual(retorno['count'], 0)
        self.assertEqual(retorno['value'], 0)

    #teste validar numeros
    def test_se_realmente_tem_numeros(self):
        pasw = Mock()
        pasw.password = '14567rf68EDF'
        ad = Aditivos(pasw)
        retorno = ad.validar_numeros()
        self.assertEqual(retorno['count'], 7)
        self.assertEqual(retorno['value'], 28)

    def test_se_nao_tem_numeros(self):
        pasw = Mock()
        pasw.password = 'ASDitehgedrt'
        ad = Aditivos(pasw)
        retorno = ad.validar_numeros()
        self.assertEqual(retorno['count'], 0)
        self.assertEqual(retorno['value'], 0)

    #teste validar simbolos
    def test_se_realmente_tem_simbolos(self):
        pasw = Mock()
        pasw.password = '!@#$%edr*&TT65'
        ad = Aditivos(pasw)
        retorno = ad.validar_simbolos()
        self.assertEqual(retorno['count'], 7)
        self.assertEqual(retorno['value'], 42)

    def test_se_nao_tem_simbolos(self):
        pasw = Mock()
        pasw.password = 'aQueri35'
        ad = Aditivos(pasw)
        retorno = ad.validar_simbolos()
        self.assertEqual(retorno['count'], 0)
        self.assertEqual(retorno['value'], 0)

    #teste validar numeros e simbolos no meio
    def test_se_realmente_tem_simbolos_e_numeros_no_meio(self):
        pasw = Mock()
        pasw.password = 'Af%#45#klp'
        ad = Aditivos(pasw)
        retorno = ad.validar_numeros_e_simbolos_no_meio_do_password()
        self.assertEqual(retorno['count'], 5)
        self.assertEqual(retorno['value'], 10)

    def test_se_nao_tiver_simbolos_e_numeros_no_meio(self):
        pasw = Mock()
        pasw.password = 'AfhTRlsbdklp'
        ad = Aditivos(pasw)
        retorno = ad.validar_numeros_e_simbolos_no_meio_do_password()
        self.assertEqual(retorno['count'], 0)
        self.assertEqual(retorno['value'], 0)





