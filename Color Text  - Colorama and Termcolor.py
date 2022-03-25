from colorama import init
from termcolor import colored, cprint
from Init_Screen import *

init_screen()

init()  # из модуля colorama корректной работы цвета в консоли
cursor.hide()
color_symbol = ('red', 'green', 'grey', 'yellow', 'magenta', 'cyan', 'blue', 'white')
color_back = []
for color in color_symbol:
    color_back.append('on_' + color)
print(color_back)
print(colored('Мы умеем так! - 1', 'red', 'on_yellow', attrs=['reverse']))
print(colored('Мы умеем так! - 2', 'green', 'on_magenta', attrs=['reverse']))
print(colored('Мы умеем так! - 3', 'grey', 'on_red', attrs=['reverse']))
print(colored('Мы умеем так! - 4', 'green', 'on_cyan', attrs=['reverse']))
#
cprint('А ещё можем так!', 'green', 'on_red', attrs=['reverse'])
cprint('А ещё можем так!', 'red', 'on_green', attrs=['reverse'])

key_pressed(colored('Проверка цвета - shift для продолжения', 'red'), 'shift')
key_pressed(colored('Просто ещё одна проверка и тоже shift для продолжения', 'green'), 'shift')
key_pressed(colored('Просто ещё одна проверка и тоже shift для продолжения', 'magenta'), 'shift')
key_pressed(colored('Просто ещё одна проверка и тоже shift для продолжения', 'cyan'), 'shift')
key_pressed(colored('Просто ещё одна проверка и тоже shift для продолжения', 'grey','on_white'), 'shift')

key_pressed(colored('Последняя проверка, для завершения программы - также shift', 'yellow'), 'shift')
