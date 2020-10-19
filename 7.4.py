import random
def test():
    print(str('число от 10 до 15'))
    a = int(input("Ваше число: "))
    b = random.randint(10, 15)
    if a == b:
        print('Победа, ', b)
    else:
        print('not today')
test()
