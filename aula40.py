while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-*/): ')

    numeros_validos = None
    num1 = 0
    num2 = 0
    try:
        numeros_validos = True

    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')

    if len(operador) > 1:
        print('Digite apenas um operador.')

    print('Realizando sua conta, confira o resultado abaixo.')
    if operador == '+':
        print(num1 + num2 )

    elif operador == '-':
        print(num1 - num2 )

    elif operador == '/':
        print(num1 / num2 )
        
    elif operador == '*':
        print(num1 * num2 )

    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    

    if sair is True:
        break