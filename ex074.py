import random
lista_randons = []
for i in range (0,5):
    lista_randons.append(random.randint(1, 10))
tpl_randons = tuple(lista_randons)

print(f'Os valores sorteados foram: \033[33m{tpl_randons}\033[m')
print(f'O maior valor sorteado foi \033[33m{max(tpl_randons)}\033[m')
print(f'O menor valor sorteado foi \033[33m{min(tpl_randons)}\033[m')
print(f'Números organizados \033[33m{sorted(tpl_randons)}\033[m')

