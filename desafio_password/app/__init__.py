from app.password.password import Password
from app.requerimentos.requerimentos import Requerimentos
from app.requerimentos.aditivos import Aditivos
from app.requerimentos.deducao import Deducoes

def start():
    password = Password('StrongPassword')
    add = Aditivos(password)
    ded = Deducoes(password)
    add.validar()
    ded.validar()
    add.show_total_pontos()
    add.mostrar_aditivos()
    ded.mostrar_deducoes()
    return True
