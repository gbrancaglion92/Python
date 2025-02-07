n = []
print(f'-'*25)
print(f'Organizador de lista')
print(f'-'*25)
for i in range(0, 5):
    num = int(input(f'Digite um valor: '))
    if num == 0:
        print(f'Programa encerrado')
        break
    n.append(num)
    


print(f'\033[33m {n}\033[m]')