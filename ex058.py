#melhora do ex028

from random import randint
tentativas = 1
pc = randint(0,10)
print('/'*30)
print('Advinhe o número que eu pensei')
print('/'*30)

n = int(input('Qual número pensei? '))
while pc != n:
    n = int(input('Você errou, não foi esse que pensei. Tente mais uma vez: '))
    tentativas += 1
print('Parabéns, você acertou! Foram necessárias {} chutes para acertar.'.format(tentativas))
