limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

'''
3) Faça um programa em python que leia e valide as seguintes informações:
    a) Nome: maior que 3 caracteres;
    b) Idade: entre 0 e 150;
    c) Salário: maior que zero;
    d) Sexo: 'f' ou 'm';
    e) Estado Civil: 's', 'c', 'v', 'd';
    
'''

while True:
    nome = input("Digite seu nome: ")
    
    if len(nome) > 3:
        break
    else:
        print("Nome com mais de 3 caracteres.")