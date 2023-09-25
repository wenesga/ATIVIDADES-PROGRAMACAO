def limpa(): return print("\033[2J\033[;H", end='')


limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
# -----------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''
5. Faça um programa que receba do usuário um vetor com 10 posições. Em seguida, 
   deverá ser impresso o maior e o menor elemento do vetor. '''

# Declara um vetor de 10 posições
vetor = []

# Lê os valores do vetor
for i in range(3):
    numero = float(input("Digite o valor da posição %d: " % i))
    vetor.append(numero)

# Declara as variáveis do maior e do menor valor
maior = vetor[0]
menor = vetor[0]

# Itera sobre o vetor para encontrar o maior e o menor valor
for numero in vetor:
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

# Imprime o maior e o menor valor
print("O maior valor do vetor é: %.2f" % maior)
print("O menor valor do vetor é: %.2f" % menor)
