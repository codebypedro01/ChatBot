def conversor_temperatura():
    import time
    print('[Conversor de Temperatura]: Vamos verificar a temperatura!')
    temperatura = float(input('Digite a temperatura: '))
    opcao = int(input('Opções de Conversão disponiveis:' \
    '\n1. Celsius para Fahrenheit' \
    '\n2. Celsius para Kelvin' \
    '\n3. Fahrenheit para Celsius' \
    '\n4. Fahrenheit para Kelvin' \
    '\n5. Kelvin para Celsius' \
    '\n6. Kelvin para Fahrenheit' \
    '\nSelecione a conversão desejada [1-6]: '))

    time.sleep(1)
    print('Convertendo a temperatura...')
    time.sleep(1)

    if opcao == 1:
        calc_temp = ((temperatura * 9) / 5) + 32
        print(f'[Conversor de Temperatura]: {temperatura}°C -> {calc_temp}°F.')
    elif opcao == 2:
        calc_temp = temperatura + 273.15
        print(f'[Conversor de Temperatura]: {temperatura}°C -> {calc_temp}°K.')
    elif opcao == 3:
        calc_temp = (temperatura - 32) * 5/9
        print(f'[Conversor de Temperatura]: {temperatura}°F -> {calc_temp}°C.')
    elif opcao == 4:
        calc_temp = (temperatura - 32) * 5/9 + 273.15
        print(f'[Conversor de Temperatura]: {temperatura}°F -> {calc_temp}°K.')
    elif opcao == 5:
        calc_temp = temperatura - 273.15
        print(f'[Conversor de Temperatura]: {temperatura}°K -> {calc_temp}°C.')
    elif opcao == 6:
        calc_temp = (temperatura - 273.15) * 9/5 + 32
        print(f'[Conversor de Temperatura]: {temperatura}°K -> {calc_temp}°F.') 
    else:
        print('ERRO: Valor Inválido!') 

conversor_temperatura()