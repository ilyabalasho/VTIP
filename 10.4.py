import random
def test():
    print(str('numb 1 до 200'))
    d = random.randint(1, 200)
    while True:
        a = input("\ur numb\'Выход\': ")
    if a == 'ex':
            print('\nВ unlucky :(')
            break
        a = int(a)
        if a == d:
            print('win, ', d)
            break
        elif a>d:
            print('\n over > n!')
        elif a<d:
            print('\n num < n!')
test()
