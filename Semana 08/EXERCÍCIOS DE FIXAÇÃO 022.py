def limpa(): return print("\033[2J\033[;H", end='')


limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
# -----------------------------------------------------------------------------
# EXERCÍCIOS DE FIXAÇÃO
'''
2. Leia um conjunto de números reais, armazenando-os em um vetor, e calcule o 
   quadrado de cada componente desse vetor, armazenando o resultado em outro 
   vetor. Ambos os conjuntos possuem 10 elementos. Imprima os conjuntos.    '''

# Inicializa os vetores
vetor_original = []
vetor_quadrado = []

# Lê os números reais e os armazena no vetor_original
for i in range(4):
    numero = float(input(f"Digite o {i+1}º número real: "))
    vetor_original.append(numero)

# Calcula o quadrado de cada componente e armazena no vetor_quadrado
for numero in vetor_original:
    quadrado = numero ** 2
    vetor_quadrado.append(quadrado)

# Imprime os conjuntos
print("Vetor Original:", vetor_original)
print("Vetor dos Quadrados:", vetor_quadrado)
