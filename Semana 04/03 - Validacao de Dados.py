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
        print("Nome deve ser maior que 3 caracteres")
        
while True:
    idade = int(input("Digite sua idade: "))
    if idade > 0 and idade < 150:
        break
    else:
        print("Idade deve ser entre 0 e 150")
        
while True:
    salario = float(input("Digite seu salario: "))
    if salario > 0:
        break
    else:
        print("Salário deve ser maior que zero")
        
while True:
    sexo = input("Digite seu sexo: 'f' ou 'm': ")
    if sexo == "f" or sexo == "m":
        break
    else:
        print("Sexo deve ser: 'f' ou 'm'")
        
while True:
    estado_civil = input("Digite seu Estado Civil: 's', 'c', 'v', 'd': ")
    if estado_civil == "s" or estado_civil == "c" or estado_civil == "v" or estado_civil == "d":
        break
    else:
        print("Estado Civil deve ser: 's', 'c', 'v', 'd'")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        