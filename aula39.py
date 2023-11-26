"""TABUADA"""


try:
    n = int(input("Digite o número da tabuada: "))
    operador = input("Digite o operador: ")
    i = 1

  
    while i <= 10:
        if operador == '*':
            print(f"{n} x {i} = {n * i}")
            i += 1

        elif operador == '/':
            print(f"{n} / {i} = {n / i:.2f}")
            i += 1

        elif operador == '+':
            print(f"{n} + {i} = {n + i}")
            i += 1

        elif operador == '-':
            print(f"{n} - {i} = {n - i}")
            i += 1
except:
    print("Você precisa digitar um número!")

