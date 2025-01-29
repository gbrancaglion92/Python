from datetime import  date
tbl_brasileirao = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'EC Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Ahtletico-PR', 'Cicriúma', 'Atlético-Go', 'Cuiabá')
ano_anterior = (date.today().year) - 1

print('-*'*30)
print(f'Os 5 primeiros colocados em {ano_anterior} foram: ')
for posicao, time in enumerate(tbl_brasileirao[:5], start=1):
    print(f'\033[33m{posicao}º {time}\033[m')
print('-*'*30)
print(f'Os 4 últimos colocados foram: ')
for posicao, time in enumerate(tbl_brasileirao[-4:], start=17):
    print(f'\033[33m{posicao}º {time}\033[m')
print('-*'*30)
print(f'Lista em ordem alfabética: \033[33m\n{sorted(tbl_brasileirao)} \033[m')
print('-*'*30)
print(f'O Corinthians ficou em \033[33m{tbl_brasileirao.index('Corinthians')+1}º\033[m lugar.')
