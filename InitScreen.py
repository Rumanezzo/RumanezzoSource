from os import system, get_terminal_size, environ

from keyboard import read_event, KEY_DOWN
from cursor import hide, show


def non_start_in_ide():
    if 'pycharm_hosted' in environ:
        print('Не надо запускать этот скрипт в Pycharm!')
        show()
        r = input('Если тем не менее хотите попробовать запустить нажмите введите ★yes★ на клавиатуре: ')
        if r != 'yes':
            exit()


def set_mod(columns, lines):
    system('mode ' + str(columns) + ',' + str(lines))
    system('title Запускаемся с использованием InitScreen!')
    system('cls')


def key_pressed(prompt, *key_in):
    print(prompt)

    while True:
        event = read_event()
        if event.event_type == KEY_DOWN:
            key = event.name
            if key in key_in:
                break
    return key


def get_screen():
    try:
        x, y = get_terminal_size()
        set_mod(x, y)

    except OSError:
        print('Похоже вы пытаетесь запустить скрипт из-под IDE... -> не надо...!')
        x, y = 106, 32
    return x, y


def resize(prompt, key_in, x, y):
    system('title ' + prompt)
    while True:
        event = read_event()
        if event.event_type == KEY_DOWN:
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

    return x, y


def init_screen():
    try:
        with open('screen.txt', 'r') as f_scr:
            line = f_scr.readline()

        line_list = line.split()
        x0, y0 = map(int, line_list)
        set_mod(x0, y0)

    except FileNotFoundError:
        f_scr = open('screen.txt', 'w')
        x1, y1 = get_screen()
        x0, y0 = resize('Меняем размер экрана. Просто нажимайте стрелки, а когда надоест - shift', 'shift', x1, y1)
        print(f'Судя по всему Вам понравилась Ширина {x0} и Высота {y0}')
        coord_for_writing = str(x0) + ' ' + str(y0)
        f_scr.write(coord_for_writing)

    return x0, y0


def main():
    hide()
    init_screen()
    key_pressed('Для продолжения нажмите Shift!', 'shift')


if __name__ == "__main__":
    non_start_in_ide()
    system('mode 92, 24')
    system('title Вы запустили модуль InitScreen... Зачем вы это сделали?!... Вы об этом пожалеете!')
    print('Вы точно уверены, что вам надо было запускать этот модуль???')
    key_out = key_pressed('Для продолжения нажмите ♦Shift♦, для отказа нажмите ♦Ctrl♦', 'shift', 'ctrl')

    if key_out == 'ctrl':
        exit()

    main()
