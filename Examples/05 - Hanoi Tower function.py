def hanoi(n, k, m):
    """ n  - number of disks, k - with, m - on"""
    if n == 0:
        return
    p = 6 - k - m
    hanoi(n - 1, k, p)
    print(k, '->', m)
    hanoi(n - 1, p, m)


n_ = int(input('Вводите сколько дисков перекладываем -> '))
hanoi(n_, 1, 3)

input('Я закончила. Нажмите Enter!')
