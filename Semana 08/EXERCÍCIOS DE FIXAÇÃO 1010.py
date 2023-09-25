import numpy as np
def limpa(): return print("\033[2J\033[;H", end='')


limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
# -----------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''
10. Leia uma matriz 4x4, imprima a matriz e retorne a localização(linha e coluna) 
    do maior valor. '''

# Inicializa a matriz 4x4 com zeros
matriz = [[0] * 4 for _ in range(4)]

# Lê os valores da matriz
for i in range(4):
    for j in range(4):
        matriz[i][j] = float(
            input(f"Digite o valor para a posição [{i}][{j}]: "))

# Imprime a matriz
matriz = np.array(matriz)
print(matriz)

# Encontra a localização do maior valor
maior_valor = matriz[0][0]
linha_maior = 0
coluna_maior = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            linha_maior = i
            coluna_maior = j

# Imprime a localização do maior valor
print(f"O maior valor está na linha {linha_maior} e coluna {coluna_maior}.")
