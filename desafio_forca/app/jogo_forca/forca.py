from app.fruta.lista_frutas import ListaFrutas

from random import choice


class Forca:
    def __init__(self, lista_frutas: ListaFrutas):
        self.lista_frutas = lista_frutas
        self.chute = str
        self.fruta_secreta = object
        self.ganhou_jogo = False
        self.perdeu_jogo = False
        self.letras_incorretas = 0
        self.letras_corretas = 0
        self.dicas = []

    def jogar_forca(self):
        self.mostrar_titulo()
        self.sortear_fruta()
        self.montar_dica()
        while not self.perdeu_jogo and not self.ganhou_jogo:
            print(self.dicas)
            self.receber_input()
            self.chute_letra_correta()
            self.chute_letra_incorreta()
            self.ganhou_se_acertou_todas_as_letras()
            self.ganhou_se_chutou_uma_palavra()
            self.se_errou_enforcou()

    def mostrar_titulo(self):
        print('*' * 50)
        print(f'{"JOGO DA FORCA" :^46}')
        print('*' * 50)

    def sortear_fruta(self):
        self.fruta_secreta = choice(self.lista_frutas.get_lista())

    def montar_dica(self):
        for i in range(len(self.fruta_secreta.get_nome())):
            self.dicas.append('__')
        print('Esse é o tamanho da palavra secreta: ')

    def receber_input(self):
        self.chute = input('\nDigite uma letra: ')
        return self.chute

    def chute_letra_correta(self):
        posicao = 0
        acerto = 0
        for letra in self.fruta_secreta.get_nome():
            if self.chute == letra:
                self.dicas[posicao] = letra
                self.letras_corretas += 1
                acerto += 1
            posicao += 1
        return self.chute

    def chute_letra_incorreta(self):
        if self.chute not in self.fruta_secreta.get_nome():
            self.letras_incorretas += 1
            print(f'A palavra secreta não contém a letra: {self.chute}')
        return self.chute

    def ganhou_se_acertou_todas_as_letras(self):
        if self.letras_corretas == len(self.fruta_secreta.get_nome()):
            self.ganhou_jogo = True
            print(f'PALAVRA SECRETA É {self.fruta_secreta.get_nome()}\n'
                  'VOCÊ GANHOU!!!')
        return self.chute

    def ganhou_se_chutou_uma_palavra(self):
        if self.chute == self.fruta_secreta.get_nome():
            self.letras_corretas = self.fruta_secreta.get_nome()
            self.ganhou_jogo = True
            print(f'PALAVRA SECRETA É {self.fruta_secreta.get_nome()}\n'
                  'VOCÊ GANHOU!!!')
        return self.chute

    def se_errou_enforcou(self):
        if self.letras_incorretas == 6:
            self.perdeu_jogo = True
            print('VOCÊ PERDEU!!!')










