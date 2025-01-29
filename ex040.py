n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
media = (n1 + n2) / 2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f} e ele está '.format(n1, n2, media))
if media <= 5:
    print('reprovado')
elif 5 < media < 6.9:
    print('em recuperação')
else:
   print('aprovado')
