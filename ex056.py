#nome, idade e sexo de 4 pessoas

soma_idades = 0
media_idades = 0
mulheres_jovens = 0
homem_velho = 0
nomevelho = ''

for i in range (1, 5):
    print('---{}ª PESSOA---'.format(i))
    nome = input('Nome: ')
    idade = float(input('Idade: '))
    genero = input('Gênero [F/M]: ')
    #média das idades
    if idade == 1:
        soma_idades = idade
    else:
        soma_idades += idade
    media_idades = (soma_idades / 4)
    #F com menos de 21 anos
    if genero in 'Ff':
        if idade < 21:
            mulheres_jovens += 1
    #nome homem mais velho
    if genero in 'Mm' and i == 1:
        homem_velho = idade
        nomevelho = nome
    if genero in 'Mm' and idade > homem_velho:
        homem_velho = idade
        nomevelho = nome

print('A soma total de idades é \033[33m{}\033[m e sua média é \033[33m{}\033[m'.format(soma_idades, media_idades))
print('O homem mais velho tem \033[33m{}\033[m anos e se chama \033[33m{}\033[m'.format(homem_velho, nomevelho))
print('Existem \033[33m{}\033[m mulheres com menos de 21 anos.'.format(mulheres_jovens))
