#input 1º termo e progressão aritmética - mostre os 10 primeiros termos dessa progressão

t = int(input('Informe o termo: '))
r = int(input('Informe a razão: '))
decimo = t + (10-1) * r

for c in range (t, decimo + r   , r): #como mostrar só os 10 primeiros?
    print(c, end = ' → ')
print('Acabou')