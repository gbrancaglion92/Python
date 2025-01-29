r1 = int(input('Informe um valor: '))
r2 = int(input('Informe um valor: '))
r3 = int(input('Informe um valor: '))

if (r1+r2) > r3 and (r2+r3) > r1 and (r1+r3) > r2:
    print('É possível formar um triângulo')
    if r1 == r2 == r3:
        print('Triângulo equilátero')
    if r1 == r2 and r2 != r3 or r2 == r3 and r3 != r1 or r1 == r3 and r3 != r2:
        print('Triângulo isósceles')
    if r1 != r2 and r2 != r3 and r1 != r3:
        print('Triângulo escaleno')
else:
    print('Não é possível formar um triângulo')
