from app.forca import Forca
from app.frutas import Frutas


def start():
    frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']
    forca = Forca(frutas)
    forca.sortear_fruta()
    forca.Jogar()

print('*'*50)
print(f'{"JOGO DA FORCA" :^46}')
print('*'*50)