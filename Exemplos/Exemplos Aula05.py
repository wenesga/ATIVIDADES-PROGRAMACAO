limpa = lambda: print("\033[2J\033[;H", end='') #Função limpa console
limpa() #Limpa console

"""
Arraias - TO - 2023
UFT - Lincenciatura em Computação
Disc: Programação de Computadores
@Autor: Wenes Aquino - 2º Períldo
"""

nome = input("digite nome: ")
idade = int(input(f"digite idade {nome}: "))
nascimento = 2023 - idade

print(f"""Seu é {nome} e 
Tem {idade} anos e 
Nasceu em {nascimento}""")






























