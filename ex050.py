# input de 6 numeros e soma APENAS DOS PARES

s = 0
cont = 0
cont_par = 0
for c in range (0, 6):
    n = int(input('Informe um valor: '))
    cont += 1
    if n %  2 == 0:
        s += n
        cont_par += 1
print('Você informou {} números, desses {} foram pares. A soma deles é {}'.format(cont, cont_par, s))
