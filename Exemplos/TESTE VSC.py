limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

def main():
    resposta = input('Deseja ativar o modo noturno? (sim/não): ')

    if resposta.lower() == 'sim':
        print("Modo noturno ativado!")
    elif resposta.lower() == "não":
        print("Modo noturno desativado!")
    else:
        print("Resposta inválida. Por favor, responda 'sim' ou 'não'.")

if __name__ == "__main__":
    main()