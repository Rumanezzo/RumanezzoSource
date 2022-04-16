from os import system, get_terminal_size
from time import sleep

import keyboard
import cursor


def set_mod(columns, lines):
    cmd = 'mode ' + str(columns) + ',' + str(lines)
    system(cmd)


def key_pressed(prompt, *key_in):
    print(prompt)

    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name
            if key in key_in:
                break
    return key


def get_screen():
    try:
        x, y = get_terminal_size()
        set_mod(x, y)
        return x, y
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
            elif key == 'f11' or 'alt+enter':
                if full_scr == 0:
                    print('Внимание! Вы вышли в полноэкранный режим!')
                    full_scr = 1
                else:
                    set_mod(x, y)
                    full_scr = 0
            else:
                pass

    return x, y


def init_screen():
    try:
        with open('screen.txt', 'r') as f_inst:
            line = f_inst.readline()

        line_list = line.split()
        x0, y0 = map(int, line_list)
        set_mod(x0, y0)

    except FileNotFoundError:
        f_inst = open('screen.txt', 'w')
        x1, y1 = get_screen()
        x0, y0 = resize('Меняем размер экрана. Просто нажимайте стрелки, а когда надоест - shift', 'shift', x1, y1)
        print(f'Судя по всему Вам понравилась Ширина {x1} и Высота {y1}')
        coord_for_writing = str(x0) + ' ' + str(y0)
        f_inst.write(coord_for_writing)

    f_inst.close()
    return x0, y0


def main():
    cursor.hide()
    init_screen()
    key_pressed('Для продолжения нажмите Shift!', 'shift')


if __name__ == "__main__":
    set_mod(106, 20)
    system('title Вы запустили модуль Init_Screen... Зачем вы это сделали?!... Вы об этом пожалеете!')
    print('Вы точно уверены, что вам надо было запускать этот модуль???')
    key_out = key_pressed('Для продолжения нажмите ♦Shift♦, для отказа нажмите ♦Ctrl♦', 'shift', 'ctrl')

    if key_out == 'ctrl':
        exit()
    print('Начнем через 5 сек!')
    sleep(5)
    main()
