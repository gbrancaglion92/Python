from random import randint

from jupyter_client.session import json_packer

itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)

print('-=-'*20)
print('''Suas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
print('-=-'*20)
jogador = int(input('Escolha pedra, papel ou tesoura: '))
print('O computador escolheu {}'.format(itens[computador]))
print('-=-'*20)
if computador == 0: #PEDRA
    if jogador == 0: #pedra
        print('Empate')
    elif jogador == 1: #papel
        print('Você venceu')
    elif jogador == 2: #tesoura
        print('O computador venceu')
    else:
        print('Jogada inválida')
elif computador == 1: #PAPEL
    if jogador == 0: #pedra
        print('O computador venceu')
    elif jogador == 1: #papel
        print('Empate')
    elif jogador == 2: #tesoura
        print('Você venceu')
    else:
        print('Jogada inválida')
elif computador == 2: #TESOURA
    if jogador == 0: #pedra
        print('Você venceu')
    elif jogador == 1: #papel
        print('O computador venceu')
    elif jogador == 2: #tesoura
        print('Empate')
    else:
        print('Jogada inválida')
