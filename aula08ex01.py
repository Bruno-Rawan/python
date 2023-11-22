nome = str(input('Digite seu nome: '))
sobrenome = str(input('Digite seu sobrenome: '))
# idade = int(input('Digite sua idade: '))
anonasc = int(input('Ano de nascimento: '))
ano_atual = int(input('Em que ano estamos? '))
altura = float(input('Altura (mts): '))

calc_ano = ano_atual - anonasc

if calc_ano >= 18:
    print(f'Prazer {nome} {sobrenome}!')
    print(f'Você têm {altura}mts de altura, e sua idade é {calc_ano} anos.')

else:
    print('Você não é maior de idade fim de programa!!!!')