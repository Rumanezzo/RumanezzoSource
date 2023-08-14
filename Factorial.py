from math import factorial

x = [factorial(t) for t in range(10, 200, 10)]

for i in x:
    n = 0
    while not(i % 10):
        n += 1
        i = i // 10
    print(n, end='; ')
