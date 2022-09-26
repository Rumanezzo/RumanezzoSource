from os import chdir, getcwd, listdir, remove
# Скрипт удаляет файла из каталога - Внимание!
shift = 3
chdir('d:/Programs/ScanKromsator/Tempsk/')
print(f'Текущая папочка -> {getcwd()}')
dirs = listdir()
print(f'Её содержимое -> {dirs}')

for i in dirs:
    name = int(i[:-4])
    if (name - shift) % 4:
        print(f'Удаляем {i}')
        remove(i)
