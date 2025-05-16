def Calculadora():
    print('[CALCULADORA]: Vamos começar!')

    try:

        numero1 = int(input('Digite o primeiro número: '))
        operador = str(input('Digite o operador (+, -, *, /): ')).strip()
        numero2 = int(input('Digite o segundo número: '))

        if operador == '+':
            resultado = numero1 + numero2

        elif operador == '-':
            resultado = numero1 - numero2

        elif operador == '*':
            resultado = numero1 * numero2

        elif operador == '/':
            if numero2 == 0:
                print('[ERRO]: Divisão por zero!')
            resultado = numero1 / numero2        
        
        else:
            print('[ERRO]: Operador inválido!')

        print(f'Resultado: {numero1} {operador} {numero2} = {resultado}')
    
    except:
        print('[ERRO]: Entrada Inválida. Digite apenas números.')
    