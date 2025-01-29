n = []
for i in range (0,5):
    n.append(int(input(f'Digite um valor para a posição {i}: ')))
print('\033[33m/\033[m'*50)
print(f'\033[33mA lista gerada foi {n}\033[m')
print('\033[33m/\033[m'*50)

n.sort()
print(f'Lista organizada {n}')

maior = max(n)
posicao_maior = [i for i, v in enumerate(n) if v == maior]
if len(posicao_maior) == 1:
    print(f'O maior número digitado foi {max(n)} que está na posição {posicao_maior[0]}')
else:
    print(f'O maior número digitado foi {max(n)} que está nas posições {posicao_maior}')

menor = min(n)
posicao_menor = [i for i, v in enumerate(n) if v == menor]
print(f'O menor número digitado foi {min(n)} que está nas posições {posicao_menor}')