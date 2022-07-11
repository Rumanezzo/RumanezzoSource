a, b = map(int, input('Введите 2 целых числа через пробел -> ').split())

if a < b:
    print(f'Так как {a} < {b} - я их поменяла местами!')
    a, b = b, a

print(f'{a} + {b} = {a + b}')
print(f'{a} ' + chr(183) + f' {b} = {a * b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} : {b} = {a // b}({a % b})')

input('Нажмите на Enter для завершения!')
