from datetime import  date

ano_atual = date.today().year
ano_nasci = int(input('Informe seu ano de nascimento: '))
classificacao = ano_atual - ano_nasci

if classificacao <= 9:
    print('Sua idade é {} e você está na categoria Mirim'.format(classificacao))
elif 10 <= classificacao <= 14:
    print('Sua idade é {} e você está na categoria Infantil'.format(classificacao))
elif 15 <= classificacao <= 19:
    print('Sua idade é {} e você está na categoria Júnior'.format(classificacao))
elif classificacao == 20:
    print('Sua idade é {} e você está na categoria Sênior'.format(classificacao))
else:
    print('Sua idade é {} e você está na categoria Master'.format(classificacao))