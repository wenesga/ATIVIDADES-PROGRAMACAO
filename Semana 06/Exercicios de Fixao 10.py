limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

'''10. Desenvolva um programa que simule uma lista de compras em um supermercado. Utilize
uma lista de dicionários, onde cada dicionário representa um item com informações como
nome, quantidade e preço.'''

# Inicialize a lista de compras como uma lista de dicionários
lista_de_compras = []

# Adicione itens à lista de compras
lista_de_compras.append({"Nome": "Maçã", "Quantidade": 5, "Preço": 1.99})
lista_de_compras.append({"Nome": "Leite", "Quantidade": 2, "Preço": 2.50})
lista_de_compras.append({"Nome": "Pão", "Quantidade": 3, "Preço": 2.00})
lista_de_compras.append({"Nome": "Arroz", "Quantidade": 1, "Preço": 4.99})

# Listar todos os itens na lista de compras
print("Lista de Compras:")
for item in lista_de_compras:
    nome = item["Nome"]
    quantidade = item["Quantidade"]
    preco = item["Preço"]
    subtotal = quantidade * preco
    print(f"Nome: {nome}, Quantidade: {quantidade}, Preço: R${preco:.2f}, Subtotal: R${subtotal:.2f}")

# Calcular o valor total da lista de compras
valor_total = sum(item["Quantidade"] * item["Preço"] for item in lista_de_compras)
print(f"Valor Total da Compra: R${valor_total:.2f}")
