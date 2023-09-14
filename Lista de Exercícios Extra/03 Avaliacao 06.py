limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

idades = []
alturas = []

for i in range(5):

    print(f"Pessoa {i + 1}:")

    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura (em metros): "))
    idades.append(idade)
    alturas.append(altura)

print("\nIdades:")

for idade in reversed(idades):
    print(idade)

print("\nAlturas:")

for altura in reversed(alturas):
    print(f"{altura:.2f} metros")