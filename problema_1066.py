pares = positivos = negativos = impares = 0

while True:
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num == abs(num):
        positivos += 1
    else:
        negativos += 1
print(f'{pares} valor (es) par(es)\n{impares} valor (es) impar(es)\n{positivos} valor (es) positivo(s)\n{negativos} valor (es) negativo(s).')
