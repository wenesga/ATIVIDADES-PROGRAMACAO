limpa = lambda: print("\033[2J\033[;H", end='')
limpa()

""" #----------------------------------------------------------
    Arraias - TO => 2023 => UFT - Lincenciatura em Computação
    Disciplina => Programação de Computadores
    @Autor => Wenes Aquino => 2º Períldo
"""#-----------------------------------------------------------

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo  numero: "))

soma = num1 + num2
subt = num1 - num2
prod = num1 * num2      
pote = pow(num1, num2)

if num2 == 0:
    divs = "Absurdo!"
    rest = "Absurdo!"
else:
    divs = num1 / num2
    rest = num1 % num2 
    
print(f"""
Resultados: {num1} + {num2} = {soma}
            {num1} - {num2} = {subt}
            {num1} * {num2} = {prod}
            {num1} / {num2} = {divs}
   resto de {num1} % {num2} = {rest}
  potência de {num1}^{num2} = {pote}
""")