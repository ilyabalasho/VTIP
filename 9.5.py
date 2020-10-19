import random
L = ['самовар', 'весна', 'лето']
a = random.choice(L)
n = random.randint(0, len(a)-1)
for i in range(len(a)):
    if i == n:
        print('?', end='')
        continue
    print(a[i], end='')
while True:
    f=input('\nRand alph: ')
    if f== a[n]:
        print('Win')
        break
    else:
        print('Not today')
