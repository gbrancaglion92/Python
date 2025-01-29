#tabuada do número informado pelo usuário

n = int(input('Informe um número: '))
s = 0
for c in range (0, 10):
    s += 1
    print('{} x {} = '.format(n,s), n*s)
