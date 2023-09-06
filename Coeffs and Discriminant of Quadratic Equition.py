smb = ('•', '²')


def quadro(a, b, c):
    d = b ** 2 - 4 * a * c
    return f'{a}•x² + {b}•x + {c} = 0', f'D = {b}² - 4•{a}•{c} = {d}'


print(quadro(2, 3, 1)[0])
print(quadro(3, 2, 4)[1])
a0, b0, c0 = list(map(int, input('a = ?, b = ?, c = ? ').split()))
print(quadro(a0, b0, c0)[0])
print(quadro(a0, b0, c0)[1])
input('Enter! -> ')
