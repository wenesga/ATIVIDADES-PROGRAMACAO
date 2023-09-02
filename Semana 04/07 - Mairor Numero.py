limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

'''
7) Faça um programa que leia 5 números e informe o maior número.
'''

numeros = []

for i in range(1, 6):
    
    numero = float(input("Digite um número: "))
    numeros.append(numero)

maior_numero = max(numeros)
print(f"O maior número é: {maior_numero}")
