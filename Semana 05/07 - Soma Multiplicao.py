limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

''' 7. Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
    multiplicação e os números.'''
    
import random

numeros = random.sample(range(10), 5)

add = 0
mul = 1

for i in numeros:
    
    add = add + i
    mul = mul * i
    
print(f"Soma  dos  Numeros : {numeros} = {add}")
print(f"Produto dos Numeros: {numeros} = {mul}")



