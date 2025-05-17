def Calculadora():
    print('''[CALCULADORA]: Vamos começar!
[Calculadora]: Como posso te ajudar hoje?
1 - Calculo simples entre dois valores
2 - Mostrar tabuada de um número''')
    opcao_escolhida = int(input('R: '))
    if opcao_escolhida == 1:
        try:
            
            print('[Calculadora]: Iniciando calculo simples entre dois valores...\n')
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
            print('[ERRO]: Entrada Inválida. Digite apenas números inteiros.')
    elif opcao_escolhida == 2:
        try:
            
            print('[Calculadora]: Iniciando Tabuada\n')
            numero = int(input("Digite um número para ver a tabuada: "))
            print('--' * 20)
            nome_titulo = f'Tabuada do {numero}'
            print(f'{nome_titulo:^}')
            print('--' * 20)
            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")
            print('--' * 20)
        except:
            print('[ERRO]: Entrada Inválida. Digite apenas números inteiros.')