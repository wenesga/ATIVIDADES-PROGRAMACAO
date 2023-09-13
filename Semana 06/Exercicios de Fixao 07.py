limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

'''7. Crie uma lista de tuplas para representar uma tabela de classiﬁcação de um campeonato.
Cada tupla deve conter o nome do time e sua pontuação.'''

classificacao_campeonato = [
    ("Time A", 15),
    ("Time B", 12),
    ("Time C", 10),
    ("Time D", 8),
    ("Time E", 5)
]

print(classificacao_campeonato)