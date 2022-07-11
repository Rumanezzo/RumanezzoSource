from random import randint, seed

seed()
n = 5
correct = 0
for k in range(n):
    while True:
        ans = int(input('[Чёт] -> (2) или [Нечет] -> (1) => ('))

        if ans != 1 and ans != 2:
            print('Вводи 1 или 2! И не тупи! Пробуй снова!')
        else:
            break
    ans_ = randint(1, 2)
    print('Число компьютера -> ', ans_)
    if ans == ans_:
        correct += 1
print('Счёт', correct, ':', n - correct, '=> ', end='')
if correct > n // 2:
    print('Выигрыш!')
else:
    print('Проигрыш!')

input("\nНажмите на Enter для завершения -> ")
