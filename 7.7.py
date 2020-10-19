import math
x = float(input('Введите значение x: '))
a=1.0
f = ()
def test(f, x, a):
    if 0.2<=x<=0.9:
        z = math.sin(x)
        print("f = ", z)
    elif a:
        print("f = ", a)

test(f, x, a)
