n = int(input('Введите Число от 1 до 99 -⟶ '))

n1 = n // 10

if n1 <= 3:
    print('X' * n1, end='')
elif n1 == 4:
    print('XL', end='')
elif 4 < n1 < 9:
    print('L' + 'X' * (n1 - 5), end='')
elif n1 == 9:
    print('LC', end='')

n = n % 10

if n <= 3:
    print('I' * n)
elif n == 4:
    print('IV')
elif 4 < n < 9:
    print('V' + 'I' * (n - 5))
elif n == 9:
    print('IX')

input("Нажмите на Enter для завершения -⟶ ")
