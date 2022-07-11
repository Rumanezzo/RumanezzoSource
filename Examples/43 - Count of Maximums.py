n = int(input('Сколько чисел? -> ')) or 9
print('Вводите числа - нажимайте после каждого на Enter')

count = 1
maxis = 0

for i in range(n):
    current = int(input(f'{n - i} -> '))
    if i == 0:
        maxis = current
    elif current > maxis:
        count = 1
        maxis = current
    elif current == maxis:
        count += 1

print('В вашем вводе максимумов ->', count)
input('Нажмите на Enter, чтобы закончить!')
