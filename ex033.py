n1 = int(input('Informe o N1: '))
n2 = int(input('Informe o N2: '))
n3 = int(input('Informe o N3: '))
menor = n1

if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor valor é {}'.format(menor))

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior número é {} '.format(maior))
