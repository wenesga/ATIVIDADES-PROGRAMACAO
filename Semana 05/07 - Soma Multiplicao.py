limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

''' 7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
    multiplicação e os números.'''
    
import random
import functools

numeros = random.sample(range(10), 3)

soma = sum(numeros)
mult = functools.reduce(lambda a, b: a * b, numeros)

    
print(f"Soma  dos  Numeros : {numeros} = {soma}")
print(f"Produto dos Numeros: {numeros} = {mult}")



