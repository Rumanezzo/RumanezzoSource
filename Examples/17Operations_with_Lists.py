s0 = [10, 20, 30]
s1 = [15, 54, 12, 34, 23, 22, 21, 72, 53, 25, 17, 19, 89]
enum = enumerate(s1)
print('enumerate в цикле:')
for i in enum:
    print(i)
print('Список заданный ->', s1)
print('Список задом-наперед ->', list(reversed(s1)))
print('В список', s0, 'вставили [1,2] и получилось:')

s0.insert(1, [1, 2])
print(s0)
s0[2:2] = [3, 4]
print(s0)
s0[2:3] = [100, 200]
print(s0)

print(s1)
print("Удаляем элемент с индексом 5 ->", s1.pop(5))
print(s1)
s1.remove(21)
print(s1)
del s1[3]
print(s1)
s1[2:5] = []
print(s1)
s1[1:3] = [-1, -2, -3, -4, -5]
print(s1)

input("\nНажмите на Enter для завершения -> ")
