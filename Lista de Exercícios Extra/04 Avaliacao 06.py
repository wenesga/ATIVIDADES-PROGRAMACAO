limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

pessoas = []

for i in range(4):

    print(f"Cadastro da pessoa {i + 1}:")

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    cpf = input("CPF: ")
    pessoa = {"Nome": nome, "Idade": idade, "CPF": cpf}
    pessoas.append(pessoa)

pessoas_2 = []

for pessoa in pessoas:

    if pessoa["Idade"] < 18:
        pessoas_2.append(pessoa)
        pessoas.remove(pessoa)

print("\nPessoas 1:")

for pessoa in pessoas:
    print(pessoa)

print("\nPessoas 2:")

for pessoa in pessoas_2:
    print(pessoa)