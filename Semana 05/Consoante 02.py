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
    
# A função isalpha() verifica se todos os caracteres na string são letras do alfabeto.

# caractere.lower() not in "aeiou" verifica se o caractere não é uma das cinco vogais em minúsculas. 
# Se a expressão retornar True, significa que o caractere não é uma vogal; 
# caso contrário, se retornar False, significa que o caractere é uma vogal.
    
    if caractere.isalpha() and caractere.lower() not in "aeiou": 
        contador_consoantes += 1
        consoantes_lidas.append(caractere)

# Impressão do resultado
print(f"Quantidade de consoantes lidas: {contador_consoantes}")
print(f"Consoantes lidas: {', '.join(consoantes_lidas)}")

# ' ,'.join(consoantes_lidas) une os elementos da lista consoantes_lidas em uma única string, 
# usando ', ' como separador. Isso significa que cada elemento da lista será seguido por uma 
# vírgula e um espaço na string resultante.







