# Не запускать в IDE!
from Init_Screen import system, hide
from time import perf_counter

system('cls')
system('title Все внимание - Заголовок окна')
hide()


print("◊-----------------------------------------◊")
print("  Пока Вы здесь страдаете фигнёй           ")
print("  Я очень важным делом занимаюсь           ")
print("  Хоть в праве Вас считать большой Свиньей ")
print("  Зачем-то Вам понравиться пытаюсь...      ")
print("◊-----------------------------------------◊")
print()

for _ in range(1000000, 2000000, 100000):
    time_start = perf_counter()
    x = len(str(2 ** _))
    time_finish = perf_counter()
    t = round(time_finish - time_start, 2)

    system(f" title {_}-я степень двойки содержит ⟶ {x} цифр, на вычисления ушло ⟶ {t} сек")

input("\nНажмите на Enter для завершения!")
