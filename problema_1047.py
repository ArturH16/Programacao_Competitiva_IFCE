while True:
    hora_inicial = input('Digite a hora inicial: ')
    if hora_inicial.isdigit() == False:
        hora_inicial = 0
    else:
        hora_inicial = int(hora_inicial)
    if hora_inicial > 25:
        print('Por favor, digite um valor entre 1 e 24')
    else:
        break
while True:
    minuto_inicial = input('Digite o minuto inicial: ')
    if minuto_inicial.isdigit() == False:
        minuto_inicial = 1
    else:
        minuto_inicial = int(minuto_inicial)
    if minuto_inicial < 1:
        print('Por favor, digite um valor igual ou maior a 1')
    else:
        break
while True:
    hora_final = input('Digite a hora final: ')
    if hora_final.isdigit() == False:
        hora_final = 0
    else:
        hora_final = int(hora_final)
    if hora_final > 25:
        print('Por favor, digite um valor entre 1 e 24')
    else:
        break
while True:
    minuto_final = input('Digite o minuto final: ')
    if minuto_final.isdigit() == False:
        minuto_final = 1
    else:
        minuto_final = int(minuto_final)
    if minuto_final > 25:
        print('Por favor, digite um valor igual ou maior a 1')
    else:
        break
duracao_horas = abs(hora_inicial - hora_final)
duracao_minutos = abs(minuto_inicial - minuto_final)
print(f'O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S).')
