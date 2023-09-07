limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

# Vetor de 10 is
vetor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Inicialização do contador de consoantes e lista de consoantes lidas
contador = 0
consoante = []

# Verificação e contagem de consoantes
for i in vetor:
    if i.isalpha() and i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u':
        contador += 1
        consoante.append(i)

# Vetor de 10 is
print(f"Vetor: {vetor}")

# Impressão do resultado
print(f"Quantidade Consoantes: {contador}")

consoante = ' - '.join(consoante)
print(f"Numero de Consoantes: {consoante}")
