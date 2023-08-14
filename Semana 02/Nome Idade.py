limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

""" #----------------------------------------------------------
    Arraias - TO => 2023 => UFT - Lincenciatura em Computação
    Disciplina => Programação de Computadores
    @Autor => Wenes Aquino => 2º Períldo
"""#-----------------------------------------------------------

"""
Faça um programa em Python que solicite ao usuário o seu nome e idade. Em seguida,
exiba na tela uma mensagem contendo o nome e a idade informados pelo usuário.
"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

print(f"""
      Nome: {nome}
      Idade: {idade} anos
""")
