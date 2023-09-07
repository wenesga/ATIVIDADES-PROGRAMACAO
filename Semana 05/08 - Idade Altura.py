limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

'''8. Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação
   no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.'''
   
lista_idade = []
lista_altura = []
altura = 0
idade = 0

for pessoa in range(1, 3):
    
    for altura in range(1, 2):
        idade = int(input(f"Digite idade da {pessoa}ª Pessoa: "))
        lista_idade.append(idade)
        altura = float(input(f"Digite altura da {pessoa}ª Pessoa: "))
        lista_altura.append(altura)
        print('\n')
        
print(f"Lista de Idade = {lista_idade}") 
print(f"Lista de Altura = {lista_altura}")

lista_idade.reverse()
lista_altura.reverse()

print(f"\nLista de Idade Invertida = {lista_idade}") 
print(f"Lista de Altura Invertida = {lista_altura}")

