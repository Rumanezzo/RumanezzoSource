# 'Короткая Версия' условного оператора
l, r, ob, stl, sto, rt = chr(8810), chr(8811), chr(8413), chr(8592) + chr(9598), chr(9598) + chr(8594) + ' ', chr(8730)

while True:
    reply = input('Вводите любое число, или z' + ob + 'для выхода ' + sto)
    if reply == 'z':
        break  # Это и есть короткая версия if!!!
    try:
        num = int(reply)
    except ValueError:
        print('Вы ввели не число, а так, я бы вычислила корень!')
        print(l + reply.lower() + r, stl, 'это вообще что?!')
    else:
        print(rt, num, '=', num ** .5, sep='')

print('Пока - пока!!!')
input("Нажмите на Enter для завершения " + sto)
