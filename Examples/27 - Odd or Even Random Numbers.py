import os
from random import randint

n_comp = randint(1, 2)
trues = 0
n = int(input('Сколько попыток сможете вынести (max-10) -> '))
for k in range(n):
    while True:
        answer = int(input('Чёт (введите 2) или Нечет (введите 1)? -> '))
        if answer != 1 and answer != 2:
            print('Надо вводить 1 или 2! Попробуйте ещё раз')
        else:
            break
    print('Число компьютера -> ', n_comp)
    print('То есть Вы...', end='')
    if answer == n_comp:
        print('угадали!')
        trues += 1
    else:
        print('обломились!')
print('Подведём Итоги:')
print('Вы окончательно и без поворотно...', end='')
if trues > n // 2:
    print('Выиграли!')
else:
    print('Проиграли')
os.system('pause')
