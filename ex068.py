from random import randint
tot = 0
pc = randint(0,100)

print('-='*30)
v = int(input('Digite um valor: '))
opcao = str(input('Você quer par ou ímpar? [P/I] ')).upper()
s = pc + v

if s % 2 == 0:
    resultado = 'PAR'
if s % 2 != 0:
    resultado = 'IMPAR'

while resultado == opcao:
    final = 'GANHOU'
    tot += 1

    print('-' * 30)
    print(f'Você jogou {v} e o computador {pc}. O total deu {s} {resultado}')

    print('VOCÊ VENCEU')
    print('Vamos jogar novamente...')

    print('-=' * 30)
    v = int(input('Digite um valor: '))
    opcao = str(input('Você quer par ou ímpar? [P/I] ')).upper()
    s = pc + v

    if s % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'IMPAR'

if resultado != opcao:
    final = 'PERDEU'

    print('-' * 30)
    print(f'Você jogou {v} e o computador {pc}. O total deu {s} {resultado}')
    print('-' * 30)

    print(f'VOCÊ PERDEU')
    print(f'GAME OVER. Você venceu {tot} vezes')
