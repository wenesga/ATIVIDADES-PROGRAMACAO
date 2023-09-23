limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#------------------------------------------------------------------------------

# Criar um dicionário para armazenar nomes de alunos e suas notas
alunos_notas = {}

# Pedir ao usuário para inserir os dados dos alunos
n = int(input("NUMERO DE ALUNOS: "))

for i in range(n):
    
    nome = input("NOME: ")
    notas = input("NOTAS: ").split()

    notas = [float(x) for x in notas]
    media = sum(notas) / len(notas)
    alunos_notas[nome] = media

# Encontrar o aluno com a maior média
aluno_maior_media = max(alunos_notas, key=alunos_notas.get)
maior_media = alunos_notas[aluno_maior_media]

# Exibir o nome e a nota do aluno com a maior média
print(f"Aluno com a maior média: {aluno_maior_media}, Média: {maior_media}")
