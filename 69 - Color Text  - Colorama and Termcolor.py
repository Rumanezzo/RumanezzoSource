from colorama import init
from termcolor import colored, cprint
from Init_Screen import *

init_screen()

init()  # из модуля colorama корректной работы цвета в консоли
cursor.hide()

print(colored('Мы умеем так!', 'red', 'on_yellow', attrs=['bold']))
print(colored('Мы умеем так!', 'green', 'on_magenta', attrs=['bold']))
#
cprint('А ещё можем так!', 'green', 'on_red', attrs=['dark'])
cprint('А ещё можем так!', 'yellow', 'on_green', attrs=['dark'])

key_pressed(colored('Проверка цвета - shift для продолжения', 'red'), 'shift')
key_pressed(colored('Просто ещё одна проверка и тоже shift для продолжения', 'green'), 'shift')
key_pressed(colored('Просто ещё одна проверка и тоже shift для продолжения', 'magenta'), 'shift')
key_pressed(colored('Просто ещё одна проверка и тоже shift для продолжения', 'red'), 'shift')
key_pressed(colored('Последняя проверка, для завершения программы - также shift', 'yellow'), 'shift')
