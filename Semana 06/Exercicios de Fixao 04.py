limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

'''4. Crie uma lista de tuplas para armazenar as coordenadas (x, y) de pontos em um plano
cartesiano. Escreva um programa que calcule a distância entre dois pontos.'''

coordenadas = [(1, 2), (3, 4), (5, 6)]

ponto1 = coordenadas[0]
ponto2 = coordenadas[2]

x1, y1 = ponto1
x2, y2 = ponto2

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print(distancia)