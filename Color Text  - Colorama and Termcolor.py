import random

from colorama import init  # для нормального вывода на консоль, иначе в windows - глюки
from termcolor import colored, cprint
from Init_Screen import hide, init_screen, key_pressed

width, height = init_screen()

init()  # из модуля colorama корректной работы цвета в консоли
hide()  # прячем курсор в окне консоли
color_symbol_lst = ['red', 'green', 'grey', 'yellow', 'magenta', 'cyan', 'blue', 'white']
color_back_lst = []
for color in color_symbol_lst:
    color_back_lst.append('on_' + color)

color_back = 'on_grey'

print('Программа демонстрирует работу с цветом в консоли'.center(width, '▓'))

print()

for i, color in enumerate(color_symbol_lst):
    out = f'{i}-й раз выводим {color}'
    how_many = width // len(out)
    width_word = width // how_many
    color_back = 'on_white' if color == 'grey' else 'on_grey'

    cprint(out.center(width_word, '▓') * how_many, color, color_back)
    # можно обернуть строку в метод colored() и распечатывать её print

print()

for color_back in color_back_lst:
    color = 'grey' if color_back == 'on_white' else 'white'
    print(colored('ᛝ' * width, color, color_back))

random.shuffle(color_symbol_lst)
random.shuffle(color_back_lst)

color_pairs = list(zip(color_symbol_lst, color_back_lst))

print()

for color_pair in color_pairs:
    if color_pair[0] != color_pair[1][3:]:
        out = f'█{color_pair[0]} - цвет символов, {color_pair[1][3:]} - цвет фона█' * 2
        cprint(out.center(width, '▓'), color_pair[0], color_pair[1])

print('\n')

key_pressed(colored('Демонстрация завершена - для завершения программы нажмите shift',
                    random.choice(color_symbol_lst)).center(width), 'shift')
