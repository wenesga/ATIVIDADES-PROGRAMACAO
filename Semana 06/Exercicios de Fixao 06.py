limpa = lambda: print("\033[2J\033[;H", end='')
limpa()
""" Arraias - TO - 2023 - UFT - Lincenciatura em Computação
    Disciplina: Programação de Computadores
    @Autor: Wenes Aquino - 2º Períldo                   """
#-----------------------------------------------------------

'''6. Escreva um programa que gerencie uma lista de tarefas a fazer. Utilize uma lista de
dicionários, onde cada dicionário representa uma tarefa com descrição, data de prazo e
status.'
'''

import datetime

# Crie uma lista vazia de tarefas
tarefas = []

# Adicione uma tarefa à lista
tarefas.append({
    "description": "Comprar pão",
    "due_date": datetime.date.today() + datetime.timedelta(days=1),
    "status": "pendente"
})

# Adicione outra tarefa à lista
tarefas.append({
    "description": "Lavar a louça",
    "due_date": datetime.date.today() + datetime.timedelta(days=2),
    "status": "pendente"
})

# Exiba a lista de tarefas
for tarefa in tarefas:
    print("Descrição:", tarefa["description"])
    print("Data de vencimento:", tarefa["due_date"])
    print("Status:", tarefa["status"])

# Atualize o status de uma tarefa
tarefa = tarefas[0]
tarefa["status"] = "concluída"

# Exiba a lista de tarefas atualizada
for tarefa in tarefas:
    print("Descrição:", tarefa["description"])
    print("Data de vencimento:", tarefa["due_date"])
    print("Status:", tarefa["status"])
