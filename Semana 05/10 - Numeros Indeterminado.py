limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

'''10 - Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;'''

notas = []

while True:
    nota = float(input("Me dê uma nota (-1 para dar um tchau): "))

    if nota == -1:
        break
    notas.append(nota)

quantidade = len(notas)

print(f"Você me deu {quantidade} notas. Uau!")
print("Notas que você me deu:", end=' ')

for nota in notas:
    print(nota, end=" ")

print("\nNotas em ordem reversa:", end=' ')
for nota in reversed(notas):
    print(nota, end=' ')

soma = sum(notas)
print(f"\nSoma das notas: {soma}.")

media = soma / quantidade
print(f"Média das notas é: {media}.")

acima_da_media = len([nota for nota in notas if nota > media])

print(f"Temos {acima_da_media} notas acima da média. Impressionante!")

abaixo_de_sete = len([nota for nota in notas if nota < 7])
print(f"Você tem {abaixo_de_sete} notas abaixo de 7. Estamos de olho! 😉")

print("Ok, acabou! Até a próxima!")















