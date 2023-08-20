limpa = lambda: print("\033[2J\033[;H", end='')
limpa()



nome = input("digite seu nome ")
mensagem = "Olá, "+ nome+ "! Bem vindo ao nosso Programa"
print(mensagem)