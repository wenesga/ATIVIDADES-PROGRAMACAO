limpa = lambda: print("\033[2J\033[;H", end='')
limpa()#------------------------------------------------------------
""" Arraias - TO <=> 2023 <=> UFT - Lincenciatura em Computação
    Disc <=> Programação de Computadores
    @Autor => Wenes Aquino -> 2º Períldo
"""    #------------------------------------------------------------

#LISTA

# contagem     1       2        3         4          5    
alimento = ["arroz","carne","feijao", "farinha", "leite"]
# indices      0       1        2         3          4
# invertido   -5      -4       -3        -2         -1

print("Quarto item =", alimento[3])
print("Terceiro item invertido =", alimento[-3])
print("Terceiro item pro ultimo =", alimento[2:])
print("Do terceiro até o quinto=", alimento[2:4],"\n")

print(alimento,"\n")

alimento[3] = "arroz" #Difine valor de um item
print(alimento,"\n")

alimento.extend(["abobora", "batata"]) #Adiciona e esse lista na outra
print(alimento,"\n")

alimento.append("banana") #Adiciona apenas um item
print(alimento,"\n")

alimento.insert(3, "pêra") #Adiciona em um posição especificada
print(alimento,"\n")

alimento.pop() #Removi o último item
print(alimento,"\n")

alimento.pop(4) #Removi o item especificado pelo índice
print(alimento,"\n")

alimento.remove("arroz") #Removi o último especificado
print(alimento,"\n")

alimento.clear() #Limpa a lista
print(alimento,"\n")


print(alimento.index("carne"),"\n") #Retorna indice do item especificado

print(alimento.count("arroz"),"\n") #Conta itens especificado

print(alimento)
alimento.sort() #Ordenar strings
print(alimento)

idades = [20,56,54,32]
print(idades)
idades.sort() #Ordenar numeros
print(idades)

idades.reverse()
print(idades) #Ordem reversa

#COPIA POR REFERENCIA
alimento2 = alimento #Ocupa mesmo espaço na memoria
print(alimento2)
alimento.remove("arroz") #Remove arroz de alimento
print(alimento2,"\n") #Tambem foi removiddo de alimento2 

#COPIA
alimento2 = alimento.copy() #Faz copia de uma lista
alimento.remove("arroz") 
print(alimento)
print(alimento2) 

#TUPLES => Faz mesmo coisa que "Lista" exceto alterar os valores
coordenadas = (45, 62)
print(coordenadas[1])
print(coordenadas.count(45))









