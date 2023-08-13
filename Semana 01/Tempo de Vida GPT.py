limpa = lambda: print("\033[2J\033[;H", end='') #Função limpa console
limpa() #Limpa console

""" 
Arraias - TO - 2023
UFT - Lincenciatura em Computação
Disc: Programação de Computadores
@Autor: Wenes Aquino - 2º Períldo
"""

def calculoVida():
    try:
        cigPorDia = int(input("Quantos cigarros por dia: "))
        anosFuman = int(input("Há quantos anos fumando: "))

        totalCiga = cigPorDia * anosFuman * 365
        tempMinut = totalCiga * 10
        tempoDias = tempMinut / (24 * 60)

        print("Você perderá {:.2f} dias de vida.".format(tempoDias))
    
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

calculoVida()
