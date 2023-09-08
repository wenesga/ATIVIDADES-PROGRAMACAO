limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

'''9. Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um
crime. As perguntas são:
    
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?" 

O programa deve no ﬁnal emitir uma classiﬁcação
sobre a participação da pessoa no crime. Se a pessoa responder positivamente a
2 questões ela deve ser classiﬁcada como "Suspeita", entre 3 e 4 como
"Cúmplice" e 5 como "Assassino". Caso contrário, ele será classiﬁcado como
"Inocente".'''

respostas = []
    
respostas.append(input("Telefonou para a vítima?   => (S ou N): ").upper())
respostas.append(input("Esteve no local do crime?  => (S ou N): ").upper())
respostas.append(input("Mora perto da vítima?      => (S ou N): ").upper())
respostas.append(input("Devia para a vítima?       => (S ou N): ").upper())
respostas.append(input("Já trabalhou com a vítima? => (S ou N): ").upper())

print('\n')

if respostas.count('S') == 2:
    print("Você é Suspeito. 🕵️‍♂️")

elif respostas.count('S') == 3 or respostas.count('S') == 4:
    print("Você é Cúmplice. 👥")

elif respostas.count('S') == 5:
    print("Você é o Assassino! 🔪💀")

else:
    print("Você é Inocente. 😇")
        
print(f"\nRespostas = {respostas}")
print(f"\nRespostas prositiva = {respostas.count('S')}")


















