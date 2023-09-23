def limpa(): return print("\033[2J\033[;H", end="")


limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
# -----------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
"""
1. Crie um programa que conte a quantidade de ocorrências de cada 
palavra em um texto fornecido pelo usuário."""

texto = input("Digite um texto: ")

lista_palavras = texto.split()
contagem = {}

for palavra in lista_palavras:
    if palavra in contagem:
        contagem[palavra] = contagem[palavra] + 1

    else:
        contagem[palavra] = 1

print(f"\nLista de contagem = {contagem}\n")

for palavra, quantidade in contagem.items():
    print(f"{palavra} => {quantidade}")
