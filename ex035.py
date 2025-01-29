#input de 3 valores
#output se os valores formam ou não um triângulo

r1 = int(input('Informe um valor: '))
r2 = int(input('Informe um valor: '))
r3 = int(input('Informe um valor: '))

if (r1+r2) > r3 and (r2+r3)>r1 and (r1+r3)>r2:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')
