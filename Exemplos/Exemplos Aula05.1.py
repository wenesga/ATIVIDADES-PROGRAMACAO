limpa = lambda: print("\033[2J\033[;H", end='') #Função limpa console
limpa() #Limpa console
#--------------------------------------------------------------------
""" Arraias - TO - 2023
    UFT - Lincenciatura em Computação
    Disc: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""
#--------------------------------------------------------------------

numero1 = int(input("Digite um numero: "))
numero2 = int(input("Digite outro numero: "))
resultado = numero1 * numero2

print(f"{numero1} x {numero2} = {resultado}")