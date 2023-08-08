""" 
Arraias - TO - 2023
UFT - Lincenciatura em Computação
Disc: Programação de Computadores
@Autor: Wenes Aquino - 2º Períldo
"""

inteiro = int(input("Digite quantidade de horas: "))

# Conversão para dias
dias = inteiro // 24
# Conversão para horas
horas = inteiro % 24
# Exibe o resultado na tela
print(f"{inteiro} horas = {dias} dias e {horas} horas.")