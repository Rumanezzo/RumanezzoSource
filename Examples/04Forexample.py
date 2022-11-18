txt = input("Введите Текст без пробелов -> ")
i = 1

for s in txt:
    t = str(i) + "-я буква:"
    print(t, s)
    i += 1

input("Работа завершена! Нажми Клавишу Enter!")
