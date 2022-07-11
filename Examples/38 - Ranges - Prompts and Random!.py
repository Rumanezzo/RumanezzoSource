from random import randint

print('Немного случайностей для начала...')
a = int(input('Вводите низ -> ') or 1)
b = int(input('Вводите верх -> ') or 4)
n = int(input('Сколько надо чисел? -> ') or 5)

for x in range(1, n + 1):
    print(x, randint(a, b), sep='->', end='; ')
print()
name = input('Введите своё имя, или просто нажмите [Enter]! -> ') or 'Anonymous'
print('Приветствую тебя,', name)

b == 0 or print(b // a, '-кратное превосходство!', sep='')
print('Выводим в Цикле содержимое range(1,', n, ')', sep='')
for value in range(1, n):
    print(value)
print('Замечаем, что', n, 'не включено!')
print('Выводим список на основе вашего range(1,', n, ')', sep='')
values = list(range(1, n))
print(values)
input("\nНажмите на Enter для завершения -> ")
