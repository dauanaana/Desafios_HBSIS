from app.password.password import Password



class Requerimentos:
    def __init__(self, password: Password):
        self.password = password
        self.exigencia = 0
        self.pontos = 0

    def mostar_pontos(self):
        return self.pontos




