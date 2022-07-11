import os
from random import randint

os.system('title Чёт или нечет - угадай-ка!')
n_comp = randint(1, 2)
trues = 0
n = int(input('Сколько попыток сможете вынести (max-10) ⟶ '))
half = n // 2
for k in range(n):
    while True:
        answer = int(input('Чёт (введите 0) или Нечет (введите 1)? ⟶ '))
        if answer != 1 and answer != 0:
            print('Надо вводить 0 или 1! Попробуйте ещё раз')
        else:
            break
    print('Число компьютера ⟶ ', n_comp)
    print('То есть Вы...', end='')
    if answer == n_comp:
        print('угадали!')
        trues += 1
    else:
        print('обломились!')
print('Подведём Итоги:')
print('Вы окончательно и без поворотно...', end='')
if trues > half:
    print('Выиграли!')
elif trues == half:
    print('Свели поединок к ничьей!')
else:
    print('Проиграли...')
os.system('pause')
