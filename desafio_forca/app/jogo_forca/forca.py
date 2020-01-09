from app.fruta.lista_frutas import ListaFrutas
from random import choice

#alterar print para return
def _mostar(mostar):
    print(mostar)


def _input(param):
    return input(param)


class Forca:
    def __init__(self, lista_frutas: ListaFrutas):
        self.lista_frutas = lista_frutas
        self.chute = str
        self.p_secreta = object
        self.acertou = False
        self.enforcou = False
        self.erros = 0
        self.acertos = 0
        self.dicas = []

    def montar_dica(self):
        for i in range(len(self.p_secreta.nome)):
            self.dicas.append('__')
        _mostar('Esse é o tamanho da palavra secreta: ')

    def Jogar(self):
        self.montar_dica()
        while not self.enforcou and not self.acertou:
            _mostar(self.dicas)
            chute = _input('\nDigite uma letra: ')
            if chute == self.p_secreta.nome:
                self.acertou = True
                _mostar(self.p_secreta.nome)
                break
            self._tentativa(chute)
            self._se_errou_enforcou()
            self.se_ganhou()

    def sortear_fruta(self):
        self.p_secreta = choice(self.lista_frutas.lista)

    def _se_errou_enforcou(self):
        if self.erros == 6:
            self.enforcou = True
            _mostar('VOCÊ PERDEU!!!')

    def _tentativa(self, chute):
        posicao = 0
        acerto = 0
        for letra in self.p_secreta.nome:
            if chute.upper() == letra.upper():
                self.dicas[posicao] = letra.upper()
                self.acertos += 1
                acerto += 1
            posicao += 1

        if acerto == 0:
            self.erros += 1
            _mostar(f'A palavra secreta não contém a letra: {chute}')

    def se_ganhou(self):
        if self.acertos == len(self.p_secreta.nome):
            self.acertou = True
            _mostar(f'PALAVRA SECRETA É {self.p_secreta.nome}')
            _mostar('VOCÊ GANHOU')









