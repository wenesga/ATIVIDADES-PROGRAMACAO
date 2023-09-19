limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

# Exemplo de `break`

for letra in "abc":
  if letra == "b":
    break
  print(letra)

# Exemplo de `exit()`

idade = 20

if idade < 18:
  print("Você é menor de idade.")
  exit()
else:
  print("Você é maior de idade.")
