word = input('Введите слово по-заковыристее -> ') or 'синхрофазотрон'

print('Анализируем слово', word)

word_set = sorted(set(word))

collect = []
for i in word_set:
    x = word.count(i)
    print(i, '->', x)
    collect.append(x)
dic1 = zip(word_set, collect)
print(dict(dic1))

input('Нажмите Enter для завершения -> ')
