#1 soma 2 multiplicar 3 maior 4 novos números 5 sair do programa

n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
opcoes = 0
while opcoes != 5:
    print('/' * 30)
    print('''     MENU:
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MOSTRAR O MAIOR
    [ 4 ] INSERIR NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''''')
    print('/' * 30)
    opcoes = int(input('\033[32m>>>>>>> Selecione uma das opções: \033[m'))
    if opcoes == 1:
        print('A soma de {} e {} é {}'.format(n1, n2, n1+n2))
    elif opcoes == 2:
        print('A multiplicação de {} e {} é {}'.format(n1, n2, n1*n2))
    elif opcoes == 3:
        if n1 > n2:
            print('O maior entre {} e {} é {}'.format(n1, n2, n1))
        else:
            print('O maior entre {} e {} é {}'.format(n1, n2, n2))
    elif opcoes == 4:
        n1 = int(input('Informe um novo valor para o primeiro número: '))
        n2 = int(input('Informe um novo valor para o segundo número: '))
    elif opcoes == 5:
        print('Fim do programa. Tchau!')
    else:
        print('Opção inválida. Selecione um valor entre 1 e 5.')

