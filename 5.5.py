test = int()
def call(test):
    test = int(input("kод вашего города: "))
    if test == 343:
        print("Екатеринбург")
        a = round(float(input("количество минут звонка: ")))
        a = a*15
        print('Стоимость:', a)
    elif test == 381:
        print("Омск")
        a = round(float(input("количество минут")))
        a = a*18
        print('Стоимость', a)
    elif test == 473:
        print("Воронеж")
        a = round(float(input("количество минут")))
        a = a*13
        print('Стоимость', a)
    elif test == 485:
        print("Ярославль")
        a = round(float(input("количество минут")))
        a = a*11
        print('Стоимость:', a)
    else:
        print("Error") 
call(test)
