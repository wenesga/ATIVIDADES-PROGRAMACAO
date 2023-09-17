limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

'''3. Escreva um programa que calcule a média das notas de uma turma de alunos. 
      Utilize uma lista de dicionários, onde cada dicionário representa um aluno 
      com nome e notas em diferentes disciplinas.'''

alunos = [{"Nome": "Wenes", "notas": [8, 9, 10]},
          {"Nome": "Aquino", "notas": [7, 8, 9]},
          {"Nome": "Gomes", "notas": [6, 7, 8]}]

soma = 0
total_notas = 0

for aluno in alunos:
    for nota in aluno["notas"]:
        soma = soma + nota

    total_notas = total_notas + len(aluno["notas"])

media = soma / total_notas

print("Média da turma = ", media)