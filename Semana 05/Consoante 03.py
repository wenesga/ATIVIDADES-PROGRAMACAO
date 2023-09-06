limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

# Função para verificar se um caractere é uma consoante
def eh_consoante(caractere):
    consoantes = "bcdfghjklmnpqrstvwxyz"
    return caractere.lower() in consoantes

# Inicialização do vetor de caracteres
vetor = []

# Leitura dos 10 caracteres
for i in range(10):
    caractere = input("Digite um caractere: ")
    vetor.append(caractere)

# Contagem de consoantes e impressão delas
contador_consoantes = 0
consoantes_lidas = []

for caractere in vetor:
    if eh_consoante(caractere):
        contador_consoantes += 1
        consoantes_lidas.append(caractere)

print(f"Quantidade de consoantes lidas: {contador_consoantes}")
print(f"Consoantes lidas: {', '.join(consoantes_lidas)}")
