limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

"""#----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

while True:
    
    nome = input("Digite seu nome => ")
    senha = input("Crie uma senha  => ")
    
    if nome == senha:
        
        print("\nA senha nao pode ser igual ao seu nome!\nTente novamente!\n")
   
    else:
        print("\nSucesso!")
        break