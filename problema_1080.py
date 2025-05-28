lista = []
for c in range(0,100):
    num = int(input())
    lista.append(num)
for p,v in enumerate(lista):
    if v == max(lista):
        print(f'{v}\n{p + 1}')
