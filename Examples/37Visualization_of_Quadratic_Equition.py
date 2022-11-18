# -*- coding: UTF-8 -*-
from math import sqrt


def vis(coefficient):
    coefficient_str = ''
    if coefficient > 0:
        coefficient_str = ' + ' + str(coefficient)
    elif coefficient == 0:
        coefficient_str = ''
    elif coefficient < 0:
        coefficient_str = ' - ' + str(-coefficient)
    return coefficient_str


print('Вводите целые [!] коэффициенты уравнения ax² + bx + c = 0')

while True:
    try:
        a = int((input('a ⟶ ')) or 3)
        b = int((input('b ⟶ ')) or -17)
        c = int((input('c ⟶ ')) or 14)
        print("Вы ввели a =", a, "b =", b, "c =", c)
    except ValueError:
        print('Видимо вы криво вводите данные - введу-ка я их за вас!')
        a, b, c = 3, -17, 14

    if a == 1:
        a_str = ''
    else:
        a_str = str(a)

    b_str = vis(b)
    c_str = vis(c)

    eqn = a_str + 'x²' + b_str + 'x' + c_str + ' = 0'

    print('Ваше Квадратное уравнение ---⟶', eqn)
    D = b ** 2 - 4 * a * c
    ds = '² - 4•' if a * c > 0 else '² + 4•'
    print('Ваш Дискриминант --⟶ D = ', abs(b), ds, abs(a), '•', abs(c), ' = ', D, sep='')
    if D > 0:
        print('У Вас 2 корня')
        if int(sqrt(D)) == sqrt(D):
            d_sqrt_str = str(int(sqrt(D)))
            print('"Хорошенький" Дискриминант! D =', d_sqrt_str + '²')
            print('√D =', d_sqrt_str)
        else:
            print('"Кривенький" Дискриминант, поэтому попробуем оценить его квадратный корень')
            print(f'{int(sqrt(D))} < √{D} < {int(sqrt(D)) + 1}')
    elif D == 0:
        print('У Вас 1 корень')
    else:
        print('Нет корней!')
    x = input('Продолжаем? Нажмите ⟶[enter] или для выхода ⟶[q] + [enter] ----⟶ ')
    if x == 'q':
        break
