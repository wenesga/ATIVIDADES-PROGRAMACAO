import numpy as np
def limpa(): return print("\033[2J\033[;H", end='')


limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
# -----------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''
8. Declare uma matriz 5x5 e preencha com 1 na diagonal principal e 0 nos demais
   elementos. Ao ﬁnal, escreva a matriz obtida. '''

# Declara uma matriz 5x5
matriz = []
for i in range(5):
    linha = []
    for j in range(5):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

matriz = np.array(matriz)

# Imprime a matriz
print(matriz)
