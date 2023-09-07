limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

'''6. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor
   a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.'''
lista_media = []
lista_aprovado = []

for a in range(1, 3):
    
    soma = 0
    for n in range(1, 5):
        nota = float(input(f"Digite a {n}ª Nota do {a}º Alino: "))
        soma = soma + nota
    
    media = soma / 4
    print(f"Soma = {soma}")
    print(f"Média = {media}\n") 
    lista_media.append(media)
    
    if media >= 7:
        lista_aprovado.append(media)

num_aprov = len(lista_aprovado)
        
print(f"\nLista de Médias = {lista_media}") 
print(f"Lista Aprovados = {lista_aprovado}")
print(f"Numero Aprovados = {num_aprov}")