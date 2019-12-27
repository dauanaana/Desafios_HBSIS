class Carta:
    def __init__(self, name: str, value: int):
        self._name = name
        self._value = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

class A(Carta):
    def __init__(self, name='A', value=1):
        super().__init__(name, value)

class Dois(Carta):
    def __init__(self, name='2', value=2):
        super().__init__(name, value)

class Tres(Carta):
    def __init__(self, name='3', value=3):
        super().__init__(name, value)

class Quatro(Carta):
    def __init__(self, name='4', value=4):
        super(). __init__(name, value)

class Cinco(Carta):
    def __init__(self, name='5', value=5):
        super().__init__(name, value)

class Seis(Carta):
    def __init__(self, name='6', value=6):
        super().__init__(name, value)

class Sete(Carta):
    def __init__(self, name='7', value=7):
        super().__init__(name, value)

class Oito(Carta):
    def __init__(self, name='8', value=8):
        super().__init__(name, value)

class Nove(Carta):
    def __init__(self, name='9', value=9):
        super().__init__(name, value)

class Dez(Carta):
    def __init__(self, name='10', value=10):
        super().__init__(name, value)

class J(Carta):
    def __init__(self, name='J', value=10):
        super().__init__(name, value)

class Q(Carta):
    def __init__(self, name='Q', value=10):
        super().__init__(name, value)

class K(Carta):
    def __init__(self, name='K', value=10):
        super().__init__(name, value)



