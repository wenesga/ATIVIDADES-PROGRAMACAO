limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------
'''
Programa que calcula o valor total investido por um colecionador em sua coleção 
de Discos e o valor médio gasto. O usuário deverá informar a quantidade de 
discos e o valor para cada um. 
'''
# Solicita a quantidade de discos na coleção
quantidade_discos = int(input("Digite a quantidade de discos na coleção: "))

# Inicializa a variável para armazenar o valor total investido
valor_total = 0

# Loop para receber o valor de cada disco
for i in range(1,quantidade_discos):       #ERRO <==
    valor_disco = float(input(f"Digite o valor do disco {i+1}: "))
    valor_total += valor_disco
    
# Calcula o valor médio gasto por disco
valor_medio_por_disco = valor_total / quantidade_discos

# Exibe os resultados
print("Resumo da coleção:")
print(f"Valor total investido: R${valor_total:.2f}")
print(f"Valor médio por disco: R${valor_medio_por_disco:.2f}")