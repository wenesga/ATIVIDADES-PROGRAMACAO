limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------
'''
4)  Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
    taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com
    uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de
    anos necessários para que a população do país A ultrapasse ou iguale a população do
    país B, mantidas as taxas de crescimento.
'''
# A = 80000 - 3% = 0.3
# B = 200000 - 1.5% = 0.015

pais_A = 80000
pais_B = 200000
ano = 0

while pais_A < pais_B:
    
    pais_A = pais_A + (pais_A * 0.03)
    pais_B = pais_B + (pais_B * 0.015)
    ano = ano + 1
    
print(f"Anos necessarios = {ano}")
    
       
      


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

