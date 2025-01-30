n = []
for c in range(0, 5):
    n.append(int(input(f'Informe o {c + 1}º valor da posição {c}: ')))

maior = max(n)
menor = min(n)
p_maior = [i for i, v in enumerate(n) if v == maior]
p_menor = [i for i, v in enumerate(n) if v == menor]

print('\033[33m/\033[m'*30)
print(f'Você digitou os valores {n}')
if len(p_maior) > 1:
    print(f'O maior número o é {maior} que se encontra nas posições {p_maior}')
else:
    print(f'O maior número o é {maior} que se encontra na posição {p_maior}')

if len(p_menor) == 1:
    print(f'O menor número o é {menor} que se encontra na posição {p_menor}')
else:
    print(f'O menor número o é {menor} que se encontra nas posições {p_menor}')
    