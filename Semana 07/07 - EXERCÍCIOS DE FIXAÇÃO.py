limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#------------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''7. Crie um programa que encontre a interseção de vários conjuntos fornecidos 
   pelo usuário.'''

conjuntos = []
cont = 0

while True:
    cont += 1
    conjunto = input(f"{cont}º Conjunto ou 'n'(sair): ").split()

    if conjunto == ['n']:
        break
    else:
        conjuntos.append(set(conjunto))
        intersesao = set.intersection(*conjuntos)

if intersesao == set():
    print("Náo exite intersesao")
else:
    print('Intersesao: ', intersesao)






















