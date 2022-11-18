from random import randint
from time import time

# First Way
t1 = time()
a = []
for i in range(1000000):
    a.append(randint(1, 10))
t2 = time()
print('1 способ ->', round(t2 - t1, 2), 'сек')
# Second Way
b = []*1000000
for i in range(1000000):
    b[i] = randint(1, 10)
t3 = time()
print('2 способ ->', round(t3 - t2, 2), 'сек')
# Third Way
c = [randint(1, 10) for _ in range(1000000)]
t4 = time()
print('3 способ ->', round(t4 - t3, 2), 'сек')
input('«Нажмите «Enter» для завершения ••••» ')
