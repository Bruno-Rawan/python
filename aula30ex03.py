nome = input('Digite seu nome: ')
nome_espaco = len(nome.replace(' ', '',))


if nome_espaco <= 4:
    print('Nome curto!')

elif nome_espaco >= 5 and nome_espaco <= 6:
    print('Nome normal!')

else:
    print('Nome grande!')

print(f'Seu nome tem {nome_espaco} letras.')