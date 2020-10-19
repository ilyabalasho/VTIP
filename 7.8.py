import random
def test():
    a1 = random.randint(1, 6)
    a2 = random.randint(1, 6)
    if a1>a2:
        print('Победил  1,', a1)
    elif a2>a1:
        print('Победил  2,', a2)
    elif a1 == a2:
        print('Ничья')
test()
