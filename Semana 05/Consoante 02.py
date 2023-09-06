limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

# Vetor de 10 caracteres
vetor = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Inicialização do contador de consoantes e lista de consoantes lidas
contador_consoantes = 0
consoantes_lidas = []

# Verificação e contagem de consoantes
for caractere in vetor:
    if caractere.isalpha() and caractere.lower() not in "aeiou":
        contador_consoantes += 1
        consoantes_lidas.append(caractere)

# Impressão do resultado
print(f"Quantidade de consoantes lidas: {contador_consoantes}")
print(f"Consoantes lidas: {', '.join(consoantes_lidas)}")
