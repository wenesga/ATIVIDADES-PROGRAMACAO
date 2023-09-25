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


def localizar_maior_valor(matriz):
    # Declara as variáveis do maior valor e da sua localização
    maior_valor = matriz[0][0]
    linha_maior = 0
    coluna_maior = 0

    # Itera sobre a matriz para encontrar o maior valor
    for i in range(3):
        for j in range(3):
            if matriz[i][j] > maior_valor:
                maior_valor = matriz[i][j]
                linha_maior = i
                coluna_maior = j

    # Retorna a localização do maior valor
    return linha_maior, coluna_maior


# Declara uma matriz 4x4
matriz = []
for i in range(3):
    linha = []
    for j in range(3):
        numero = float(input("Digite o valor da posição (%d, %d): " % (i, j)))
        linha.append(numero)
    matriz.append(linha)


matriz = np.array(matriz)


# Imprime a matriz
print(matriz)

# Chama a função para localizar o maior valor da matriz
linha_maior, coluna_maior = localizar_maior_valor(matriz)

# Imprime a localização do maior valor
print("O maior valor da matriz está na linha %d e coluna %d." %
      (linha_maior, coluna_maior))
