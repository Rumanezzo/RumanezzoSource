from os import chdir, getcwd, listdir, remove
# Скрипт удаляет файла из каталога - Внимание!
chdir('d:/Programs/')
print(f'Текущая папочка -> {getcwd()}')
dirs = listdir()
print(f'Её содержимое -> {dirs}')

for i in dirs:
    name = int(i[:-4])
    if name % 4:
        print(f'Удаляем {i}')
        remove(i)
