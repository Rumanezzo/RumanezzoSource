import random
list1 = ['Марина', 'Маруся', 'Яна']
list2 = ['Прохиндейка', 'Поросёночек', 'Лапочка']

random.shuffle(list1)
random.shuffle(list2)


list3 = list(zip(list1, list2))
list4 = []
for word in list3:
    list4.append(word[0] + '-' + word[1])
print(list4)
input('Нажмите Enter для завершения -> ')
