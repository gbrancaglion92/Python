vel=float(input('Informe a velocidade do automóvel: '))

if vel > 80:
    multa = (vel-80)*7
    print('Você foi multado no valor de R$',multa)
