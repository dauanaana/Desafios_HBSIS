from random import shuffle

class Deck:
    def __init__(self, cartas: list):
        self._cartas = cartas

    def get_cartas(self):
        return self._cartas.copy()

    def shuffle_deck(self):
        return shuffle(self._cartas)

    def get_pega_carta(self):
        return self._cartas.pop(0)

