n = []
while True:
    n.append(int(input('Digite um valor: ')))
    print('Valor adicionado com sucesso')

    while True:
        continuacao = str(input(f'Deseja continuar? [S/N]')).upper().strip()
        if continuacao in ['S', 'N']:
            break
        print(f'Opção incorreta. Tente novamente.')
    if continuacao == 'N':
        print(f'Os valores inseridos foram: \033[33m{n}\033[m')
        print(f'Programa encerrado')
        break
    