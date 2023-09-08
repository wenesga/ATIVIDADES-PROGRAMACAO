limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

'''
4. Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram
   lidas. Imprima as consoantes.
'''
import random
import string

caracteres = string.ascii_lowercase # Cria uma sequência de letras minúsculas
vetor = random.sample(caracteres, 10) # Gera uma lista de 10 letras aleatórias e únicas

# vetor = ["a", "b", "e", "h", "l", "u", "a", "i", "w", "a"]

contador = 0
consoantes = []

for i in vetor:
    
    if i!='a' and i!='e' and i!='i' and i!='o' and  i!='u':

        contador += 1
        consoantes.append(i)

print(f"Caracteres => [{', '.join(caracteres)}]")
print(f"Vetor Caracteres => [{', '.join(vetor)}]")
print(f"Consoantes => [{', '.join(consoantes)}]")
print(f"Quantidade => {contador}")





