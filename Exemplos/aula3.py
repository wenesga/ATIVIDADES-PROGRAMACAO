# -*- coding: utf-8 -*-

# nota1=float(input("Digite a nota do primeiro bimestre: "))
# nota2=float(input("Digite a nota do segundo bimestre: "))
# nota3=float(input("Digite a nota do terceiro bimestre: "))
# nota4=float(input("Digite a nota do quarto bimestre: "))

# media=(nota1+nota2+nota3+nota4)/4

# print("A média da nota é: ",media)

# if (media >= 7):
#   print("O aluno foi aprovado.")
# if (media<7) and (media >= 4):
#   print("O aluno vai ter que fazer exame final.")
# if (media < 4):
#   print("O aluno reprovou.")



nome_login_cadastrado="wenes"
senha_cadastrada="123"

nome_login_pedido=input("Digite o nome de login: ")
senha_pedida=input("Digite a senha:")

if nome_login_cadastrado==nome_login_pedido and senha_cadastrada==senha_pedida:
  print("Login realizado com sucesso!")
else:
  print("Login ou senha invalidos")


# nome_login_cadastrado="Eduardo Ribeiro"
# senha_cadastrada="123456"

# nome_login_pedido=input("Digite o nome de login: ")
# senha_pedida=input("Digite a senha:")

# if nome_login_cadastrado==nome_login_pedido:
#   if senha_cadastrada == senha_pedida:
#     print("Login realizado com sucesso!")
#   else:
#     print("Senha não confere.")
# else:
#     print("O nome de Login Não existe.")




# nome_login_cadastrado="Eduardo Ribeiro"
# senha_cadastrada="123456"

# nome_login_pedido=input("Digite o nome de login: ")

# if nome_login_cadastrado==nome_login_pedido:
#   senha_pedida=input("Digite a senha:")
#   if senha_cadastrada == senha_pedida:
#     print("Login realizado com sucesso!")
#   else:
#     print("Senha não confere.")
# else:
#     print("O nome de Login Não existe.")



# valor_total_compra=float(input("Digite o valor final da compra:"))

# if(valor_total_compra>=100):
#   desconto=valor_total_compra*0.1
#   valor_com_desconto=valor_total_compra-desconto

# elif(valor_total_compra>=50)and (valor_total_compra<100):
#   desconto=valor_total_compra*0.05
#   valor_com_desconto=valor_total_compra-desconto


# else:
#   valor_com_desconto=valor_total_compra
# print("O valor final com desconto será de: ", valor_com_desconto)



# valor_total_compra=float(input("Digite o valor final da compra:"))

# if(valor_total_compra>=100):
#   valor_com_desconto=valor_total_compra-(valor_total_compra*0.1)

# elif(valor_total_compra>=50)and (valor_total_compra<100):
#   valor_com_desconto=valor_total_compra-(valor_total_compra*0.05)


# else:
#   valor_com_desconto=valor_total_compra
# print("O valor final com desconto será de: ", valor_com_desconto)



# valor_do_emprestimo=float(input("Digite o valor do empréstimo:"))
# quantidade_de_parcelas=float(input("Digite a quantidade de Parcelas:"))
# renda_do_cliente=float(input("Digite a renda do cliente:"))
# valor_da_parcela=valor_do_emprestimo/quantidade_de_parcelas

# if (valor_do_emprestimo>=1000) and (valor_do_emprestimo<=50000) and (quantidade_de_parcelas>=6) and (quantidade_de_parcelas<=36) and (valor_da_parcela<=(renda_do_cliente*0.3)):
#   print("Emprestimo Aprovado!")
# else:
#   print("Emprestimo Negado!")



# valor_do_emprestimo=float(input("Digite o valor do empréstimo:"))
# quantidade_de_parcelas=float(input("Digite a quantidade de Parcelas:"))
# renda_do_cliente=float(input("Digite a renda do cliente:"))
# valor_da_parcela=valor_do_emprestimo/quantidade_de_parcelas


# if (valor_do_emprestimo<1000):
#   print("Emprestimo negado! Escolha um valor de empréstimo maior ou igual a 1000.")
# elif(valor_do_emprestimo>50000):
#   print("Emprestimo negado! Escolha um valor de empréstimo menor ou igual a 50000.")
# elif(quantidade_de_parcelas<6):
#   print("Emprestimo negado! Escolha uma quantidade de parcelas maior que 6.")
# elif(quantidade_de_parcelas>36):
#   print("Emprestimo negado! Escolha uma quantidade de parcelas menor que 36.")
# elif(valor_da_parcela>(renda_do_cliente*0.3)):
#   print("Emprestimo negado! O valor da parcela deve ser maior que 30% da renda do cliente!")
# else:
#   print("Emprestimo Aprovado!")



# valor_do_emprestimo=float(input("Digite o valor do empréstimo:"))

# if (valor_do_emprestimo<1000):
#   print("Emprestimo negado! Escolha um valor de empréstimo maior ou igual a 1000.")
# elif(valor_do_emprestimo>50000):
#   print("Emprestimo negado! Escolha um valor de empréstimo menor ou igual a 50000.")
# else:
#   quantidade_de_parcelas=float(input("Digite a quantidade de Parcelas:"))
#   if(quantidade_de_parcelas<6):
#     print("Emprestimo negado! Escolha uma quantidade de parcelas maior que 6.")
#   elif(quantidade_de_parcelas>36):
#     print("Emprestimo negado! Escolha uma quantidade de parcelas menor que 36.")
#   else:
#     renda_do_cliente=float(input("Digite a renda do cliente:"))
#     valor_da_parcela=valor_do_emprestimo/quantidade_de_parcelas
#     if(valor_da_parcela>(renda_do_cliente*0.3)):
#       print("Emprestimo negado! O valor da parcela deve ser maior que 30% da renda do cliente!")
#     else:
#        print("Emprestimo Aprovado!")