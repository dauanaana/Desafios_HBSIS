import re
from string import ascii_letters as alpha

from app.password.password import Password
from app.requerimentos.requerimentos import Requerimentos


class Deducoes(Requerimentos):
    def __init__(self, password: Password):
        super().__init__(password)

    def mostrar_deducoes(self):
        letras = self.somente_letras()
        numeros = self.somente_numeros()
        maiusculas_cons = self.letras_maiusculas_consecutivas()
        minuscula_cons = self.letras_minusculas_consecutivas()
        numeros_cons = self.somente_numeros_consecutivos()
        letras_seq = self.somente_letras_sequenciais()
        numeros_seq = self.somente_numeros_sequenciais()
        simbolos_seq = self.somente_simbolos_sequenciais()
        print(f"{'Somente letras:':<28} {letras['count']} | {letras['value']}")
        print(f"{'Somente números:':<28} {numeros['count']} | {numeros['value']}")
        print(f"{'Maiúsculas consecutivas:':<28} {maiusculas_cons['count']} | {maiusculas_cons['value']}")
        print(f"{'Minúsculas consecutivas:':<28} {minuscula_cons['count']} | {minuscula_cons['value']}")
        print(f"{'Números consecutivos:':<28} {numeros_cons['count']} | {numeros_cons['value']}")
        print(f"{'Letras sequenciais:':<28} {letras_seq['count']} | {letras_seq['value']}")
        print(f"{'Números sequenciais:':<28} {numeros_seq['count']} | {numeros_seq['value']}")
        print(f"{'Símbolos sequenciais:':<28} {simbolos_seq['count']} | {simbolos_seq['value']}")

    def validar(self):
        #somente letras
        letras = self.somente_letras()
        self.pontos -= letras['value']

        #somente numeros
        numeros = self.somente_numeros()
        self.pontos -= numeros['value']

        # somente letras maiusculas consecutivas
        maiusculas_cons = self.letras_maiusculas_consecutivas()
        self.pontos -= maiusculas_cons['value']

        #somente letras minusculas consecutivas
        minusculas_cons = self.letras_minusculas_consecutivas()
        self.pontos -= minusculas_cons['value']

        #somente numneros consecutivos
        numeros_cons = self.somente_numeros_consecutivos()
        self.pontos -= numeros_cons['value']

        #somente letras sequenciais
        letras_seq = self.somente_letras_sequenciais()
        self.pontos -= letras_seq['value']

        #somente numeros sequenciais
        numeros_seq = self.somente_numeros_sequenciais()
        self.pontos -= numeros_seq['value']

        #somente simbolos sequenciais
        simbolos_seq = self.somente_simbolos_sequenciais()
        self.pontos -= simbolos_seq['value']

    def somente_letras(self):
        lista_somente_letras = {}
        letras = len(re.findall('[a-zA-Z]', self.password.password()))
        if letras == len(self.password.password()):
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

    def letras_maiusculas_consecutivas(self):
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

    def letras_minusculas_consecutivas(self):
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

pas = Password('B#1l82@lp745')
deducoes = Deducoes(pas)
print(deducoes.somente_numeros)
# deducoes.mostrar_deducoes()
# print(deducoes.pontos)



