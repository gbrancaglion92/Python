t = int(input('Informe o termo: '))
r = int(input('Informe a razão: '))
total = int(input('Quantos termos você quer ver? '))
c = 0
s = 0
while c < total:
    print(t, end = ' → ')
    c += 1
    t += r
    s += 1
print('PAUSA')
op = input('\nMostrar mais [S/N]').upper()
while op == 'S':
    c = 0
    mm = int(input('Quantos termos mais quer ver? '))
    while c < mm:
        print(t, end=' → ')
        c += 1
        t += r
        s += 1
    print('PAUSA')
    op = input('\nMostrar mais [S/N]').upper()
if op == 'N':
    print('Programa encerrado. Foram exibidos {} termos.'.format(s))
while op != 'S' and op != 'N':
    print('Opção inválida, tente novamente.')
    c = 0
    mm = int(input('Quantos termos mais quer ver? '))
    while c < mm:
        print(t, end=' → ')
        c += 1
        t += r
        s += 1
    print('PAUSA')
    op = input('\nMostrar mais [S/N]').upper()