limpa = lambda: print("\033[2J\033[;H", end='')
limpa()#------------------------------------------------------------
""" Arraias - TO <=> 2023 <=> UFT - Lincenciatura em Computação
    Disc <=> Programação de Computadores
    @Autor => Wenes Aquino -> 2º Períldo
"""    #------------------------------------------------------------

# FUNÇÃO 18/08/2023

def sanduiche(nome):
    print(f'Fazer sanduiche para {nome}')
    
def batata(tamanho):
    print(f'Batata {tamanho}')
    
def refrigerante(tipo, tamanho):
    print(f'{tipo} {tamanho}')

def fazer_combo(nome, tamanhoBat, tipo, tamanhoRefr):
    sanduiche(nome)
    batata(tamanhoBat)
    refrigerante(tipo, tamanhoRefr)


fazer_combo('Wenes', 'Grande', 'Coca', 'Pequeno\n')
fazer_combo('Aquino', 'Medio', 'Peps', 'Grande\n')
fazer_combo('Gomes', 'Pequeno', 'Fanta', 'Pequeno')