# Не запускать в IDE см. примечание ниже!
import os
from math import pi, e, factorial
from sys import getwindowsversion, version_info, platform


def set_mod(columns, lines):
    cmd = 'mode ' + str(columns) + ',' + str(lines)
    os.system(cmd)


def screen_init():
    try:
        x0, y0 = os.get_terminal_size()
        set_mod(x0, y0)
        print(f'Из модуля os берем размер консоли -> {x0} - ширина, {y0} - высота')
        x1, y1 = map(int, input('Меняем размер окна на Ваш ☻: [ширина]⎵[высота] ⟶ ').split() or (106, 32))
        set_mod(x1, y1)
    except OSError:
        print('Похоже вы пытаетесь запустить скрипт из-под IDE...')


# Следующая команда "мешает" запустить скрипт в IDE
screen_init()

print('Ваша Платформа ->', platform)
print('Версия Операционной системы ->', getwindowsversion())

print('Здесь информация о версии Python ->', version_info)
print('Из модуля os текущий каталог ->', os.getcwd())


print('Число π ->', pi)
print('Число e ->', e)
n = input('Введите натуральное число, а я найду его факториал -> ')
print(f'Вычисляем {n}! =', factorial(int(n)))
input('Для завершения - нажимайте Enter! -> ')
