import math
def test():
    x = int(input('Введите х: '))
    y = int(input('Введите y: '))
    z = (x+((2+y)/x**2))/(y+(1/(math.sqrt(x**2 + 10))))
    print(z)
test()



def test0():
    c =  int(input('0<=x<= 360 градусов: '))
    y = int(input('Введите y: '))
    x = math.radians(c)
    q = 2.8*math.sin(x) + math.fabs(y)
    print(q)
test0()
