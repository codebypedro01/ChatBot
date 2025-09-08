from calculadora import Calculadora
from data_e_hora import mostrar_data_e_hora
from conversor_temperatura import conversor_temperatura
from gerador_de_senhas import gerar_senha

nome_usuario = input('[CHAT]: Olá, qual seu nome? ').strip().capitalize()

if all(part.isalpha() for part in nome_usuario.split()):
    print(f'''\nOlá {nome_usuario}, como posso te ajudar hoje?

[ 1 ] Calculadora
[ 2 ] Data e Hora atual
[ 3 ] Conversor de Temperatura
[ 4 ] Gerar senha aleatória
[ 5 ] Frase Motivacional
[ 0 ] Sair
''')
    opcao_escolhida = int(input('Digite a opção desejada: '))
    match opcao_escolhida:
        case 1:
            # calculadora()
            Calculadora()
                
        case 2:
            # data_e_hora()
            mostrar_data_e_hora()
                
        case 3:
            # conversor_de_temperatura()
            conversor_temperatura()
        case 4:
            # gerador_de_senha()
            gerar_senha()
            tamanho = int(input('Digite o tamanho da senha: '))
            print(f'Senha gerada: {gerar_senha(tamanho)}')
        case 5:
            # frase_motivacional()
            print('Frase Motivacional')
        case 0:
            # sair()
            print('Sair')
        case _:
            # opcao_invalida()
            print('Opção Invalida')
        

else:
    print('[CHAT]: Digite um nome!')
        



