from random import randint

tokens = [1] * 91 # 0-й элемент не используется!

for i in range(1, 91):
    b = randint(1, 90)
    print(f'Кричу {i}-й раз!')
    while tokens[b] == 0:
        b = randint(1, 90)
    tokens[b] = 0
    print(f'Фишка №{b}...', end='')

    if b == 7:
        print('Кочерга')
    elif b == 11:
        print('Барабанные Палочки')
    elif b == 12:
        print('Дюжина')
    elif b == 13:
        print('Чертова Дюжина')
    elif b == 22:
        print('Уточки')
    elif b == 44:
        print('Стульчики')
    elif b == 69:
        print('Туда и обратно')
    elif b == 77:
        print('Топорики')
    elif b == 80:
        print('Бабка')
    elif b == 90:
        print('Дед')
    else:
        print()
    input()

print('Мешок опустошен!')
input('Нажмите Enter для завершения!')
