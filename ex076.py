listagem = ('Pão', 3.50, 'Fermento', 1.25, 'Maça', 5.99, 'Gelatina', 0.56, 'Cerveja', 2.39)
print('/'*30)
print('LISTAGEM DE PREÇOS'.center(30))
print('/'*30)

for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>3.2f}')
