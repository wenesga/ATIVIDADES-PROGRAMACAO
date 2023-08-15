limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

""" #----------------------------------------------------------
    Arraias - TO => 2023 => UFT - Lincenciatura em Computação
    Disciplina => Programação de Computadores
    @Autor => Wenes Aquino => 2º Períldo
"""#-----------------------------------------------------------

""" 
    Escreva um programa em Python que solicite ao usuário a quantidade de horas
    trabalhadas por mês e o valor da hora de trabalho, e calcule o salário mensal.
"""

horas_trabalho = int(input("Digite as horas trabalhadas: "))
valor_horas = float(input("Digite o valor da hora: "))

salario_mensal = horas_trabalho * valor_horas

print(f"Salario = {salario_mensal}")