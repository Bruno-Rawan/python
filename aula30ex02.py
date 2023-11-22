try:
    horas = input('Digite as horas(hrs): ')

    horas_e_minutos = horas.split(':')
    horas = float(horas_e_minutos[0])
    minutos = float(horas_e_minutos[1])

    if horas >= 00.00 and horas < 12.00:
        print('Bom Dia!')

    elif horas >= 12.00 and horas < 18.00:
        print('Boa Tarde!')

    elif horas >= 18.00 and horas <= 23.59:
        print('Boa Noite!')

except:
    print('Valor invalido') 