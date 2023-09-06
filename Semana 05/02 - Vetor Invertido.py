limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

'''
2. Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

nummeros = [1, 2, 3, 5, 10, 14, 22, 30, 51, 100]

nummeros.reverse()

print(nummeros)