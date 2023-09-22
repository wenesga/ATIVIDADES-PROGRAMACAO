limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#------------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''8. Desenvolva um programa que veriﬁque se uma lista fornecida pelo 
      usuário está contida em outra lista.'''

# Transforma string em uma lista e converte a lista para conjunto
lista1 = set(input("Digite a 1º lista: ").split())
lista2 = set(input("Digite a 2º lista: ").split())

# Imprime os dois conjunto
print('Conjuto1 =', lista1)
print('Conjuto2 =', lista2)

# Verifica se um conjunto está contido em outro conjunto
if lista1.issubset(lista2):
    print("Conjuto1 está contida em Conjuto2")

elif lista2.issubset(lista1):
    print("Conjuto2 está contida em Conjuto1")

else:
    print("Não existe Subconjuto")