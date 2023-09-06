limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

'''
3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

notas = [90, 100, 85, 98]

soma = 0

for i in notas:
    
    soma = soma + i
    
media = soma / len(notas)  

print(f"Notas = {notas}")
print(f"Media = {media}")
    