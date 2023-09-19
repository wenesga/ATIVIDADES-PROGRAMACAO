limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO - 02
'''
2. Desenvolva um programa que veriﬁque se uma palavra é um anagrama de outra palavra
   fornecida pelo usuário.'''
# Passos:
# 1 - Obtém as palavras do usuário. => ok
# 2 - Verifica se as palavras têm o mesmo comprimento. => ok
# 3 - Cria um dicionário para contar o número de ocorrências de cada letra na 1ª palavra. => ok
# 4 - Cria um dicionário para contar o número de ocorrências de cada letra na 2ª palavra. => ok
# 5 - Verifica se os dois dicionários são iguais.
# 6 - As palavras são anagramas.

import sys # fornece acesso a informações sobre o sistema operacional e o ambiente de execução
import os

nome_arquivo = sys.argv[0]                 # Obtém o nome do arquivo Python que está sendo executado.
nome_puro = os.path.basename(nome_arquivo) # Obtém o nome do arquivo sem o caminho.
print(nome_puro)                           # Imprime o nome do arquivo.

#----------------------------------------Obtém as palavras do usuário.
palavra_1 = input("Digite a 1ª palavra => ")
palavra_2 = input("Digite a 2ª palavra => ")
#----------------------------------------Corverte caixa Alta para Baixa
palavra_1 = palavra_1.lower()
palavra_2 = palavra_2.lower()
#----------------------------------------Verifica se as palavras têm o mesmo comprimento.
if len(palavra_1) != len(palavra_2):
    print("Não é Anagrama")
    sys.exit() # Encerrar o progrma
#----------------------------------------Cria dicionário para contar ocorrências de cada letra na 1ª palavra.    
dic_1 = {}
for letra in palavra_1:
    if letra in dic_1: 
        dic_1[letra] = dic_1[letra] + 1
    else:
        dic_1[letra] = 1
#----------------------------------------Cria dicionário para contar ocorrências de cada letra na 2ª palavra.
dic_2 = {}
for letra in palavra_2:
    if letra in dic_2:
        dic_2[letra] = dic_2[letra] + 1
    else:
        dic_2[letra] = 1
#----------------------------------------Verifica se os dois dicionários são iguais. 
for letra in dic_1:
    if letra not in dic_2:
        print("Não é Anagrama")
        sys.exit() # Encerrar o progrma
    elif dic_1[letra] != dic_2[letra]:
        print("Não é Anagrama")
        sys.exit() # Encerrar o progrma
#----------------------------------------# # As palavras são anagramas.
print(f"São Anagrama: ({palavra_1}) <=> ({palavra_2}) ") 





