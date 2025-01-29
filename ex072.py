n_extensos = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove','dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if not 0 <= n <= 20:
        n = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {n_extensos[n]}.')
    cont = str(input('Deseja continuar? ')).strip().upper()[0]
    if cont == 'S':
        continue
    else:
        print('Programa encerrado.')
        break
