import os

import keyboard
from colorama import init
from termcolor import colored, cprint


def set_mod(columns, lines):
    cmd = 'mode ' + str(columns) + ',' + str(lines)
    os.system(cmd)
    return


def on_click_input(prompt, key_in):
    print(prompt)

    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if key == key_in:
                break
            print(f'Pressed: {key}')
    return key


def screen_init():
    try:
        x_, y_ = os.get_terminal_size()
        set_mod(x_, y_)
        print(f'Из модуля os берем размер консоли -> {x_} - ширина, {y_} - высота')
        x1, y1 = map(int, input('Меняем размер окна на Ваш ☻: [ширина]⎵[высота] ⟶ ').split() or (106, 32))
        set_mod(x1, y1)
        return x1, y1
    except OSError:
        print('Похоже вы пытаетесь запустить скрипт из-под IDE...')


def resize(prompt, key_in, x_, y_):
    full_scr = 0
    print(prompt)
    x, y = x_, y_
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name

            if key == key_in:
                break
            elif key == 'down':
                y += 1
                set_mod(x, y)
            elif key == 'up':
                y -= 1
                set_mod(x, y)
            elif key == 'right':
                x += 1
                set_mod(x, y)
            elif key == 'left':
                x -= 1
                set_mod(x, y)
            elif key == 'f11':
                if full_scr == 0:
                    print('Внимание! Вы вышли в полноэкранный режим!')
                    full_scr = 1
                else:
                    set_mod(x, y)
                    full_scr = 0
            else:
                print(f'Pressed: {key}')
    return x, y


x0, y0 = screen_init()
x2, y2 = resize('Пробуем менять размер экрана. Просто нажимайте стрелки, а когда надоест - shift', 'shift', x0, y0)
print(f'Судя по всему Вам понравилась Ширина {x2} и Высота {y2}')
init()  # из модуля colorama корректной работы цвета в консоли
text = colored('Мы умеем так!', 'red', 'on_yellow', attrs=['bold'])
print(text)
cprint('А ещё можем так!', 'green', 'on_red', attrs=['dark'])

on_click_input(colored('Нажмите какую-нибудь клавишу или shift для прекращения опроса', 'red'), 'shift')
on_click_input(colored('Просто ещё одна проверка и тоже shift для прекращения опроса', 'green'), 'shift')
on_click_input(colored('Последняя проверка, для завершения программы - также shift', 'yellow'), 'shift')
