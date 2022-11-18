import math
import os
import random

os.system('cls')
print('Генерим Случайные Радиусы и считаем Площади Кругов')
n = int(input('Сколько надо Кругов? -> '))
for x in range(n):
    radius = random.randint(25, 50)
    area = math.pi * radius ** 2
    print('%d-й круг с площадью S = %.2f, радиусом R = %d' % (x + 1, area, radius))
input('Нажмите Enter!')
