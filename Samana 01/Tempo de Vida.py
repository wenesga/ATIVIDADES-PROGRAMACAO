limpa = lambda: print("\033[2J\033[;H", end='') #Função limpa console
limpa() #Limpa console

""" 
Arraias - TO - 2023
UFT - Lincenciatura em Computação
Disc: Programação de Computadores
@Autor: Wenes Aquino - 2º Períldo
"""
"""
1 ano = 365 dias
1h = 60min
1dia  = 24h = (24*60) = 1440 min.
"""
cigPorDia = int(input("Quantos cigarros por dia: "))
anosFuman = int(input("Quantos anos você fuma: "))

diasVida = int((cigPorDia * anosFuman) * 10 * 365 / 1440)

print(f"Você perderá {diasVida} dias de vida")







