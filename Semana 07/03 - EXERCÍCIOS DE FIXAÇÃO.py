def limpa(): return print("\033[2J\033[;H", end='')


limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
# -----------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''
3. Escreva um programa que encontre e imprima os elementos comuns entre duas listas
fornecidas pelo usuário.
 '''

# Solicita as listas ao usuário
lista1 = input("Digite a primeira lista separada por espaços: ").split()
lista2 = input("Digite a segunda lista separada por espaços: ").split()

print(f"\nLista1 = {lista1}")
print(f"Lista2 = {lista2}")

# # Converte as entradas em conjuntos para facilitar a comparação
conjunto1 = set(lista1)
conjunto2 = set(lista2)

print(f"\nConjunto1 = {conjunto1}")
print(f"Conjunto2 = {conjunto2}")

# Encontra os elementos comuns (Intersecçao)
comum = conjunto1.intersection(conjunto2)

# Imprime lista dos elementos comuns
print(f"\nComuns = {comum}")
