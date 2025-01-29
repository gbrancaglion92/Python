num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para binário é '.format(num), bin(num))
elif opcao == 2:
    print('{} convertido para octal é '.format(num), oct(num))
elif opcao == 3:
    print('{} convertido para hexadecimal é '.format(num), hex(num))