#input peso de 5 pessoas e mostre o maior e menor

pesos = []

for i in range (1, 6):
    peso = float(input('Informe seu peso da pessoa {}ª em kg: '.format(i)))
    pesos.append(peso)

maior_peso = max(pesos)
menor_peso = min(pesos)
print('Peso maior foi {}kg'.format(maior_peso))
print('Peso menor foi {}kg'.format(menor_peso))
