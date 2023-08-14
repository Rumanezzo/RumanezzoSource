from InitScreen import system, key_pressed, hide, show
from time import sleep
from random import randint

game = True  # Пока истина - крутимся в главном цикле

system('title Игра - "Королевство Эйфория" - пробная версия!')
gamer = input('Введите Ваше Имя, сир... -⟶ ')
n_years = int(input(f'Сколько лет Вы, {gamer}, собираетесь править? -⟶ '))
n_start = 1911
n_current = n_start  # Текущий год - начинаем с 1911
n = 1  # Считаем годы правления
n_before_end = n_years  # Храним сколько лет осталось до заявленного конца

square_land_all = 1000
prise_of_land = 2


def events_of_year():
    events_key = randint(1, 100)
    print(f'Вам выпало {events_key} событие и это пока не о чём...')
    return events_key


while game:
    system('cls')
    print(f'На дворе {n_current}-й год')
    print(f'Великодушный диктатор {gamer} правит {n}-й год')
    print(f'У Вас в распоряжении {square_land_all} акров (приблизительно {0.4 * square_land_all} га) земли')
    hide()
    question = f'Хотите сбежать, на своём {n}-м году правления? ★Shift★ - нет, ★Ctrl★ - да'
    key = key_pressed(question, 'shift', 'ctrl')

    if key == 'ctrl':
        game = False
        continue
    show()
    square_land_used = int(input('Сколько акров земли хотите засеять -⟶ '))
    square_land_sold = int(input('Сколько акров земли хотите продать? -⟶ '))
    square_land_free = square_land_all - square_land_used - square_land_sold

    if square_land_free:
        print(f'У вас осталось незадействованными акров -⟶ {square_land_free} ')

    print(f'Итак - вы засеяли {square_land_used} акров, продали {square_land_sold} акров земли')

    print('Сейчас у Вас больше нет никаких возможностей, поэтому запускаю цикл обработки событий за год...')
    event = events_of_year()
    print(f'Вам прилетело -⟶ {event}')

    hide()
    sleep(5)

    n_current += 1
    n_before_end -= 1
    n += 1

    print(f'Наступает следующий {n_current}-й год, Вам осталось править {n_before_end} лет...')
    key_pressed('Нажмите ★Shift★ для продолжения', 'shift')

key_pressed("Нажмите на ★Enter★ для завершения...", 'enter')
