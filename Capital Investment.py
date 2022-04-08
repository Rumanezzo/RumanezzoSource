import random

from Init_Screen import *
# Здесь 10 платежных матриц, как tuple 10 tuples of 4 tuples of 3 elements
game = (((0.478, 0.337, 0.185), (+0.3, -0.7, +0.7), (-0.3, +0.7, -0.3), (+0.2, +0.1, -0.5)),
        ((0.106, 0.530, 0.364), (-0.5, -0.3, +0.7), (+0.5, -0.5, +0.7), (+0.3, +0.5, -0.7)),
        ((0.415, 0.347, 0.237), (+0.3, -0.7, +0.7), (-0.3, +0.7, -0.3), (+0.4, +0.0, -0.5)),
        ((0.274, 0.346, 0.380), (+0.5, -0.7, +0.4), (-0.3, +0.7, -0.3), (-0.5, +0.2, +0.3)),
        ((0.437, 0.438, 0.125), (+0.6, -0.6, +0.4), (-0.6, +0.8, -0.3), (-0.3, +0.5, -0.3)),
        ((0.304, 0.435, 0.261), (+0.8, -0.7, +0.4), (-0.6, +0.4, +0.2), (-0.2, +0.6, -0.6)),
        ((0.422, 0.390, 0.188), (-0.5, +0.8, -0.3), (+0.7, -0.5, -0.3), (-0.3, +0.1, +0.7)),
        ((0.214, 0.357, 0.429), (+0.3, -0.2, +0.1), (-0.3, +0.4, -0.1), (+0.1, -0.2, +0.2)),
        ((0.222, 0.413, 0.365), (+0.4, -0.4, +0.3), (-0.2, +0.1, +0.1), (-0.1, +0.4, -0.3)),
        ((0.093, 0.463, 0.444), (+0.0, -0.6, +0.7), (-0.6, +0.0, +0.2), (+0.2, +0.8, -0.8)))

greek = ('Ⅰ', 'Ⅱ', 'Ⅲ')
names = ('♦', '☱', '☲', '☴')
start_year = 1900
init_screen()
cursor.hide()
w = 1000
n = int(input('Сколько лет хотите играть? -⟶ '))
success = 0
x, y = 0.33 * w, 0.33 * w
for year in range(start_year, n + start_year):
    os.system('cls')
    choice = random.randint(0, 9)
    print(f'Вложение Капитала, год {year}')
    print()
    print(f'Капитал в начале года равен {w}$')
    print(f'Возможные состояния рынка на {year} год:')
    print()
    print('      Ⅰ      Ⅱ      Ⅲ')
    for i, index in enumerate(game[choice]):
        print(names[i], end=' ')
        for j, index_ in enumerate(index):
            print(f'{index_: 7.3f}', end='')
        print('\n') if i == 0 else print()
    print()

    try:
        x = input('Сколько хотите вложить в предприятие ☱? -⟶ ')
        x = int(x)
    except TypeError:

        print(f'Ввели какую-то фигню, так что вложила за Вас 33%, то есть {0.33 * w}')
    try:
        y = input('Сколько хотите вложить в предприятие ☲? -⟶ ')
        y = int(y)
    except TypeError:
        print(f'Ввели какую-то фигню, так что вложила за Вас 33%, то есть {0.33 * w}')

    z = w - x - y
    print(f'Остаток {z}, вкладываю в ☴')
    q = random.random()
    r = 2
    if q < game[choice][0][0] + game[choice][0][1]:
        r = 1
    if q < game[choice][0][0]:
        r = 0
    print('Состояние рынка', greek[r])
    w0 = w
    w += game[choice][1][r] * x + game[choice][2][r] * y + game[choice][3][r] * z
    w = int(w + 0.5)
    print(f'Ваш капитал теперь равен {w}')
    if (w - w0) > 0:
        success += 1

    print(f'Детализация: {game[choice][1][r]} • {x} + {game[choice][2][r]} • {y} + {game[choice][3][r]} • {z} = {w}')

    key = key_pressed('для продолжения нажмите Shift', 'shift')

if w > 2000:
    print('Потрясающий результат!!! Срочно начинайте играть на бирже! Вы - настоящий Стяжатель!')
elif w > 1750:
    print('Отличный результат! Или Вы везучий, или умелый. В любом случае Вы - молодец!')
elif w > 1400:
    print('Хороший результат! Вы - однозначно в тройке лидеров, но есть куда расти!')
elif w > 1000:
    print('Неплохо... Ещё немного поднажать, и Вы - в тройке лидеров!')
else:
    print('Нет оснований для уныния. Ведь в другой раз наверняка повезет!')
print(f'Вы провели {success} удачных сделок из {n}')
key_pressed('Мы закончили. Нажмите Enter', 'enter')
