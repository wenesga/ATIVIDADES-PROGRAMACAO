limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

""" #----------------------------------------------------------
    Arraias - TO => 2023 => UFT - Lincenciatura em Computação
    Disciplina => Programação de Computadores
    @Autor => Wenes Aquino => 2º Períldo
"""#-----------------------------------------------------------

import math

angulo = float(input("Digite o angulo: "))

seno = math.sin(angulo)
coss = math.cos(angulo)
tang = math.tan(angulo)

print(f""""
      Seno({angulo}) = {seno}
   Cosseno({angulo}) = {coss}
  Tangente({angulo}) = {seno}
""")