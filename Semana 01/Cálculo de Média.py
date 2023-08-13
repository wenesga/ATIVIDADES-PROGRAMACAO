""" 
Arraias - TO - 2023
UFT - Lincenciatura em Computação
Disc: Programação de Computadores
@Autor: Wenes Aquino - 2º Períldo
"""
cls = lambda: print("\033[2J\033[;H", end='') #Função para limpa o console
cls() #Limpa o console

nota1 = input("Digite a nota 1: ")
nota2 = input("Digite a nota 2: ")
nota3 = input("Digite a nota 3: ")

media = (float(nota1) + float(nota2) + float(nota3))/3

print("Média = ", media)
