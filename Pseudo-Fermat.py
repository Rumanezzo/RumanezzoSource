from time import sleep
from os import system
from cursor import hide
from InitScreen import init_screen

init_screen()
system('title Демонстрация соотношения наподобие Теоремы Ферма')
timing = int(input('Укажите сколько секунд будете любоваться выводом, а затем нажмите Enter ⟶ '))
hide()
system('cls')

s = '⁴'

a, b, c, d = 2682440, 15365639, 18796760, 20615673
print('Немного вычислений:')
print(str(a) + s + ' + ' + str(b) + s + ' + ' + str(c) + s + ' =', a ** 4 + b ** 4 + c ** 4)
print('\nГипотеза:')
print('Это число совпадает с⟶ ' + str(d) + s + '?')
print('Считаем -------------⟶ ' + str(d) + s + ' =', d ** 4)
print()
print('Кажется у нас совпадение!')
print('Компьютер проверяет равенство: ' + str(a) + s + ' + ' + str(b) + s + ' + ' + str(c) + s + ' = ' + str(d) + s)
print('Компьютер утверждает -⟶ ', a ** 4 + b ** 4 + c ** 4 == d ** 4)

for _ in range(timing):
    system(f'title Наслаждайтесь, а мы заканчиваем через {timing - _} секунд!')
    sleep(1)
