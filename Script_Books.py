from os import chdir, getcwd, listdir, remove
from sys import argv

# Скрипт удаляет файла из каталога - Внимание!
shift = 4
if len(argv) > 1:
    print(len(argv))
    chdir(argv[1])
else:
    chdir('d:/Temp/1/')
    print('Вы не указали папку для обработки - использую по умолчанию...')

print(f'Текущая папочка -> {getcwd()}')
dirs = listdir()
print(f'Её содержимое -> {dirs}')
key = input('Нажмите Enter для начала обработки, или 1 + Enter для отмены -> ')
if key:
    exit(1)

for i in dirs:
    name = i[:-4]
    print(name)
    name = int(name)
    if (name - shift) % 6:
        print(f'Удаляем {i}')
        remove(i)
input('Завершено! Нажмите Enter')
