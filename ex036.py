#aprovar empréstimo
valor_casa = float(input('Informe o valor do imóvel: '))
salario_comprador = float(input('Informe seu salário: '))
anos_pagamento = int(input('Informe em quantos anos será realiado o pagamento: '))

parcela = valor_casa / (anos_pagamento * 12)
print('A parcela fica no valor de R$ {:.2f} que devem ser pagos em {} anos.'.format(parcela, anos_pagamento))

if parcela < (0.3 * salario_comprador):
    print('Você pode realizar o financiamento.')
else:
    print('Você não pode realizar o financiamento.')