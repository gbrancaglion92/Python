medidor = 15
while True:
    v = int(input('Valor em ml: '))
    if v == 0:
        print('Conversões finalizadas. Bora cozinhar!')
        break
    ing = str(input('Ingrediente: '))
    conversao = v / medidor
    print(f'\033[33mSerão necessárias {conversao:.1f} colheres de {ing}\033[m')
