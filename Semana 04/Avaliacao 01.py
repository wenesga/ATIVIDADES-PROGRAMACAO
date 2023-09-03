limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

numeros = []
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)
resposta = max(numeros)
print(resposta)