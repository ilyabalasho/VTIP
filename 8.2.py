x = str(input(''))
n = 10
def test(x, n):
    d = len(x)
    if d > n:
        print(x.upper())
    else:
        print(x)
test(x, n)
