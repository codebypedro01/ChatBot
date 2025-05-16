from datetime import datetime

def mostrar_data_e_hora():

    agora = datetime.now()
    data_formatada = agora.strftime('%d/%m/%Y')
    hora_formatada = agora.strftime('%H:%M:%S')

    print(f'[DATA E HORA]: Hoje é {data_formatada} e agora são {hora_formatada}')