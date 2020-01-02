import re
from string import ascii_letters as alpha

from app.password import Password
from app.requisitos import Requisitos


class Deducoes(Requisitos):
    def __init__(self, password: Password):
        super().__init__(password)

    def validar(self):
        #somente letras
        letras = self.somente_letras()
        self.pontos -= letras['value']

        #somente numeros
        numeros = self.somente_numeros()
        self.pontos -= numeros['value']

        # somente letras maiusculas consecutivas
        letras_mai_consecutivas = self.letras_maiusculas_cons()
        self.pontos -= letras_mai_consecutivas['value']

        #somente letras minusculas consecutivas
        letras_min_consecutivas = self.letras_minusculas_cons()
        self.pontos -= letras_min_consecutivas['value']

        #somente numneros consecutivos
        numeros_consecutivos = self.somente_numeros_consecutivos()
        self.pontos -= numeros_consecutivos['value']

        #somente letras sequenciais
        letras_sequenciais = self.somente_letras_sequenciais()
        self.pontos -= letras_sequenciais['value']

        #somente numeros sequenciais
        numeros_sequenciais = self.somente_numeros_sequenciais()
        self.pontos -= numeros_sequenciais['value']

        #somente simbolos sequenciais
        simbolos_sequenciais = self.somente_simbolos_sequenciais()
        self.pontos -= simbolos_sequenciais['value']

    def somente_letras(self):
        lista_somente_letras = {}
        letras = re.findall('[a-zA-z]', self.password.password)
        if len(letras) == len(self.password.password):
            lista_somente_letras['count'] = letras
            lista_somente_letras['value'] = letras
            return lista_somente_letras
        else:
            lista_somente_letras['count'] = 0
            lista_somente_letras['value'] = 0

            return lista_somente_letras

    def somente_numeros(self):
        lista_somente_numeros = {}
        numeros = re.findall('[0-9]', self.password.password)
        if len(numeros) == len(self.password.password):
            lista_somente_numeros['count'] = numeros
            lista_somente_numeros['value'] = numeros
        else:
            lista_somente_numeros['count'] = 0
            lista_somente_numeros['value'] = 0

            return lista_somente_numeros

    def letras_maiusculas_cons(self):
        posicao_consecutiva = 0
        lista_consecutivas = {}
        password = self.password.password

        for posicao in range(len(password) - 1):
            if posicao != (len(password)):
                if password[posicao].isupper():
                    if password[posicao + 1].isupper():
                         posicao_consecutiva += 1
        lista_consecutivas['count'] = posicao_consecutiva
        lista_consecutivas['value'] = posicao_consecutiva * 2

        if posicao_consecutiva > 0:
            return lista_consecutivas
        else:
            lista_consecutivas['count'] = 0
            lista_consecutivas['value'] = 0
            return lista_consecutivas

    def letras_minusculas_cons(self):
        posicao_consecutiva = 0
        lista_consecutivas = {}
        password = self.password.password

        for posicao in range(len(password) - 1):
            if posicao != (len(password)):
                if password[posicao].islower():
                    if password[posicao + 1].islower():
                         posicao_consecutiva += 1

        lista_consecutivas['count'] = posicao_consecutiva
        lista_consecutivas['value'] = posicao_consecutiva * 2

        if posicao_consecutiva > 0:
            return lista_consecutivas
        else:
            lista_consecutivas['count'] = 0
            lista_consecutivas['value'] = 0
            return lista_consecutivas

    def somente_numeros_consecutivos(self):
        posicao_consecutiva = 0
        lista_n_consecutivos = {}
        password = self.password.password

        for posicao in range(len(password) - 1):
            if posicao != (len(password)):
                if password[posicao].isnumeric():
                    if password[posicao + 1].isnumeric():
                        posicao_consecutiva += 1
        lista_n_consecutivos['count'] = posicao_consecutiva
        lista_n_consecutivos['value'] = posicao_consecutiva * 2

        if posicao_consecutiva > 0:
            return lista_n_consecutivos
        else:
            lista_n_consecutivos['count'] = 0
            lista_n_consecutivos['value'] = 0
            return lista_n_consecutivos

    def somente_letras_sequenciais(self):
        posicao_sequencial = 0
        sequencia = {}
        password = self.password.password
        maior = 0
        for posicao in range(len(password) - 1):
            try:
                if alpha.index(password[posicao]) + 1 == alpha.index(password[posicao + 1]):
                    posicao_sequencial += 1
                    if posicao_sequencial > maior:
                        maior = posicao_sequencial
                else:
                    posicao_sequencial = 0
            except:
                continue
        if maior >= 3:
            sequencia['count'] = maior
            sequencia['value'] = maior * 3
            return sequencia
        else:
            sequencia['count'] = 0
            sequencia['value'] = 0
            return sequencia

    def somente_numeros_sequenciais(self):
        numero_sequencial = 0
        lista_sequencia = {}
        password = self.password.password

        for posicao in range(len(password)):
            if posicao != len(password):
                try:
                    if int(password[posicao]) + 1 == int(password[posicao + 1]):
                      numero_sequencial += 1
                except:
                    continue
        if numero_sequencial >= 3:
            lista_sequencia['count'] = numero_sequencial
            lista_sequencia['value'] = numero_sequencial * 3
            return lista_sequencia
        else:
            lista_sequencia['count'] = 0
            lista_sequencia['value'] = 0
            return lista_sequencia

    def somente_simbolos_sequenciais(self):
        lista_sequencial = {}
        simbolo_sequencial = 0
        password = re.findall('\W', self.password.password)
        for posicao in range(len(password) - 1):
            if posicao != len(password):
                try:
                    if re.search('\W', password[posicao]) and re.search('\W', password[posicao + 1]):
                        simbolo_sequencial += 1
                except:
                    continue
        if simbolo_sequencial >= 3:
            lista_sequencial['count'] = simbolo_sequencial
            lista_sequencial['value'] = simbolo_sequencial * 3
            return lista_sequencial
        else:
            lista_sequencial['count'] = 0
            lista_sequencial['value'] = 0
            return lista_sequencial


# pas = Password('!@#$%')
# ded = Deducoes(pas)
# ded.validar()
# print(ded.pontos)
#print(ded.somente_letras())
#pritn(ded.somente_numeros())
#print(ded.letras_maiusculas_cons())
#print(ded.letras_minusculas_cons())
#print(ded.somente_numeros_consecutivos())
#print(ded.somente_letras_sequenciais())
#print(ded.somente_numeros_sequenciais())
#print(ded.somente_simbolos_sequenciais())


