limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

# Criando uma lista heterogênea com diferentes tipos de dados

dados_pessoa = ["João", 25, 1.75, True]

# Acessando elementos da lista

nome = dados_pessoa[0]

idade = dados_pessoa[1]

altura = dados_pessoa[2] * 2

e_maior = dados_pessoa[0]

# Exibindo informações

print("Nome:", nome)

print("Idade:", idade)

print("Altura:", altura)

print("É maior de idade?", e_maior)