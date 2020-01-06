from app.frutas.lista_frutas import Frutas
from random import choice


class Forca(Frutas):
    def __init__(self, frutas: list):
        super().__init__(frutas)
        self.chute = ''
        self.p_secreta = ''
        self.acertou = False
        self.enforcou = False
        self.erros = 0
        self.acertos = 0
        self.dicas = []

    def montar_dica(self):
        for i in range(len(self.p_secreta)):
            self.dicas.append('__')
        print('Esse é o tamanho da palavra secreta: ')

    def Jogar(self):
        self.montar_dica()
        while not self.enforcou and not self.acertou:
            print(self.dicas)
            chute = input('\nDigite uma letra: ')
            if chute == self.p_secreta:
                self.acertou = True
                print(self.dicas)
                break

            posicao = 0
            acerto = 0
            for letra in self.p_secreta:
                if chute.upper() == letra.upper():
                    self.dicas[posicao] = letra.upper()
                    self.acertos += 1
                    acerto += 1
                posicao += 1

            if acerto == 0:
                self.erros += 1
                print(f'A palavra secreta não contém a letra: {chute}')

            if self.erros == 6:
                self.enforcou = True
                print('VOCÊ PERDEU!!!')

            if self.acertos == len(self.p_secreta):
                self.acertou = True
                print(f'PALAVRA SECRETA É {self.p_secreta}')
                print('VOCÊ GANHOU')








