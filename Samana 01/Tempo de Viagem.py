limpa = lambda: print("\033[2J\033[;H", end='') #Função limpa console
limpa() #Limpa console

""" 
Arraias - TO - 2023
UFT - Lincenciatura em Computação
Disc: Programação de Computadores
@Autor: Wenes Aquino - 2º Períldo
"""

distancia = float(input("Digite a Distância em km: "))
velociadeMedia = float(input("Digite Vel média em km/h: "))

tempo   = distancia / velociadeMedia
horas   = int(distancia) // int(velociadeMedia)
minutos = int((tempo - horas)* 60)

print(f"         Tempo de viagem: {horas}h:{minutos}min")