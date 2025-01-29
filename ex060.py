#fatorial de um número

n = int(input('Informe um número: '))
f = 1 #fator nulo de multiplicação
c = 1
while c <= n:
    f *= c
    c += 1
print('O fatorial de {} é {}.'.format(n, f))


# Resolução com for:
n = int(input('numero: '))
f = 1
for i in range (1, n + 1):
    f *= i
print(f)