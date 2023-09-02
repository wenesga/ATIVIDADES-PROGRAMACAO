limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

'''
5) Altere o programa anterior permitindo ao usuário informar as populações e as taxas de
   crescimento iniciais. Valide a entrada e permita repetir a operação.
'''

populacao_pais_A = float(input("Digite numero da populacao A: "))
taxa_cres_pais_A = float(input("Digite taxa de crescimento da populacao A: "))

populacao_pais_B = float(input("Digite numero da populacao B: "))
taxa_cres_pais_B = float(input("Digite taxa de crescimento da populacao B: "))

ano = 0

while populacao_pais_A < populacao_pais_B:
    
    populacao_pais_A = populacao_pais_A + (populacao_pais_A * taxa_cres_pais_A)
    populacao_pais_B = populacao_pais_B + (populacao_pais_B * taxa_cres_pais_B)
    ano = ano + 1
    
print(f"Anos necessarios = {ano}")