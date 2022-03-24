from colorama import init
from termcolor import colored, cprint
from Init_Screen import *

x0, y0 = init_screen()

init()  # из модуля colorama корректной работы цвета в консоли
text = colored('Мы умеем так!', 'red', 'on_yellow', attrs=['bold'])
print(text)
cprint('А ещё можем так!', 'green', 'on_red', attrs=['dark'])

key_pressed(colored('Нажмите какую-нибудь клавишу или shift для прекращения опроса', 'red'), 'shift')
key_pressed(colored('Просто ещё одна проверка и тоже shift для прекращения опроса', 'green'), 'shift')
key_pressed(colored('Последняя проверка, для завершения программы - также shift', 'yellow'), 'shift')
