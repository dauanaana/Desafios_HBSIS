from app import fruta
from app.jogo_forca.forca import Forca
from app.fruta.lista_frutas import Fruta, ListaFrutas


def start():
    print('*' * 50)
    print(f'{"JOGO DA FORCA" :^46}')
    print('*' * 50)
    banana = Fruta('banana')
    jabuticaba = Fruta('jabuticaba')
    pitanga = Fruta('pitanga')
    mirtilo = Fruta('mirtilo')
    morango = Fruta('morango')
    abacaxi = Fruta('abacaxi')
    cereja = Fruta('cereja')

    lista_frutas = ListaFrutas([banana, jabuticaba, pitanga, mirtilo, morango, abacaxi, cereja])
    forca = Forca(lista_frutas)
    forca.sortear_fruta()
    forca.Jogar()


