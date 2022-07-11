from Init_Screen import system, key_pressed, hide
from time import sleep
from random import randint

game = True  # Пока истина - крутимся в главном цикле

system('title Игра - "Королевство Эйфория" - пробная версия!')
gamer = input('Введите Ваше Имя, сир... -⟶ ')
n_years = input(f'Сколько лет Вы, {gamer} намереваетесь править? -⟶ ')
n_start = 1900
n_current = n_start  # Текущий год - начинаем с 1900
n = 1  # Считаем годы правления
n_before_end = n_years  # Храним сколько лет осталось до заявленного конца

square_land_all = 1000
prise_of_land = 2


def events_of_year():
    events_key = randint(1, 100)
    print(f'Вам выпало {events_key} событие и это пока не о чём...')


while game:
    system('cls')
    print(f'{n_current}-й год вашего правления')
    print(f'У Вас в распоряжении {square_land_all} гектаров земли')
    hide()
    question = f'Не хотите ли сбежать, не на своём {n} году правления? shift - да, ctrl - нет'

    key = key_pressed(question, 'shift', 'ctrl')
    if key == 'shift':
        game = False
        continue

    square_land_used = int(input('Сколько гектаров земли хотите засеять -⟶ '))
    square_land_sold = int(input('Сколько земли хотите продать? -⟶ '))
    square_land_free = square_land_all - square_land_used - square_land_sold

    if square_land_free:
        print(f'У вас осталось незадействованными -⟶ {square_land_free}')

    print(f'Итак - вы засеяли {square_land_used} гектар, продали {square_land_sold} гектар земли')

    print(f'Осталось незадействованными -⟶ {square_land_free} гектар')
    print('Сейчас у Вас больше нет никаких возможностей, поэтому запускаю цикл обработки событий за год...')

    hide()
    sleep(5)
    system('cls')
    n_current += 1
    n_before_end -= 1
    n += 1

    print(f'Наступает следующий {n_current}-й год, Вам осталось править {n_before_end} лет...')

key_pressed("Нажмите на ★Enter★ или ★Shift★ для завершения...", 'enter', 'shift')
