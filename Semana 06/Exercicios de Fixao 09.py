limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

'''9. Crie uma lista de tuplas para armazenar informações sobre livros. Cada tupla deve conter
título, autor e ano de publicação de um livro. Escreva um programa que ordene a lista de
acordo com o ano de publicação.'''

# Crie a lista de tuplas com informações sobre livros
livros = [
    ("Livro 1", "Autor 1", 2005),
    ("Livro 2", "Autor 2", 1998),
    ("Livro 3", "Autor 3", 2010),
    ("Livro 4", "Autor 4", 1985),
    ("Livro 5", "Autor 5", 2021)
]

# Ordene a lista de acordo com o ano de publicação (do mais antigo para o mais recente)
livros_ordenados = sorted(livros, key=lambda livro: livro[2])

# Exiba a lista de livros ordenada
print("Lista de Livros Ordenada por Ano de Publicação:")
for livro in livros_ordenados:
    print(f"Título: {livro[0]}, Autor: {livro[1]}, Ano de Publicação: {livro[2]}")
