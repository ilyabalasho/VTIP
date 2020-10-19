import math
b =  int(input('0<=x<= 360: '))
x = math.radians(b)
def t(x):
    y = math.sin(x)**2                   
    a = math.sqrt(1-y)
    print (a)
t(x)
print(t(x))
