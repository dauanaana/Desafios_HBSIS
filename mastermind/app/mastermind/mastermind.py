
from app.colors.colors_list import ColorsList
from random import choice


class MasterMind:

    def __init__(self, colors_list: ColorsList):
        self.colors_list = colors_list
        self.random_colors = []  # cores sorteadas
        self.four_color = []  # tamanho da senha
        self.converted_random_colors = []  #conversao para string
        self.won = False  # ganhou
        self.lost = False  # perdeu
        self.error = 0  # erros
        self.play = 0

    def game(self):
        self.title()
        self.raffle_colors()
        self.converted_random_colors_to_string()
        print(self.converted_random_colors)
        while not self.won and not self.lost:
            self.play += 1
            self.four_color_password()
            self.round()
            self.attemps_game()
            self.you_won()
            self.you_lost()
            self.four_color.clear()
            self.error += 1

    def title(self):
        print('*' * 50)
        print(f'{"GAME MASTERMIND" :^46}')
        print('*' * 50)
        print(f'Colors: Red - Blue - Green - Orange - Purple - Yellow')
        print('Numero de tentativas: 20')

    def raffle_colors(self):  #raffle
        self.random_colors = [choice(self.colors_list.get_list()) for i in range(4)]

    def converted_random_colors_to_string(self):
        [self.converted_random_colors.append(c.get_name()) for c in self.random_colors]

    def four_color_password(self):  # 4 cores para senha
        for i in self.converted_random_colors:
            self.four_color.append(input("Tap one color: ").capitalize())

    def round(self):
        contador = 0
        for c in self.four_color:
            if c in self.converted_random_colors[contador]:
                print('Black')
            elif c in self.converted_random_colors:
                print('White')
            contador += 1

    def attemps_game(self):
        for c in self.four_color:
            if c not in self.converted_random_colors:
                print('Error: invalid color')

    def you_won(self):
        if self.four_color == self.converted_random_colors:
            self.won = True
            print('YOU WON!!! :)')

    def you_lost(self):
        if self.error == 4:
            self.lost = True
            print('YOU LOST!!! :(')


