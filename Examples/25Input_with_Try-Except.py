# Имеется возможность перенаправлять вывод в файл, вызывая *.py > name.txt
def main():
    print('1) Вводите целые числа, разделяя их нажатием на Enter')
    print('2) Просто нажмите на Enter для выхода из программы')
    total = 0
    count = 0

    while True:
        try:
            if count:
                print('Введено чисел ->', count, 'Накопленная сумма ->', total)
            line = input('текущее вводимое целое -> ')
            if line:
                try:
                    number = int(line)
                except ValueError as err:
                    print(err)
                    continue
                total += number
                count += 1
            else:
                if count == 0:
                    print('Ничего не введено...')
                break
        except EOFError:
            break
    if count:
        print('Всего введено чисел ->', count)
        print('Сумма введенных чисел ->', total)
        print('Среднее Арифметическое ->', total / count)
    input('Счастливо оставаться! (Нажмите еще раз Enter)')


if __name__ == '__main__':
    main()
