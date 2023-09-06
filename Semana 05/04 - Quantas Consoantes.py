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

vetor = ["a", "b", "e", "h", "l", "u", "a", "i", "w", "a"]
cont = 0

for i in vetor:
    
    if i!='a' and i!='e' and i!='i' and i!='o' and  i!='u':
        
        print(i, end=' - ')
        cont += 1
        
print("<== Consoantes")
print(f"\nNumero de consoante = {cont}")

        