# Не запускать в IDE см. примечание ниже!
from os import get_terminal_size, getcwd
from sys import getwindowsversion, version_info, platform
from math import pi, e, factorial

print('Ваша Платформа ->', platform)
print('Версия Операционной системы ->', getwindowsversion())

print('Здесь информация о версии Python ->', version_info)
print('Из модуля os текущий каталог ->', getcwd())
try:
    print('Из модуля os берем размер консоли ->', get_terminal_size())
except OSError:
    print('Похоже вы пытаетесь запустить скрипт из-под IDE...')

# Следующая команда "мешает" запустить скрипт в IDE

print('Число π ->', pi)
print('Число e ->', e)
print('Вычисляем 1000000! =', factorial(1000000))
input('Для завершения - нажимайте Enter! -> ')
