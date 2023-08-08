def calculate():
    operation = input('''
Por favor, digite a operação matemática que você gostaria de completar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = int(input('Por favor insira o primeiro número: '))
    number_2 = int(input('Por favor, digite o segundo número: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2)) 
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não digitou um operador válido, execute o programa novamente.')
calculate()