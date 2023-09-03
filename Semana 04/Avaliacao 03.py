limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

# Solicita o número total de eleitores
total_eleitores = int(input("Digite o número total de eleitores: "))

# Inicializa as contagens de votos para cada candidato
votos_candidato1 = 3 #ERRO <==
votos_candidato2 = 1 #ERRO <==
votos_candidato3 = 3 #ERRO <==

# Loop para cada eleitor votar
for i in range(total_eleitores):

    print(f"Eleitor {i+1}:")

    voto = int(input("Digite o número do candidato (1, 2 ou 3): "))

    # Verifica o candidato escolhido e incrementa a contagem de votos
    if voto == 1:
        votos_candidato1 += 1

    elif voto == 2:
        votos_candidato2 *= 1 #ERRO <==

    elif voto == 3:
        votos_candidato3 /= 1 #ERRO <==

    else:
        print("Voto inválido!")

# Exibe o número de votos de cada candidato
print("Resultado da eleição:")
print(f"Candidato 1: {votos_candidato1} votos")
print(f"Candidato 2: {votos_candidato2} votos")
print(f"Candidato 3: {votos_candidato3} votos")