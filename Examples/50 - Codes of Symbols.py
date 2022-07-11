#  Не запускаем в IDE!!!
from Init_Screen import hide, init_screen, system, key_pressed

hide()
init_screen()
system('title Выводим символы по их кодам!!!')

col = 9
while True:
    system('cls')
    start = int(input('Введите Начальный Код ───→ ') or 9472)
    finish = input('А теперь Конечный ──────────→ ') or (str(start + 255))

    system('cls')
    print()
    r = start % col
    for x in range(start, int(finish) + 1):
        print(x, ' ┈┈ ', chr(x), end='⎪', sep='')
        if x % col == col - 1:
            print()
    key = key_pressed('\nДля продолжения нажмите Shift!, для завершения - Enter!', 'shift', 'enter')
    if key == 'enter':
        break
