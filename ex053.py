#input string e diga se é palíndromo - desconsiderando espaços = ex. apos a sopa

import unicodedata

frase = str(input('Informe uma frase: '))
frase_sem_espaco = frase.replace(' ', '').lower()
frase_invertida = frase_sem_espaco[::-1]

print('=-=' * 10)
print('Sua frase foi ', frase_sem_espaco)
print('/' * 20)
print('A frase limpa fica ', frase_invertida)
print('=-=' * 10)

if frase_invertida == frase_sem_espaco:
    print('A frase é um palíndroo')
else:
    print('A frase não é um palíndromo')