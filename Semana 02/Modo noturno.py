limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

""" #----------------------------------------------------------
    Arraias - TO => 2023 => UFT - Lincenciatura em Computação
    Disciplina => Programação de Computadores
    @Autor => Wenes Aquino => 2º Períldo
"""#-----------------------------------------------------------

"""
Escreva um programa em Python que solicite ao usuário se ele deseja ativar o modo
noturno (sim ou não). O programa deve exibir a mensagem "Modo noturno ativado!" se o usuário
responder "sim", e a mensagem "Modo noturno desativado!" se o usuário responder "não"
"""

opcao = input("Deseja ativar o modo noturno (sim ou não)?\n")

if opcao == "sim":
   print("Modo noturno ativado")
        
elif opcao == "nao":
   print("Modo noturno desativido")
    
else:
   print("Opção invalida")