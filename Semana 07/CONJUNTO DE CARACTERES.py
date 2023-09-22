limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------
conjunto = set()

for letra in "abcdewerwre":
    conjunto = set(letra).union(conjunto)

print('Conjunto Letra:', conjunto)



for letra in "abcdewerwre":
    conjunto.add('www')

print('Conjunto Letra:', conjunto)