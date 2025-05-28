lista = []
hobbits = humanos = elfos = anoes = magos = 0
num = int(input())
for c in range(0,num):
    ser = input()
    lista.append(ser)
for p,v in enumerate(lista):
    if v[-1] == 'X':
        hobbits += 1
    if v[-1] == 'H':
        humanos += 1
    if v[-1] == 'E':
        elfos += 1
    if v[-1] == 'A':
        anoes += 1
    if v[-1] == 'M':
        magos += 1
print(f'{hobbits} Hobbit(s)\n{humanos} Humano(s)\n{elfos} Elfo(s)\n{anoes} Anao(oes)\n{magos} Mago(s)')
    
