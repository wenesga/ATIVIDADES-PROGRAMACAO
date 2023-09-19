limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

# Exemplo 1:
x = 1
my_list = [x, 2, 3, 4, 5]

if x in my_list:
    print("3 está na lista")
else:
    print("3 não está na lista")

# Saída:
# 3 está na lista

# Exemplo 2:
my_string = "Hello, world!"

if "world" in my_string:
    print("A palavra 'world' está na string")
else:
    print("A palavra 'world' não está na string")

# Saída:
# A palavra 'world' está na string