limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

produtos = []

while True:
        
    nome = input("\nNome ou N (Sair): ")
    
    if nome.lower() == "n":
        break
    
    preco = input("Preço: ")
    quantidade = input("Quantidade: ")
    
    produto = (nome, preco, quantidade)
    produtos.append(produto)
    
print("")

for produto in produtos:
    print(f"Produtos: ({', '.join(produto)})")

    