import numpy as np
def limpa(): return print("\033[2J\033[;H", end='')


limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
# -----------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''
3. Faça um programa que leia um vetor de 8 posições e, em seguida, leia dois 
   valores X e Y correspondentes a duas posições no vetor. Ao ﬁnal, o programa 
   deverá escrever a soma dos valores encontrados nas respectivas posições X e Y.'''


# Declara um vetor de 8 posições
vetor = np.zeros(8)

# Lê os valores do vetor
for i in range(8):
    numero = float(input("Digite o valor da posição %d: " % i))
    vetor[i] = numero

# Lê os valores X e Y
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

# Calcula a soma dos valores nas posições X e Y
soma = vetor[x] + vetor[y]

# Imprime a soma
print("A soma dos valores nas posições X e Y é: %.2f" % soma)
