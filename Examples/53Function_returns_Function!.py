from math import sin, cos, radians


def f(s):
    if s == 'sin':
        return sin
    elif s == 'cos':
        return cos
    else:
        return lambda x: x


st = input('Вводите выражение вида sin 15 или cos 33 -> ').split()
print(st[0], st[1], '=', f(st[0])(radians(eval(st[1]))))
input('Press Enter!')
