limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#------------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''10. Crie um programa que leia uma lista de nomes de alunos e suas 
       respectivas notas, armazenando essas informações em um dicionário. 
       Em seguida, exiba o nome e a nota do aluno com a maior média. '''

lista_alunos = {
    'Wenes': [98, 95, 86],
    'Gomes': [43, 77, 96],
    'Marco': [45, 52, 53],
    'Maria': [85, 85, 85]
}

maior_media = 0
nome_maior_nota = ''

for nome, notas in lista_alunos.items():

    soma = 0
    for nota in notas:
        soma = soma + nota
    media = soma / len(notas)

    print(f'Aluno = {nome} {notas} = {media}')

    if media > maior_media:
        maior_media = media
        nome_maior_nota = nome

print(f'\nMaior Média: Aluno = {nome_maior_nota} = {maior_media}')