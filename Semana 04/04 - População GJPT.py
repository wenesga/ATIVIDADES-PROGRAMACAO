limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
# taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com
# uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de
# anos necessários para que a população do país A ultrapasse ou iguale a população do
# país B, mantidas as taxas de crescimento.

# Para resolver esse problema, podemos usar um laço de repetição que calcula a 
# população de ambos os países a cada ano até que a população de A ultrapasse ou 
# iguale à população de B.

# Vamos criar duas variáveis para armazenar a população de cada país:

populacao_A = 80000
populacao_B = 200000

# Também vamos criar duas variáveis para armazenar as taxas de crescimento de cada país:

taxa_crescimento_A = 0.03
taxa_crescimento_B = 0.015

# Criamos uma variável "anos" inicialmente igual a zero para contar o número de anos 
# necessários para a população de A ultrapassar ou igualar a população de B:

anos = 0

# Agora, entramos em um laço de repetição que calcula a população de cada país a 
# cada ano até que a população de A seja maior ou igual à população de B:

while populacao_A < populacao_B:
    populacao_A += populacao_A * taxa_crescimento_A
    populacao_B += populacao_B * taxa_crescimento_B
    anos += 1

# Ao final do laço, a variável "anos" terá o número de anos necessários para a 
# população de A ultrapassar ou igualar a população de B.

# Para imprimir o resultado, basta adicionar:

print("Número de anos necessários:", anos)