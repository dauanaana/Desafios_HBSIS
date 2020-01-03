from app.password.password import Password
from app.requerimentos.requerimentos import Requerimentos
from app.requerimentos.aditivos import Aditivos
from app.requerimentos.deducao import Deducoes
<<<<<<< HEAD

def start():
   password = Password('dare4627###')
   aditivos = Aditivos(password)
   deducoes = Deducoes(password)
   pontos = (aditivos.validar() - deducoes.validar())
   aditivos.mostrar_aditivos()
   deducoes.mostrar_deducoes()
   print(f"{'TOTAL DE PONTOS:':<28}", pontos)








=======

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
>>>>>>> 256db4358ed10c0dc5f12144ffa13427cbb06d8b
