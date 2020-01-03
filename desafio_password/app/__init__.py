from app.password.password import Password
from app.requerimentos.requerimentos import Requerimentos
from app.requerimentos.aditivos import Aditivos
from app.requerimentos.deducao import Deducoes

def start():
   password = Password('dare4627###')
   aditivos = Aditivos(password)
   deducoes = Deducoes(password)
   pontos = (aditivos.validar() - deducoes.validar())
   aditivos.mostrar_aditivos()
   deducoes.mostrar_deducoes()
   print(f"{'TOTAL DE PONTOS:':<28}", pontos)








