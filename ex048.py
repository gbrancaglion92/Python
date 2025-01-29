#soma de números impares múltiplos de 3 entre 1 e 500

s = 0
cont = 0

for c in range (0,501):
    if c % 2 != 0:
        if c % 3 == 0:
            cont += 1
            s += c
print(s)
print(cont)
