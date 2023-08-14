# Типы данных - материал иллюстративный для 1-го занятия

def type_ident(lst):
    for _ in lst:    
        if type(_) == int:
            print(f'{_} - целое число')
        elif type(_) == float:
            print(f'{_} - десятичная дробь')
        elif type(_) == str:
            print(f'{_} - строка')
        elif type(_) == bool:
            print(f'{_} - логическое выражение')

lst0 = (12, '12', 13.5, 'Вася', 2 + 4, 5 / 2, "5 / 2", '2 + 2 == 4', 2 + 2 == 4, 135, 5.67, "13.5")
type_ident(lst0)
