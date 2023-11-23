"""
Ex
Gera uma string personalizada usando o while
"""

nome = 'Bruno Rawan'
indice = 0
novo_nome = ''

while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)
