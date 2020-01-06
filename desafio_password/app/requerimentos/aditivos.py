import re

from app.password.password import Password
from app.requerimentos.requerimentos import Requerimentos


class Aditivos(Requerimentos):
    def __init__(self, password: Password):
        super().__init__(password)

    def mostrar_aditivos(self):
        tamanho = self.validar_numeros_caracteres()
        maiusculas = self.validar_maiusculas()
        minusculas = self.validar_minusculas()
        numeros = self.validar_numeros()
        simbolos = self.validar_simbolos()
        caracter = self.validar_numeros_e_simbolos_no_meio_do_password()
        print(f"{'ADITIVOS ':^28}")
        print(f"{'Tamanho de Caracteres:':<28} {tamanho['count']} | {tamanho['value']}")
        print(f"{'Validar letras maiúsculas:':<28} {maiusculas['count']} | {maiusculas['value']}")
        print(f"{'Validar letras minúsculas:':<28} {minusculas['count']} | {minusculas['value']}")
        print(f"{'Validar números:':<28} {numeros['count']} | {numeros['value']}")
        print(f"{'Validar simbolos:':<28} {simbolos['count']} | {simbolos['value']}")
        print(f"{'Validar números e simbolos:':<28} {caracter['count']} | {caracter['value']}")
        print(f"{'Exigencias:':<28} {self.exigencia} | {self.exigencia * 2}\n")


    def validar(self):
        # numero de carcteres
        tamanho = self.validar_numeros_caracteres()
        self.pontos += tamanho['value']

        #letras maiusculas
        maiusculas = self.validar_maiusculas()
        self.pontos += maiusculas['value']

        # letras maiusculas
        minusculas = self.validar_minusculas()
        self.pontos += minusculas['value']

        # numeros
        numeros = self.validar_numeros()

        # Exigencias
        if numeros['count'] > 0 and len(self.password.password) > numeros['count']:
            self.pontos += numeros['value']
            if maiusculas['count'] > 0 and minusculas['count'] > 0:
                self.pontos += maiusculas['value']
                self.pontos += minusculas['value']
            elif maiusculas['count'] > 0 or minusculas['count'] > 0:
                if maiusculas['count'] > 0:
                    self.pontos += maiusculas['value']
                else:
                    self.pontos += minusculas['value']

        # caracteres especiais
        simbolos = self.validar_simbolos()
        self.pontos += simbolos['value']

        # Validar Numeros e Simbolos no meio do password
        caracter = self.validar_numeros_e_simbolos_no_meio_do_password()
        self.pontos += caracter['value']

        # FINAL - Soma com as Exigências

        if self.exigencia > 4:
            self.pontos += self.exigencia * 2

        return self.pontos

    def validar_numeros_caracteres(self):
        lista_senha = {}
        password = self.password.password
        if len(password) >= 8:
            self.exigencia += 1
        lista_senha['count'] = len(password)
        lista_senha['value'] = len(password) * 4
        return lista_senha

    def validar_maiusculas(self):
        lista_maiusculas = {}
        contador = 0
        maiusculas = re.findall('[A-Z]', self.password.password)
        contador += len(maiusculas)
        if contador > 0:
            self.exigencia += 1
            lista_maiusculas['count'] = contador
            lista_maiusculas['value'] = (len(self.password.password) - contador) * 2
            return lista_maiusculas
        else:
            lista_maiusculas['count'] = 0
            lista_maiusculas['value'] = 0
            return lista_maiusculas

    def validar_minusculas(self):
        lista_minusculas = {}
        contador = 0
        minusculas = re.findall('[a-z]', self.password.password)
        contador += len(minusculas)
        if contador > 0:
            self.exigencia += 1
            lista_minusculas['count'] = contador
            lista_minusculas['value'] = (len(self.password.password) - contador) * 2
            return lista_minusculas
        else:
            lista_minusculas['count'] = 0
            lista_minusculas['value'] = 0
            return lista_minusculas


    def validar_numeros(self):
        lista_numeros = {}
        contador = 0
        numeros = re.findall('\d', self.password.password)
        contador += len(numeros)
        if contador > 0:
            self.exigencia += 1
            lista_numeros['count'] = contador
            lista_numeros['value'] = contador * 4
            return lista_numeros
        else:
            lista_numeros['count'] = 0
            lista_numeros['value'] = 0
            return lista_numeros


    def validar_simbolos(self):
        lista_simbolos = {}
        contador = 0
        simbolos = re.findall('\W', self.password.password)
        contador += len(simbolos)
        if contador > 0:
            self.exigencia += 1
            lista_simbolos['count'] = contador
            lista_simbolos['value'] = contador * 6
            return lista_simbolos
        else:
            lista_simbolos['count'] = 0
            lista_simbolos['value'] = 0
            return lista_simbolos

    def validar_numeros_e_simbolos_no_meio_do_password(self):

        lista_caracter = {}
        inicio = 1
        final = len(self.password.password) - 1
        contador = 0

        caracter = re.findall('\W', self.password.password[inicio:final])
        contador += len(caracter)
        caracter = re.findall('\d', self.password.password[inicio:final])
        contador += len(caracter)

        if contador > 0:
            self.exigencia += 1
            lista_caracter['count'] = contador
            lista_caracter['value'] = contador * 2
            return lista_caracter
        else:
            lista_caracter['count'] = 0
            lista_caracter['value'] = 0
            return lista_caracter

# pas = Password('B#1l82@lp745')
# aditivos = Aditivos(pas)
# # aditivos.validar()
# # aditivos.mostrar_aditivos()
# # print(aditivos.pontos)
#
# # print(aditivos.validar_numeros_caracteres())
