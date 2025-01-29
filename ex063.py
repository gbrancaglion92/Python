#input n - output n primeiros números da sequencia de fibonacci

n = int(input('Informe um número: '))
c = 3
n1 = 0
n2 = 1
print('{} -> {} -> '.format(n1, n2), end = ' ')
while c <= n:
    c += 1
    n3 = n1 + n2
    print('{} -> '.format(n3), end=' ')
    n1 = n2
    n2 = n3
print('FIM')