print('Находим Наибольший Общий Делитель 2х чисел')
a = int(eval(input('Вводим a -> ')))
b = int(eval(input('Вводим b -> ')))

while a != b:
    if a > b:
        a = a - b
        print(a, end='->')
        input()
    if a < b:
        b = b - a
        print(b, end='->')
        input()

print('это Наибольший Общий Делитель!')
if a == 1:
    print('Похоже у нас здесь Взаимная Простота!')

input('Press Enter!')
