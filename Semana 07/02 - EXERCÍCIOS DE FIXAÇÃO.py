limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''
2. Desenvolva um programa que veriﬁque se uma palavra é um anagrama de outra palavra
fornecida pelo usuário.'''

# Obtém as palavras do usuário.

palavra1 = input("Digite a primeira palavra: ")
palavra2 = input("Digite a segunda palavra: ")

# Verifica se as palavras têm o mesmo comprimento.

if len(palavra1) != len(palavra2):
    print("As palavras não são anagramas.")
    exit()

# Cria um dicionário para contar o número de ocorrências de cada letra na primeira palavra.

dicionario1 = {}
for letra in palavra1:
    if letra in dicionario1:
        dicionario1[letra] += 1
    else:
        dicionario1[letra] = 1

# Cria um dicionário para contar o número de ocorrências de cada letra na segunda palavra.

dicionario2 = {}
for letra in palavra2:
    if letra in dicionario2:
        dicionario2[letra] += 1
    else:
        dicionario2[letra] = 1

# Verifica se os dois dicionários são iguais.

for letra in dicionario1:
    if letra not in dicionario2:
        print("As palavras não são anagramas.")
        break
    elif dicionario1[letra] != dicionario2[letra]:
        print("As palavras não são anagramas.")
        break

# As palavras são anagramas.

print("As palavras são anagramas.")
