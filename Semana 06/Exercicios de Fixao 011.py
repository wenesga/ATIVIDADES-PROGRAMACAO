limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

contatos = []

while True:
    
    nome = input("\nNome: ")
    telefone = input("Telefone: ")
    e_mail = input("E-mail: ")

    contato = {"nome": nome, "telefone": telefone, "e_mail": e_mail}
    contatos.append(contato)

    opcao = input("\nDeseja adicionar mais? (S/N): ")
    
    if opcao.lower() == "n":
        break

print("\nLista de Contatos:\n")

for contato in contatos:
    print(contato)