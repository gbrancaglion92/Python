while True:
    n = int(input('Ver a tabuada de: '))
    print('-'*30)
    if n < 0:
        break
    for i in range (1, 11):
        print(f'{n} x {i} = {n*i}')
    print('-' * 30)

print('Programa de tabuada encerrado. VOLTE SEMPRE!')

