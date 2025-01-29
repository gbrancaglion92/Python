salario = float(input('Informe o valor do salário R$ '))

if salario > 1250:
    aumento = (salario*0.1)+salario
    print('O aumento será de {} '.format(aumento))
else:
    aumento = (salario*0.15)+salario
    print('O aumento será de {} '.format(aumento))