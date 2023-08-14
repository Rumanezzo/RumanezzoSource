import numpy as np
import collections

lst = ('Вася', 'Петя', 'Саша', 'Федя', 'Толя', 'Коля', 'Вася', 'Коля', 'Вася', 'Толя', 'Петя', 'Вася',
       'Федя', 'Саша', 'Катя', 'Коля', 'Федя', 'Сеня', 'Вова', 'Валя', 'Толя', 'Коля', 'Степа', 'Таня',
       'Вася', 'Петя', 'Саша', 'Федя', 'Толя', 'Коля', 'Катя', 'Сеня', 'Вова', 'Степа', 'Таня', 'Игорь')

unique, counts = np.unique(lst, return_counts=True)
freq0 = dict(zip(unique, counts))
freq1 = collections.Counter(lst)

print(freq0)
print(freq1)
            