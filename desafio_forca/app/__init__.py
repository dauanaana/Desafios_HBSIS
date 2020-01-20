from app import fruta
from app.fruta.fruta import Fruta
from app.jogo_forca.forca import Forca
from app.fruta.lista_frutas import ListaFrutas


def start():
    banana = Fruta('banana')
    jabuticaba = Fruta('jabuticaba')
    pitanga = Fruta('pitanga')
    mirtilo = Fruta('mirtilo')
    morango = Fruta('morango')
    abacaxi = Fruta('abacaxi')
    cereja = Fruta('cereja')

    lista_frutas = ListaFrutas([banana, jabuticaba, pitanga, mirtilo, morango, abacaxi, cereja])
    forca = Forca(lista_frutas)
    forca.jogar_forca()


