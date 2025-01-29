#Computador pensa em um número, o usuário digita para ver se adivinhou

from random import randint

pc = randint(0,100)
print('-=-'*20)
print('Vou pensar em um número entre 0 e 100... Tente advinhar!')
print('-=-'*20)

n=int(input('Em que número pensei? '))

if pc == n:
    print('Você adivinhou!')
else:
    print('Você errou, eu pensei no número {}'.format(pc))
