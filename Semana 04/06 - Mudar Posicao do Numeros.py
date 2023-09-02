limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

'''
6) Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois
   modiﬁque o programa para que ele mostre os números um ao lado do outro.
'''

for i in range(1, 21):
    print(f"{i}")
   
for i in range(1, 21):
    print(i,", ",end="")
