from math import sqrt
def test(a, b, c):
    p = (a+b+c)/2
    S = sqrt(abs(p*(p-a)*(p-b)*(p-c))) 
    return S
a = float(input('a: ' ))
b = float(input('b: ' ))
c = float(input('c: ' ))
test(a, b, c)
print(test(a, b, c))
