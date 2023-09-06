limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

# Lê um vetor de 10 caracteres
vetor = []
for i in range(10):
    vetor.append(input("Digite um caractere: "))

# Inicializa a contagem de consoantes
count_consoantes = 0
consoantes = []

# Verifica se cada caractere é uma consoante
for caractere in vetor:
    if caractere.isalpha() and caractere.upper() not in ['A', 'E', 'I', 'O', 'U']:
        count_consoantes += 1
        consoantes.append(caractere)

# Imprime a quantidade de consoantes e as consoantes encontradas
print("Quantidade de consoantes:", count_consoantes)
print("Consoantes:", consoantes)