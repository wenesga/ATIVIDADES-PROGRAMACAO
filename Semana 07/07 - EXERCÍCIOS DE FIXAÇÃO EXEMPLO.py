limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#------------------------------------------------------------------------------

# Inicialize uma lista para armazenar os conjuntos fornecidos pelo usuário
conjuntos = []

# Peça ao usuário para inserir o número de conjuntos
num_conjuntos = int(input("Quantos conjuntos você deseja inserir? "))

# Solicite ao usuário que insira os conjuntos e adicione-os à lista
for i in range(num_conjuntos):
    elementos = input(f"Insira os elementos do conjunto {i+1} separados por espaços: ")
    conjunto = set(elementos.split())
    conjuntos.append(conjunto)

# Calcule a interseção dos conjuntos usando a função intersection()
intersecao = set.intersection(*conjuntos)

# Exiba o resultado
print("A interseção dos conjuntos fornecidos é:", intersecao)
