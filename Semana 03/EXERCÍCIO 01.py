limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

""" #----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

"""
1) Desenvolva um algoritmo em Python para veriﬁcar se um aluno foi aprovado 
em uma disciplina. O algoritmo deve solicitar ao usuário que digite a nota do 
aluno e veriﬁcar se a nota é maior ou igual a 7. Caso a nota seja maior ou 
igual a 7, o algoritmo deve exibir a mensagem "Aluno aprovado". Caso contrário, 
o algoritmo deve exibir a mensagem "Aluno reprovado".
"""

nota = float(input("Digite a nota do aluno: "))

if(nota >= 7):
    print('Aluno Aprovado')
    
else:
    print('Aluno Reprovado')