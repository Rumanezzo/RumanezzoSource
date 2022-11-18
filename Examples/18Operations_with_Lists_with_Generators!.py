from typing import List

n = sum(i * i for i in map(int, input('n -> ')))
print('Сумма квадратов цифр Вашего числа ->', n)

s2: List[int] = [i * (20 - i) for i in range(1, 11)]
s3 = [x for x in s2 if x % 3]
s4 = [x for x in range(100, 1000) if x % 3 == 2 and (x % 5 == 3 and x % 7 == 2)]
s5 = [x for x in range(100, 1000) if x - sum(i * i for i in list(map(int, str(x)))) == 517]

print('Список, заданный генератором ->', s2)
print('Список, не делящихся на 3 чисел из предыдущего списка ->', s3)
print("Трехзначные числа, дающие остатки 2, 3, 2 при делении на 3, 5, 7:")
print(s4)
print("Трехзначные числа, отличающиеся от суммы квадратов своих цифр на 517:")
print(s5)

input('Press Enter!')
