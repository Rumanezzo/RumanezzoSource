# Не запускать из-под IDE!
from os import get_terminal_size, getcwd
from sys import getwindowsversion, version_info, platform
from math import pi, e, factorial

print('Ваша Платформа ->', platform)
print('Версия Операционной системы ->', getwindowsversion())

print('Здесь информация о версии Python ->', version_info)
print('Из модуля os текущий каталог ->', getcwd())
print('Из модуля os берем размер консоли ->', get_terminal_size())
print('Число π ->', pi)
print('Число e ->', e)
print('Вычисляем 100! =', factorial(100))
input('Для завершения - нажимайте Enter! -> ')
