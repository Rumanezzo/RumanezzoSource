import os
import time
from random import randint

w1 = 0
w2 = 0

# Ввод имён играющих
player1 = input('Введите имя 1-го игрока -> ')
player2 = input('Введите имя 2-го игрока -> ')
n = int(input('Сколько Партий? -> '))

while n:
    time.sleep(2)
    os.system('cls')
    # Моделирование бросания кубика 1-м игроком
    print('Кубик бросает', player1)
    n1 = randint(1, 6)
    print('Выпало -> ', n1)

    # Моделирование бросания кубика 2-м игроком
    print('Кубик бросает', player2)
    n2 = randint(1, 6)
    print('Выпало -> ', n2)

    # Определение результата (3 возможных варианта)
    if n1 > n2:
        print('Выиграл -> ', player1)
        w1 += 1
    elif n1 < n2:
        print('Выиграл -> ', player2)
        w2 += 1
    else:
        print('Ничья!')
    n -= 1
print('Подводим Итоги...')
time.sleep(5)
print('Итоговый Счёт ->', w1, ':', w2)
input("\nНажмите на [Enter] для завершения -> ")
