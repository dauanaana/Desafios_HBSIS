from random import choice
from app.frutas.funcoes_fruta import Frutas


class ListaFrutas:
    def __init__(self, frutas: list):
        self.frutas = ['banana', 'jabuticaba', 'pitanga', 'mirtilo', 'morango', 'abacaxi', 'cereja']
        self.fruta_secreta = Frutas


    def sortear_fruta(self):
        self.p_secreta = choice(self.frutas)