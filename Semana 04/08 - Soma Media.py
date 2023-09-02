limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

'''
8) Faça um programa que leia 5 números e informe a soma e a média dos números.
'''

numeros = []

for i in range(5):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)

print(f"Soma dos números: {soma}")
print(f"Média dos números: {media}")
