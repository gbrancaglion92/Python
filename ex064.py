n = s = c = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        s += n
        c += 1
print('Fim do programa')
print('A soma dos números informados é {} e fora informados {} números.'.format(s, c))