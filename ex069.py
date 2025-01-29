s_idade = s_homens = s_mulheres = 0

print('-'*10,'CADASTRE UMA PESSOA','-'*10)

while True:
    idade = int(input('Informe a idade: '))
    nome = str(input('Informe o nome: '))
    genero = str(input('Informe o gênero: ')).upper().strip()[0]

    while genero not in 'MF':
        genero = str(input('Informe o gênero: ')).upper().strip()[0] #força o usuário a inserir uam opção
    while cont not in 'SN':
        cont = str(input('Deseja cadastrar mais um usuário? ')).upper().strip()[0]

    if idade > 18:
        s_idade += 1
    if genero == 'M':
        s_homens += 1
    if genero == 'F' and idade < 20:
        s_mulheres += 1

    cont = str(input('Deseja cadastrar mais um usuário? ')).upper().strip()[0]
    if cont == 'N':
        break

print(f'Foram cadastrados {s_idade} pessoas com mais de 18 anos')
print(f'Ao todo temos {s_homens} homens cadastrados')
print(f'E temos {s_mulheres} mulheres com menos de 20 anos cadastradas.')
