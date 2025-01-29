#contagem regressiva de 10 até 0 com pausa de 1 segundo

import time

print('Contagem regressiva')
print('=-='*20)

for c in range (10, -1, -1):
    print(c)
    time.sleep(1)

print('Feliz ano novo!')