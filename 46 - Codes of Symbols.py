from os import system

col = 9
while True:
    system('cls')
    start = int(input('Введите Начальный Код ··→ ') or 9472)
    # finish = input('А теперь Конечный ······→ ') or (str(start + 255))
    finish = start + 255
    system('cls')
    print()
    r = start % col
    for x in range(start, finish + 1):
        print(x, ' ┈┈ ', chr(x), end='⎪', sep='')
        if x % col == col - 1:
            print()
    if input('\n' + 'Нажмите Enter для продолжения и q для завершения ⟶ ') == 'q':
        break
