preco = float(input('Informe o valor do produto: '))
print('''Condições de pagamento:
[1]Dinheiro
[2]Cartão(2x)
[3]Cartão(3 ou mais)]''')
condicao = int(input('Informe a forma de pagamento: '))

if condicao == 1:
    print('O valor total será R$ ', preco-(preco*0.10))
elif condicao == 2:
    print('O valor total será de R$ ', preco-(preco*0.05))
elif condicao == 3:
    print('O valor total será de R$ ', preco+(preco*0.2))