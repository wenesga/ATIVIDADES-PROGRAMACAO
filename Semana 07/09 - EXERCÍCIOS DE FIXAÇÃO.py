limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#------------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''9. Escreva um programa que remova todos os elementos de uma lista 
      que também estão presentes em outra lista.'''

# Transforma string em uma lista e converte a lista para conjunto
lista1 = set(input("Digite a 1º lista: ").split())
lista2 = set(input("Digite a 2º lista: ").split())

# Imprime os dois conjunto
print('Conjuto1 =', lista1)
print('Conjuto2 =', lista2)

# Verifica a diferença entre os dois conjuntos
if len(lista1) > len(lista2):
    diferenca = lista1.difference(lista2)
else:
    diferenca = lista2.difference(lista1)
print("Diferença = ", diferenca)