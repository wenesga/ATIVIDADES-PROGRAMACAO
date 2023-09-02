limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------
'''
01) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o
    valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

for i in range(0, 10):
    
    nota = int(input("Digite uma nota entre 0 e 10 => "))
    
    if nota > 0 and nota < 10:
        print("Valor válido!")
        break
        
    else:
        print("Valor inválido! Tente novamente\n")
    