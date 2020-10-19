x = 0
while True:
    a = input('число или  \'Стоп\' для summ: ')
    if str(a) == 'Стоп':
        print('Ваша сумма равна: ', x)
        break
            
    else:
        x = x + int(a)
