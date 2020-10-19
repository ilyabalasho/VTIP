from random import randint
A = 3
B = 5
lst=[[randint(2, 11) for i in range(A)] for i in range(B)]
for i in lst:
    print()
    for j in i:
        print (j, end=" ")
