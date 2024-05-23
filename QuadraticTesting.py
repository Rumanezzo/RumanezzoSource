from math import sqrt
game = True

while game:
    a, b, c = input('Введите коэффициенты квадратного уравнения через пробел-> ').split()

    a, b, c = map(int, (a, b, c))
    if a*a + b*b + c*c == 0:
        game = False
    if a == 0:
        break
    d = b ** 2 - 4 * a * c
    print(f'Вы ввели a={a}, b={b}, c={c} => D={d},', end=' ')

    if d > 0:
        print(f'{d}>0 => У нас 2 корня')
        sqrt_d0 = sqrt(d)
        if int(sqrt_d0) == sqrt_d0:
            sqrt_d0 = int(sqrt_d0)
            print(f'{d}={sqrt_d0}² => могу решать!... Но пока не хочу!')
        else:
            print(f'{d} - не является квадратом. Не хочу работать с "кривым" дискриминантом!')
    elif d == 0:
        x = -b / (2 * a)
        print(f'а раз так, то у нас 1 корень x={x:.2f}...но это не точно!')
        print(f'На самом деле надо поставить минус перед {b} и поделить на удвоенное {a}')

    elif d < 0:
        print(f'{d}<0 => У нас (точнее у Вас) *нет* корней')
