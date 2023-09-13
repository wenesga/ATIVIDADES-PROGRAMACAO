limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

'''5. Implemente um programa que simule uma lista de reprodução de músicas. Utilize uma
lista de dicionários, onde cada dicionário representa uma música com informações como
título, artista e duração.'''

import random

lista_musicas = [{"Titulo": "Lucille", "Artista": "B.B. King", "Duração": "10:13"},
                 {"Titulo": "Ghost of Perdition", "Artista": "Opeth", "Duração": "5:10"},
                 {"Titulo": "Achilles Last Stand", "Artista": "Led Zeppelin", "Duração": "10:00"}]

num = random.randint(0, 2)

print(f"{num+1}ª - {lista_musicas[num]}")