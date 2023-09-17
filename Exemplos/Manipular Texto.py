limpa = lambda: print("\033[2J\033[;H", end='') #Função limpa console
limpa() #Limpa console

"""
Arraias - TO - 2023
UFT - Lincenciatura em Computação
Disc: Programação de Computadores
@Autor: Wenes Aquino - 2º Períldo
"""

texto = "wenes gomes aquino"

uft = """Universidade
Federal
Tocantins
""" #Texto com linhas quebrada

ufta = "Universidade \nFederal \nTocantins" #Texto com linhas quebrada

aspas = "Mostra (aspas) entre texto \"texto entre aspas\"." #Aspas entre texto

print("Caixa Alta = ", texto.upper())       #Caixa Alta
print("Descricao = ", texto.lower())       #Caixa Baixa
print("Descricao = ", texto.capitalize())  #Primeira Letra Maiúscula
print("Descricao = ", texto.isupper())     #Verifica se o texto é Maiúsculas
print("Descricao = ", texto.islower())     #Verifica se o texto é Minúsculas
print("Descricao = ", texto.strip())       #Remove Esapços no incio ou no final do texto
print("Descricao = ", texto.replace("e", "E"))    #Substitui texto
print("Descricao = ", texto.replace("e", "E", 1)) #Substitui o primeiro texto encontrado
print("Descricao = ", len(texto))                 #Numero de caracteres no texto
print("Descricao = ", (texto[12]))                #Mostra letra do índice especificado
print("Descricao = ", (texto[0:5]))               #Mostra intervalo de letra do índice especificado
print("Descricao = ", (texto[-1]))             #Mostra intervalo de letra do índice especificado invertido
print("Descricao = ", texto.index("a"))           #Mostra o índice da texto especificado

x = "wenes" in texto #Verifica se exite (x) na variável (texto)
print("Descricao = ", x)             #Mostra resultado da verificação

print("Descricao = ", uft) #Mostra texto linha quebrada
print("Descricao = ", ufta) #Mostra texto linha quebrada

print("Descricao = ", aspas) #Mostra Aspas entre texto































