from time import time

low = int(input('Вводите нижнюю границу -> ') or 100000)
high = int(input('Вводите верхнюю границу -> ') or 1000000)
div = int(input('На какое число делятся -> ') or 63)
# Закат Солнца в ручную - около 60 с
start = time()
lst = [x for x in range(low, high) if not(eval('*'.join(list(str(x)))) % div)]
finish = time()
timing = finish - start
print('Всего получилось', len(lst), 'чисел, на вычисления ушло ->', format(timing, '3.2f'), 'с')
# Арифметический алгоритм - около 10 с
start = time()
numbers = 0
for i in range(low, high):
    digit = i
    product = 1
    while digit:
        product *= digit % 10
        digit //= 10
    if not(product % div):
        numbers += 1
finish = time()
timing = finish - start
print('Всего получилось', numbers, 'чисел, на вычисления ушло ->', format(timing, '3.2f'), 'с')
input('Нажмите «Enter» для завершения ••••')
