limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

'''1. Crie uma lista de dicionários para representar uma agenda de contatos. 
Cada dicionário deve conter informações como nome, telefone e e-mail de uma pessoa.'''

#DICIONARIO

contatos = {}

nome =     input("Digite seu Nome: ")
telefone = input("Digite seu Telefone: ")
e_mail =   input("Digite seu E-mail: ")

contatos["Nome"] = nome
contatos["Telefone"] = telefone
contatos["E-mail"] = e_mail

print(contatos)

