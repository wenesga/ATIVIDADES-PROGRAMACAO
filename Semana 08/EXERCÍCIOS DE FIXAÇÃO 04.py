import numpy as np
def limpa(): return print("\033[2J\033[;H", end='')


limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
# -----------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''
4. Leia um vetor de 10 posições. Conte e escreva quantos valores pares ele possui. '''
# Declara um vetor de 10 posições
vetor = np.zeros(4)
vetor_par = []

# Lê os valores do vetor
for i in range(4):
    numero = float(input("Digite o valor da posição %d: " % i))
    vetor[i] = numero

# Conta os valores pares
pares = 0
for numero in vetor:
    if numero % 2 == 0:
        pares += 1
        vetor_par.append(numero)

print(vetor)

# Imprime o número de valores pares
print("O vetor possui %d valores pares." % pares)

# Imprime o vetor de valores pares
print(vetor_par)
