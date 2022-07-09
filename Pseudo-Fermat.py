from time import sleep
from os import system
from cursor import hide
from Init_Screen import init_screen

init_screen()
system('title Демонстрация соотношения наподобие Теоремы Ферма')
timing = int(input('Просто укажите сколько секунд будете ждать, а затем нажмите Enter ⟶ '))
hide()

s = '⁴'
e = '\n'

a, b, c, d = 2682440, 15365639, 18796760, 20615673
print(e)
print(str(a) + s + ' + ' + str(b) + s + ' + ' + str(c) + s + ' =', a ** 4 + b ** 4 + c ** 4, '=? ' + str(d) + s)
print('Считаем ------------ ⟶ ' + str(d) + s + ' =', d ** 4)
print(e)
print('Компьютер проверяет равенство: ' + str(a) + s + ' + ' + str(b) + s + ' + ' + str(c) + s + ' = ' + str(d) + s)
print('Результат:', a ** 4 + b ** 4 + c ** 4 == d ** 4)

for _ in range(timing):
    system(f'title Наслаждайтесь, а мы заканчиваем через {timing - _} секунд!')
    sleep(1)
