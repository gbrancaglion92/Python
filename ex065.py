tot = 1
maior = menor = s = n = 0

n = int(input('Informe um número: '))
continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
while continuar == 'S':
    n = int(input('Informe um número: '))
    s += n
    tot += 1
    if tot == 2:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    continuar = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
if continuar == 'N':
    print('Programa encerrado.')
media = s / tot
print('Foram digitados {} números. A média dos números digitados é {:.2f}. O maior número é {} e o menor é {}'.format(tot, media, maior, menor))