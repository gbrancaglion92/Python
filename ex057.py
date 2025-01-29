#input genero da pessoa, se estiver errado, peça para inserir novamente
#só aceita M ou F

genero = str(input('Informe seu gênero: ')).strip().upper()[0]
while genero not in 'MmFf':
    genero = str(input('Dados inválidos, por favor informe F ou M: ')).strip().upper()[0]
print('Você selecionou a opção {}.'.format(genero))
