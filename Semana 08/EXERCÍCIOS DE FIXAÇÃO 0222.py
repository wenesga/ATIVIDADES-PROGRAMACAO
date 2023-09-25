import numpy as np
def limpa(): return print("\033[2J\033[;H", end='')


limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
# -----------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''
2. Leia um conjunto de números reais, armazenando-os em um vetor, e calcule o 
   quadrado de cada componente desse vetor, armazenando o resultado em outro 
   vetor. Ambos os conjuntos possuem 10 elementos. Imprima os conjuntos.    '''

# Declara dois vetores
vetor = np.zeros(5)
vetor_quadrado = np.zeros(5)

# Lê os números reais do usuário
for i in range(5):
    numero = float(input("Digite um número real: "))
    vetor[i] = numero

# Calcula o quadrado de cada componente do vetor
for i in range(5):
    vetor_quadrado[i] = vetor[i] * vetor[i]

# Imprime os vetores
print("Vetor original:", vetor)
print("Vetor dos quadrados:", vetor_quadrado)
