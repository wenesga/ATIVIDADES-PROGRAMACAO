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

print(texto.upper())       #Caixa Alta
print(texto.lower())       #Caixa Baixa
print(texto.capitalize())  #Primeira Letra Maiúscula
print(texto.isupper())     #Verifica se o texto é Maiúsculas
print(texto.islower())     #Verifica se o texto é Minúsculas
print(texto.strip())       #Remove Esapços no incio ou no final do texto
print(texto.replace("e", "E"))    #Substitui texto
print(texto.replace("e", "E", 1)) #Substitui o primeiro texto encontrado
print(len(texto))                 #Numero de caracteres no texto
print((texto[12]))                #Mostra letra do índice especificado
print((texto[0:5]))               #Mostra intervalo de letra do índice especificado
print((texto[-6:-1]))             #Mostra intervalo de letra do índice especificado invertido
print(texto.index("a"))           #Mostra o índice da texto especificado

x = "wenes" in texto #Verifica se exite (x) na variável (texto)
print(x)             #Mostra resultado da verificação

print(uft) #Mostra texto linha quebrada
print(ufta) #Mostra texto linha quebrada

print(aspas) #Mostra Aspas entre texto































