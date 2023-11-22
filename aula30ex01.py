try:
    n1 = int(input('Digite um número: '))
    # n2 = int(input('Digite o segundo número: '))
    # soma = n1 + n2
    if n1 % 2 == 0:
        print('Número par.')
    else:
        print('Número ímpar.')

except ValueError:
    print('\nSó é permitido números!\nPor favor, tente novamente.')