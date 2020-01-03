import unittest
from unittest.mock import Mock

from app import Deducoes


class TestDeducoes(unittest.TestCase):
    #validar
    # def test_para_validar_se_tem_deducoes(self):
    #     pasw = Mock()
    #     pasw.password = 'meunome'
    #     ded = Deducoes(pasw)
    #     retorno = ded.validar()
    #     print(retorno)
    #     self.assertEqual(retorno, abs(ded.pontos))
    #
    # def test_para_validar_se_nao_tem_deducoes(self):
    #     pasw = Mock()
    #     pasw.password = 'Dauana#4##@'
    #     ded = Deducoes(pasw)
    #     retorno = ded.validar()
    #     self.assertEqual(retorno, abs(ded.pontos))

    #somente letras
    def test_para_verificar_se_tiver_apenas_letras(self):
        pasw = Mock()
        pasw.password = 'EuSouumaletra'
        ded = Deducoes(pasw)
        retorno = ded.somente_letras()
        self.assertEqual(retorno['count'], 13)
        self.assertEqual(retorno['value'], 13)

    def test_para_verificar_se_nao_tiver_apenas_letras(self):
        pasw = Mock()
        pasw.password = 'EuSou97344'
        ded = Deducoes(pasw)
        retorno = ded.somente_letras()
        self.assertEqual(retorno['count'], 0)
        self.assertEqual(retorno['value'], 0)

    #somente numero
    def test_para_verificar_se_tiver_apenas_numeros(self):
        pasw = Mock()
        pasw.password = '12345'
        ded = Deducoes(pasw)
        retorno = ded.somente_numeros()
        self.assertEqual(retorno['count'], 5)
        self.assertEqual(retorno['value'], 5)

    def test_para_verificar_se_nao_tiver_apenas_numeros(self):
        pasw = Mock()
        pasw.password = '12345afgh'
        ded = Deducoes(pasw)
        retorno = ded.somente_numeros()
        self.assertEqual(retorno['count'], 0)
        self.assertEqual(retorno['value'], 0)

    # somente maiusculas consecutivas
    def test_verificar_se_tiver_maiusculas_consecutivas(self):
        pasw = Mock()
        pasw.password = '125AQRDS3456areSA'
        ded = Deducoes(pasw)
        retorno = ded.letras_maiusculas_consecutivas()
        self.assertEqual(retorno['count'], 5)
        self.assertEqual(retorno['value'], 10)

    def test_verificar_se_nao_tiver_maiusculas_consecutivas(self):
        pasw = Mock()
        pasw.password = '1GyfhY74l'
        ded = Deducoes(pasw)
        retorno = ded.letras_maiusculas_consecutivas()
        self.assertEqual(retorno['count'], 0)
        self.assertEqual(retorno['value'], 0)

    # somente minusculas consecutivas
    def test_verificar_se_tiver_minusculas_consecutivas(self):
        pasw = Mock()
        pasw.password = '125AQrtfsg35ghi'
        ded = Deducoes(pasw)
        retorno = ded.letras_minusculas_consecutivas()
        self.assertEqual(retorno['count'], 6)
        self.assertEqual(retorno['value'], 12)

    def test_verificar_se_nao_tiver_minusculas_consecutivas(self):
        pasw = Mock()
        pasw.password = '1Gf629l4*s'
        ded = Deducoes(pasw)
        retorno = ded.letras_minusculas_consecutivas()
        self.assertEqual(retorno['count'], 0)
        self.assertEqual(retorno['value'], 0)

    # somente numeros consecutivos
    def test_verificar_se_tiver_numeros_consecutivos(self):
        pasw = Mock()
        pasw.password = '125gdbRdH89533253'
        ded = Deducoes(pasw)
        retorno = ded.somente_numeros_consecutivos()
        self.assertEqual(retorno['count'], 9)
        self.assertEqual(retorno['value'], 18)

    def test_verificar_se_nao_tiver_numeros_consecutivos(self):
        pasw = Mock()
        pasw.password = '1erty3gdt8'
        ded = Deducoes(pasw)
        retorno = ded.somente_numeros_consecutivos()
        self.assertEqual(retorno['count'], 0)
        self.assertEqual(retorno['value'], 0)

    # somente letras sequenciais
    def test_verificar_se_tiver_letras_sequenciais(self):
        pasw = Mock()
        pasw.password = '123abcdefghij'
        ded = Deducoes(pasw)
        retorno = ded.somente_letras_sequenciais()
        self.assertEqual(retorno['count'], 9)
        self.assertEqual(retorno['value'], 27)








