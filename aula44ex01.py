nome = input('Nome: ')

while nome == '' or nome == ' ':
    print('campo obrigatório')
    nome = input('Nome: ')
if 's' in nome or 'S' in nome:       
    print('Saindo...')
else:
    print(nome)
