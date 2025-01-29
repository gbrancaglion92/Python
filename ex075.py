lista_n = []
c = c_pares = c_nove = 0
for i in range (1,5):
    num = int(input(f'Informe o {i}º número: '))
    lista_n.append(num)
    if num % 2 == 0:
        c_pares += 1
    if num == 9:
        c_nove += 1

tpl_num = tuple(lista_n)
print(f'A tupla gerada foi \033[33m{tpl_num}\033[m')

#números 9
if c_nove == 1:
    print(f'O número 9 aparece \033[33m{c_nove}\033[m vez.')
else:
    print(f'O número 9 aparece \033[33m{c_nove}\033[m vezes.')

# números pares
if c_pares == 1:
    print(f'Foi inserido \033[33m{c_pares}\033[m número par.')
else:
    print(f'Foram inseridos \033[33m{c_pares}\033[m números pares.')

# em que posição está o 1º 3
print(f'O primeiro número 3 aparece na posição \033[33m{tpl_num.index(3)}\033[m.')



_____
Resolução Guanabara
num = (int(input('Informe um número: ')), int(input('Informe um número: ')), int(input('Informe um número: ')), int(input('Informe um número: ')))
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3) + 1} posição')
else:
    print(f'O valor 3 não foi digitado.')
print(f'Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

