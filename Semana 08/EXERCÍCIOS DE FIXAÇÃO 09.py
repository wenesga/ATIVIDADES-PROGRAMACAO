import numpy as np
def limpa(): return print("\033[2J\033[;H", end='')


limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
# -----------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''
9. Faça um programa que preenche uma matriz com o produto do valor da linha e 
   da coluna de cada elemento. Em seguida, imprima a matriz na tela.  '''


# Declara uma matriz 3x3
matriz = []

for i in range(3):
    linha = []

    for j in range(3):
        linha.append(i * j)

    matriz.append(linha)

matriz = np.array(matriz)

# Imprime a matriz
print(matriz)
