limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

""" #----------------------------------------------------------
    Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo
"""#-----------------------------------------------------------

valor_origem = float(input("Digite o valor a ser convertido: "))
moeda_origem = input("Digite a moeda de origem (ex: brl, usd, btc): ")
moeda_destino = input("Digite a moeda de destino (ex: brl, usd, btc): ")

taxa_dolar = 4.85
taxa_euro = 5.30
taxa_bitcoin = 128000

def converte(valor, taxa):
    return valor / taxa
    
if moeda_origem == 'brl' and moeda_destino == 'usd':
    resultado = converte(valor_origem, taxa_dolar)

elif moeda_origem == 'brl' and moeda_destino == 'btc':
    resultado = converte(valor_origem, taxa_bitcoin)

elif moeda_origem == 'btc' and moeda_destino == 'brl':
    resultado_btc = converte(valor_origem, taxa_bitcoin)
    resultado = converte(valor_origem, resultado_btc)
    print(resultado_btc)
    print(resultado)

elif moeda_origem == 'btc' and moeda_destino == 'usd':
    resultado = converte(valor_origem, taxa_dolar)

elif moeda_origem == 'usd' and moeda_destino == 'brl':
    resultado = converte(valor_origem, valor_origem)

elif moeda_origem == 'usd' and moeda_destino == 'btc':
    converte(valor_origem, taxa_bitcoin)
    
print(f"Valor convertido = {resultado}")
