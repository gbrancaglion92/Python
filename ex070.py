s_caro = s_total = laco = 0
nome_produto = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Valor do produto R$ '))
    cont = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('Deseja continuar? [S/N]')).upper().strip()[0]

    laco += 1
    s_total += preco
    if laco == 1 or preco < barato:
        barato = preco
        nome_produto = produto
    if preco > 1000:
        s_caro += 1

    if cont == 'N':
        break

print(f'O total gasto na compra foi de R$ {s_total:.2f}.')
print(f'{s_caro} produtos custaram mais de R$ 1.000')
print(f'O produto mais barato foi o {nome_produto} no valor de {barato:.2f}')
