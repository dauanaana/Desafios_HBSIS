from app.jogo_forca.forca import Forca
from app.frutas.lista_frutas import Frutas


def start():
    frutas = Frutas
    forca = Forca(frutas)
    forca.sortear_fruta()
    forca.Jogar()

# print('*'*50)
# print(f'{"JOGO DA FORCA" :^46}')
# print('*'*50)