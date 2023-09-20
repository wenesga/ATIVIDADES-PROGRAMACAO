limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''
5. Desenvolva um programa que remova os elementos duplicados de uma 
   lista e retorne uma nova lista sem duplicatas.'''
   
texto = 'programa uma programa elementos duplicatas uma lista retorne uma lista duplicatas'
print('TEXTO: ',texto)

lista1 = texto.split()
print('\nLISTA COM ELEMENTOS DUPLICADOS: \n', lista1)

lista2 = set(lista1)
print('\nNOVA LISTA SEM DUPLICATAS: \n', lista2)

















