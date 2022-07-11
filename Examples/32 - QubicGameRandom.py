from Init_Screen import system, key_pressed, hide
from time import sleep
from random import randint

system('title Игра для двоих - имитация бросания кубика заданное количество раз!')
w1, w2 = 0, 0

# Ввод имён играющих
player1 = input('Введите имя 1-го игрока -⟶ ')
player2 = input('Введите имя 2-го игрока -⟶ ')
n = int(input('Сколько партий играем? -⟶ '))
hide()
print('Готовимся к великому противостоянию...')
sleep(3)

while n:
    sleep(1)
    system('cls')
    # Моделирование бросания кубика 1-м игроком
    print('Кубик бросает', player1)
    n1 = randint(1, 6)
    print('Выпало -⟶', n1)

    # Моделирование бросания кубика 2-м игроком
    print('Кубик бросает', player2)
    n2 = randint(1, 6)
    print('Выпало ⟶', n2)

    # Определение результата (3 возможных варианта)
    if n1 > n2:
        print('Выиграл -⟶', player1)
        w1 += 1
    elif n1 < n2:
        print('Выиграл -⟶', player2)
        w2 += 1
    else:
        print('Ничья!')
    n -= 1
    system(f'title Играют {player1} и {player2}. Количество оставшихся партий - {n}. Текущий счёт: {w1} ÷ {w2}')

print('Подводим Итоги...')
sleep(3)
system('cls')
print(f'Итоговый Счёт -⟶ {w1} ÷ {w2}')

result = f'Победил {player1}' if w1 > w2 else f'Победил {player2}'
if w1 == w2:
    result = 'Ничья!'
print(result)

key_pressed("Нажмите на ★Enter★ или ★Shift★ для завершения...", 'enter', 'shift')
