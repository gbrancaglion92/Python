while True:
    valor = int(input('Informe o valor a ser sacado (ou 0 para sair): R$'))
    if valor == 0:
        print("Encerrando...")
        break
    if valor < 0:
        print("O valor deve ser positivo.")
        continue

    cedulas_50 = valor // 50
    valor %= 50  # Resto do valor após usar notas de R$50
    cedulas_20 = valor // 20
    valor %= 20  # Resto do valor após usar notas de R$20
    cedulas_10 = valor // 10
    valor %= 10  # Resto do valor após usar notas de R$10
    cedulas_1 = valor  # O restante será em notas de R$1

    if cedulas_50 > 0:
        print(f'{cedulas_50} notas de R$50')
    if cedulas_20 > 0:
        print(f'{cedulas_20} notas de R$20')
    if cedulas_10 > 0:
        print(f'{cedulas_10} notas de R$10')
    if cedulas_1 > 0:
        print(f'{cedulas_1} notas de R$1')
    break
print('Obrigada por utilizar nossos serviços.')
