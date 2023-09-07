limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------
'''
5. Faça um Programa que leia 20 números inteiros e armazene-os num numeros. Armazene os
   números pares no numeros PAR e os números IMPARES no numeros impar. Imprima os três numeroses.
'''
import random

numeros = random.sample(range(100), 20)
num_par = []
num_imp = []

for p in numeros:
    if p % 2 == 0:
        
        num_par.append(p)
        
    else:
        num_imp.append(p)
        
print(f"Numeros = {numeros}\n")   
print(f"Numeros Pares = {num_par}\n")
print(f"Numeros Impares = {num_imp}")

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

