from Init_Screen import init_screen, non_start_in_ide
from os import getcwd, environ
from math import pi, e, factorial
from sys import getwindowsversion, version_info, platform

non_start_in_ide()
init_screen()

print('Ваша Платформа ->', platform)
print('Версия Операционной системы ->', getwindowsversion())

print('Здесь информация о версии Python ->', version_info)
print('Из модуля os текущий каталог ->', getcwd())


print('Число π ->', pi)
print('Число e ->', e)
n = input('Введите натуральное число, а я найду его факториал -> ')
print(f'Вычисляем {n}! =', factorial(int(n)))
input('Для завершения - нажимайте Enter! -> ')
