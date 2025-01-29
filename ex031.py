dist=float(input('Informe a distância que será a viagem: '))

if dist<=200:
    passagem=dist*0.5
    print('O valor da passagem será de R${:.2f}'.format(passagem))
else:
    passagem=dist*0.45
    print('O valor da passagem será de R${:.2f}'.format(passagem))
