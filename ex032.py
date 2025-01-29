from datetime import date

ano=int(input('Informe um ano: '))
if ano == 0:
    ano = date.today().year

if ano%100==0 and ano%400==0:
    print('O ano {} é bisssexto'.format(ano))
elif ano%4==00:
    print('O ano {} é bisssexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))