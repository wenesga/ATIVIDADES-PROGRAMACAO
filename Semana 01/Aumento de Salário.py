limpa = lambda: print("\033[2J\033[;H", end='') #Função limpa console
limpa() #Limpa console

""" 
Arraias - TO - 2023
UFT - Lincenciatura em Computação
Disc: Programação de Computadores
@Autor: Wenes Aquino - 2º Períldo
"""

salario = float(input("Digite o salário: "))
porcentAumento = float(input("Digite porcentagem de aumento: "))

aumentoSalario = salario * porcentAumento / 100
novoSalario = salario + aumentoSalario

print("Salario aumentou: R$", aumentoSalario)
print("Novo salário é: R$", novoSalario)