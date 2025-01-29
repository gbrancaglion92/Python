#input um número e informe se é primo - divisível por 1 e por ele mesmo

n = int(input('Informe um número: '))
tot = 0
for i in range (1, n + 1):
    if n % i == 0:
        print('\033[034m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(i, end=' ')

if tot == 2:
    print('\033[mO número {} foi divisível {} vezes e é primo'.format(n, tot))
else:
    print('\033[mO numero {} foi divisível {} vezes e não é primo'.format(n, tot))