from datetime import date

atual = date.today().year
ano_nascimento = int(input('Informe sua idade: '))
idade = atual - ano_nascimento
alistamento = 18

if idade < 18:
    print('Você tem {} anos e ainda não tem idade para se alistar. Faltam {} anos para você se alistas.'.format(idade, alistamento-idade))
elif idade == 18:
    print('Você tem {} anos, está na idade para se alistar.'.format(idade))
else:
    print('Você tem {} anos e deveria ter se alistado há {} anos.'.format(idade, idade-alistamento))