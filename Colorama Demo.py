import colorama
from colorama import Fore, Back, Style

from Init_Screen import key_pressed, system
system('title просто играемся с модулем colorama')
#  Запускаем либо в IDE, либо Start.cmd 'Colorama Demo.py'
colorama.init()
print(Fore.LIGHTRED_EX + Back.BLUE + 'Красноватый текст и Голубой фон')
print(Fore.GREEN + Back.LIGHTBLACK_EX + 'Зеленый текст и Сероватый фон')
print(Fore.BLACK + Back.LIGHTCYAN_EX + 'Черный текст и light cyan фон')
print(Fore.LIGHTBLACK_EX + Back.CYAN + 'Черноватый текст и cyan фон')
print(Fore.YELLOW + Back.LIGHTGREEN_EX + 'желтый текст и зеленоватый фон')
print(Fore.LIGHTCYAN_EX + Back.GREEN + 'light cyan текст и зеленый фон')
print(Fore.LIGHTBLUE_EX + Back.YELLOW + 'Голубоватый текст и желтый фон')
print(Fore.LIGHTWHITE_EX + Back.BLACK + 'Беловатый текст и черный фон')
print(Fore.WHITE + Back.LIGHTBLACK_EX + 'Белый текст и черноватый фон')
print(Style.RESET_ALL)
print('Теперь обычный текст на обычном фоне - для сравнения!')

with open('Font.txt') as f:
    source = f.read().split('\n')

key_pressed('Выходим, отработав по Shift', 'shift')
