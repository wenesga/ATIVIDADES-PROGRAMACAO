limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

agenda = []

while True:
    nome = input("Digite o nome do contato ou N (Sair) : ")
    
    if nome.lower() == 'n':
        break  
    
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    
    contato = {'nome': nome, 'telefone': telefone, 'email': email}
    agenda.append(contato)

print("Lista de Contatos:")
for contato in agenda:
    print(contato)
