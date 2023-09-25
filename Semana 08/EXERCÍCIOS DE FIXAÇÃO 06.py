def limpa(): return print("\033[2J\033[;H", end='')


limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
# -----------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''
6. Escreva um programa que leia 10 números inteiros e os armazene em um vetor. 
   Imprima o vetor, o maior elemento e a posição em que ele se encontra.  '''

# Declara um vetor de 10 posições
vetor = []

# Lê os valores do vetor
for i in range(5):
    numero = int(input("Digite o valor da posição %d: " % i))
    vetor.append(numero)

# Declara a variável do maior valor
maior = vetor[0]
posicao_maior = 0

# Itera sobre o vetor para encontrar o maior valor
for i in range(1, len(vetor)):
    if vetor[i] > maior:
        maior = vetor[i]
        posicao_maior = i

# Imprime o vetor
print("Vetor:", vetor)

# Imprime o maior valor
print("O maior valor do vetor é:", maior)

# Imprime a posição do maior valor
print("A posição do maior valor é:", posicao_maior)
