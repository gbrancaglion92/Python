#usar while no ex.051
t = int(input('Informe o termo: '))
r = int(input('Informe a razão: '))
c = 0
while c < 10:
    print(t, end=' → ')
    c += 1
    t += r
print('Acabou')
