limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO - 04
'''
4. Crie um programa que calcule a média das notas dos alunos de 
   uma turma. Os dados devem ser armazenados em um dicionário, 
   onde a chave é o nome do aluno e o valor é uma lista de notas.'''

alunos = [{'Wenes': [90, 100, 80]},
          {'Gomes': [80, 50, 68]},
          {'Aquino': [50, 50, 50]}]

soma = 0

for aluno in alunos:   
    print(aluno)
    
    for notas in aluno.values():
        
        for nota in notas:
            soma = soma + nota
        
        media = soma / len(notas)
        print('Média =', media,'\n')
        soma = 0
        
        
        
        
        