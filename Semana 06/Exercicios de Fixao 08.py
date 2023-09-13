limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

'''8. Implemente um programa que controle o estoque de uma loja. Utilize uma lista de
dicionários, onde cada dicionário representa um produto com informações como nome,
quantidade em estoque e preço.'''

# Inicialize a lista de produtos como uma lista vazia
estoque = []

# Adicione produtos ao estoque
estoque.append({"Nome": "Produto A", "Quantidade": 10, "Preço": 5.99})
estoque.append({"Nome": "Produto B", "Quantidade": 15, "Preço": 9.99})

# Listar produtos no estoque
print("Lista de Produtos:")
for produto in estoque:
    print(f"Nome: {produto['Nome']}, Quantidade: {produto['Quantidade']}, Preço: R${produto['Preço']}")

# Atualizar a quantidade de um produto no estoque
nome_produto = input("Digite o nome do produto a ser atualizado: ")
quantidade_atualizada = int(input("Digite a quantidade atualizada: "))

for produto in estoque:
    if produto['Nome'] == nome_produto:
        produto['Quantidade'] = quantidade_atualizada
        print(f"A quantidade de {nome_produto} foi atualizada para {quantidade_atualizada}.")
        break
else:
    print(f"{nome_produto} não encontrado no estoque.")

# Calcular o valor total do estoque
valor_total = 0
for produto in estoque:
    valor_total += produto['Quantidade'] * produto['Preço']

print(f"O valor total do estoque é R${valor_total:.2f}")
