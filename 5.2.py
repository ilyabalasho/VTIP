a = int()
b = int()
def max(a, b):
    a = int(input('Введите целое число для а: '))
    b = int(input('Введите целое число для b: '))
    if a > b:
        print('max = ', a)
    elif b>a:
        print('max = ', b)
    else:
        print('a <> b')
max(a, b)
