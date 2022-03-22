import os
import keyboard


def set_mod(columns, lines):
    cmd = 'mode ' + str(columns) + ',' + str(lines)
    os.system(cmd)


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

        return x_, y_
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


try:
    with open('screen.txt', 'r') as f_inst:
        line = f_inst.readline()

    line_list = line.split()
    x0, y0 = map(int, line_list)
    set_mod(x0, y0)
    print('Прочитали из файла ->', line)


except FileNotFoundError:
    f_inst = open('screen.txt', 'w')
    x0, y0 = screen_init()
    x1, y1 = resize('Пробуем менять размер экрана. Просто нажимайте стрелки, а когда надоест - shift', 'shift', x0, y0)
    print(f'Судя по всему Вам понравилась Ширина {x1} и Высота {y1}')
    coord_for_writing = str(x1) + ' ' + str(y1)
    f_inst.write(coord_for_writing)

f_inst.close()

on_click_input('Для завершения нажмите Shift!', 'shift')
