import time

print('Алгоритм Евклида "Python-like". Числа - натуральные))')
a = int(input('Введите a -> '))
b = int(input('Введите b -> '))
start = time.time()
while b:
    a, b = b, a % b
print('Ваш "Python-like" Наибольший Общий Делитель =', a)
print('Время поиска ->', time.time() - start, 'с')
input('Нажмите Enter для Выхода! -> ')
