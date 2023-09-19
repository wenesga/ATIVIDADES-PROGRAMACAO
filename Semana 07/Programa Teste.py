limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------
import sys
import os

nome_arquivo = sys.argv[0]                 # Obtém o nome do arquivo Python que está sendo executado.
nome_puro = os.path.basename(nome_arquivo) # Obtém o nome do arquivo sem o caminho.
print(nome_puro)                           # Imprime o nome do arquivo.
