limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

# Inicializa as variáveis para armazenar o número e altura do aluno mais alto e mais baixo
aluno_mais_alto = 0
altura_mais_alta = 0
aluno_mais_baixo = 0
altura_mais_baixa = float('inf') # Inicializa com um valor infinito

# Loop para receber os valores dos alunos
for i in range(1, 3): # Lê 4 conjuntos de valores
     numero_aluno = int(input(f"Digite o número do aluno {i}: "))
     altura_aluno = float(input(f"Digite a altura do aluno {i} (cm): "))
     
     # Verifica se é o aluno mais alto
     if altura_aluno > altura_mais_alta:
          aluno_mais_alto = numero_aluno
          altura_mais_alta = altura_aluno
     
     # Verifica se é o aluno mais baixo
     if altura_aluno < altura_mais_baixa:
           aluno_mais_baixo = numero_aluno
           altura_mais_baixa = altura_aluno

# Resultados mais alto
print("Aluno mais alto:")
print(f"Número: {aluno_mais_alto}")
print(f"Altura: {altura_mais_alta} cm")

# Resultados mais baixo
print("Aluno mais baixo:")
print(f"Número: {aluno_mais_baixo}")
print(f"Altura: {altura_mais_baixa} cm")







