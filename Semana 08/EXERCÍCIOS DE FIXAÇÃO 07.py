def limpa(): return print("\033[2J\033[;H", end='')


limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
# -----------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''
7. Leia uma matriz 4x4, conte e escreva quantos valores são maiores que 10. '''

# Declara uma matriz 4x4
matriz = []

for i in range(4):

    linha = []

    for j in range(4):
        numero = int(input("Digite o valor da posição (%d, %d): " % (i, j)))
        linha.append(numero)

    matriz.append(linha)

# Declara a variável do contador
contador = 0

# Itera sobre a matriz para contar os valores maiores que 10
for i in range(4):

    for j in range(4):

        if matriz[i][j] > 10:
            contador += 1

# Imprime o número de valores maiores que 10
print("A matriz possui %d valores maiores que 10." % contador)
