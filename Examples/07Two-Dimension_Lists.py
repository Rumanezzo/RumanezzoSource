width = 4


def beauty_matrix(x):
    print('Красиво:')
    for i in range(len(x)):
        print(' '.join(map(lambda num: ' ' * (width - len(str(num))) + str(num), x[i])))


n, m = map(int, input('[Длина строки] -> [пробел] -> [Количество строк] -> ').split())
a = [[i] * n for i in range(m)]
beauty_matrix(a)
print('Вводим числа [пробел!], образующие:')
b = [list(map(int, input(str(i + 1) + '-ю строку!' + ' осталось - ' + str(m - i - 1) + '\n').split())) for i in
     range(m)]
beauty_matrix(b)
input('Нажмите на Enter для завершения')
