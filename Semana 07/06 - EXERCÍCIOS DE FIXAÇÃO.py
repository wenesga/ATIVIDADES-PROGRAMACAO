limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''6. Escreva um programa que conte a quantidade de caracteres 
      repetidos em uma palavra fornecida pelo usuário.'''

palavra = input("Digite uma palavra: ")
palavra = palavra.lower()
conte_letras = {}
conte_repete = 0

for letra in palavra:

    if letra in conte_letras:
        conte_letras[letra] += 1

    else:
        conte_letras[letra] = 1

    if conte_letras[letra] > 1:
        conte_repete += 1

print('Quantidade de cada letra: ', conte_letras)
print('Quantidade de letras que repete: ', conte_repete)















