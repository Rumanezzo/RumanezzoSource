# Здесь две реализации - "ручная" и через таблицу перевода символов
def digit_in_circle(n):
    nests = ''
    for i in range(len(n)):
        nests += s[int(n[i])]
    return nests


s = [chr(9312 + i) for i in range(9)]
s.insert(0, chr(9711))

stars = ''
for i in range(10):
    stars += s[i]

table = ''.maketrans('0123456789', stars)

a, b = input('Введите 2 целых слагаемых без нулей в записи через пробел -> ').split()
print('Вы ввели', a.translate(table), 'и', b.translate(table))

c = str(int(a) + int(b))
sa, sb, sc = map(digit_in_circle, (a, b, c))

res = f'Вот, что у меня получилось: {sa} + {sb} = {sc}'
print(res)
input('Нажмите на Enter для завершения!')
