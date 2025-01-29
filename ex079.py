n = []
while True:
    valor = int(input('Informe um número: '))
    if valor == -1:
        print('Programa encerrado.')
        break
    if valor in n:
        print(f'O número {valor} já foi inserido, por favor entre outro número.')
    else:
        n.append(valor)
        print(f'O número {valor} foi adicionado a sua lista.')
print(f'A lista gerada foi: \033[33m{n}')

