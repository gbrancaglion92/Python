s = total = 0
while True:
    n = int(input('Informe um número: '))
    if n == 999:
        break
    total += 1
    s += n
print(f'A soma dos {total} valores foi de {s}.')