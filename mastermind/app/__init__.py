
from app.colors.color import Color
from app.colors.colors_list import ColorsList
from app.mastermind.mastermind import MasterMind

def start():
    red = Color('Red')
    blue = Color('Blue')
    green = Color('Green')
    orange = Color('Orange')
    purple = Color('Purple')
    yellow = Color('Yellow')

    colors_list = ColorsList([red, blue, green, orange, purple, yellow])
    playgame = MasterMind(colors_list)
    playgame.game()


