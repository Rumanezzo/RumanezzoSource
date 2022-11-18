x = int(input('Введите натуральное число -> '))
if x == 2:
    print('Это число простое!')
elif x % 2 == 0:
    print('Это число простым не является! Оно - чётное!')
else:  # - нечётное число
    n_div = 2  # denominators - знаменатель - делитель
    cur_div = 3
    while cur_div * cur_div <= x:
        if x % cur_div == 0:
            n_div += 2
            break
        cur_div += 2
    if n_div == 2:
        print('Это число простое!')
    else:
        print('Это число простым не является! У него >', n_div - 1, 'делителей!')

input("Нажмите на Enter для завершения -> ")
