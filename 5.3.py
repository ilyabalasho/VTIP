a = ()
def test(a):
    a = int(input('Введите целое число a:'))
    if a%2 == 0:
        print('Значение "a" четное')
    else:
        print('Значение "a" нечетное')
test(a)
