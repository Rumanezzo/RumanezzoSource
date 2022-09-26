# Запускаем в Терминале IDE: .\SimpleFinance.py
from datetime import datetime
from os import system
from Init_Screen import key_pressed, hide

from locale import setlocale, LC_ALL

setlocale(
    category=LC_ALL,
    locale="Russian"
)

names = ('Лева ', 'Влад ', 'Дима ', 'Серж ', 'Настя', 'Дамир', 'Коля ', 'Дана ', 'Эрик ')


how_many_names = len(names)
list_of_number = [str(x) for x in range(1, how_many_names + 1)]

rate = 1000  # стоимость академического часа


class Record:
    def __init__(self, now_date=None, pupil=None, n_hours=2, cash=2000, was=0, paid=0):
        if now_date:
            self.now_date = now_date
        else:
            self.now_date = datetime.now().strftime('%y%m%d%H%M%S')

        self.month = datetime.now().strftime('%m %B').split(' ')  # Лист - Номер месяца - Название месяца
        self.pupil = pupil
        self.n_hours = n_hours
        self.cash = cash
        self.was = was
        self.paid = paid


if __name__ == "__main__":
    system('title SimpleFinance - Бухгалтерия на Минималках v0.9 - ©Rumanezzo')

    hide()
    file = 'SimpleFinance.txt'

    while True:
        now = datetime.now().strftime('%B %d-е, %Y год')
        print(f'Сегодня {now}')
        [print(f'{i + 1} -> {j}') for i, j in enumerate(names)]
        number = int(key_pressed('Вводите номер ученика:', *list_of_number))

        print(f'●●●● {names[number - 1]} ●●●●')
        n_hours0 = int(key_pressed('Сколько часов?', '1', '2'))
        print(f'●●●● {n_hours0} ак. ч. ●●●●')
        cash0 = rate * n_hours0
        was0 = int(key_pressed('Занятие проведено? 1 - Да, 0 - Нет:', '0', '1'))
        paid0 = int(key_pressed('Занятие оплачено? 1 - Да, 0 - Нет:', '0', '1'))

        new_record = Record(pupil=names[number - 1], was=was0, paid=paid0, n_hours=n_hours0, cash=cash0)
        profit_counter = 0
        prev_month = str(int(new_record.month[0]) - 1)
        if len(prev_month) == 1:
            prev_month = '0' + prev_month
        try:
            with open(file, 'r', encoding='utf-8') as f:
                for x in f:
                    record_list = x.split(' ')

                    if record_list[0][2:4] == prev_month:
                        profit_counter += int(record_list[3])
                print(f'В предыдущем месяце Вы заработали {profit_counter} р')
                if record_list[0][2:4] != new_record.month[0]:
                    print('Начался Новый Месяц!')
                    with open('SimpleMonthFinance.txt', 'a') as fm:
                        fm.write(str(prev_month) + ' ' + str(profit_counter))
        except FileNotFoundError:
            print('Нет файла с записями об учениках!')
            exit(1)

        record_for_writing = str(new_record.now_date) + ' ' + str(new_record.pupil) + ' ' + str(new_record.n_hours
                                                                                                ) + ' ' + str(
            new_record.cash) + ' ' + str(new_record.was) + ' ' + str(new_record.paid) + '\n'
        with open(file, 'a', encoding='utf-8') as f:
            f.write(record_for_writing)

        profit_counter = 0
        with open(file, 'r', encoding='utf-8') as f:
            for x in f:
                record_list = x.split(' ')
                if record_list[0][2:4] == new_record.month[0]:
                    profit_counter += int(record_list[3])

        print(f'Накопленная Зарплата за {new_record.month[1]} -> {profit_counter} р')
        #  print(new_record.__dict__)
        key = key_pressed('Еще один ученик?', '1', '0')
        system('cls')
        if key == '0':
            exit()
