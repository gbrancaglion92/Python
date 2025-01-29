#nascimento de 7 pessoas e conferir quais ainda não são maiores e quais são

from datetime import date
ano_atual = date.today().year
tot_maior = 0
tot_menor = 0
for c in range (1, 8):
    ano_nasci = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    idade = ano_atual - ano_nasci
    if idade >= 21:
        tot_maior += 1
    else:
        tot_menor += 1

print('{} pessoas são maior de idade.'.format(tot_maior))
print('{} são menor de idade.'.format(tot_menor))