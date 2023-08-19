limpa = lambda: print("\033[2J\033[;H", end='')
limpa()#------------------------------------------------------------
""" Arraias - TO <=> 2023 <=> UFT - Lincenciatura em Computação
    Disc <=> Programação de Computadores
    @Autor => Wenes Aquino -> 2º Períldo
"""    #------------------------------------------------------------

# FUNÇÃO 18/08/2023

# def sanduiche(nome):
#     print(f'Fazer sanduiche para {nome}')
    
# def batata(tamanho):
#     print(f'Batata {tamanho}')
    
# def refrigerante(tipo, tamanho):
#     print(f'{tipo} {tamanho}')

# def fazer_combo(nome, tamanhoBat, tipo, tamanhoRefr):
#     sanduiche(nome)
#     batata(tamanhoBat)
#     refrigerante(tipo, tamanhoRefr)

# fazer_combo('Wenes', 'Grande', 'Coca', 'Pequeno\n')
# fazer_combo('Aquino', 'Medio', 'Peps', 'Grande\n')
# fazer_combo('Gomes', 'Pequeno', 'Fanta', 'Pequeno\n')


# def soma_numero(num1, num2):
#     return num1 + num2 

# n1 = int(input('Digite1: '))
# n2 = int(input('Digite2: '))

# print(n1, "+", n2,"=", soma_numero(n1, n2))


def mairo_numero(lista_num):
    lista_num.sort() #ordena numeros
    lista_num.reverse() #numeros ordem reversa
    maior_num = lista_num[0] #primeiro numero da lista
    
    return maior_num

print(mairo_numero([42,6,812,7,3,1,13,14]))







