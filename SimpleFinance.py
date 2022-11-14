# Для тестирования - запускаем в Терминале IDE: .\SimpleFinance.py
from datetime import datetime
from os import system
from Init_Screen import key_pressed, hide

from locale import setlocale, LC_ALL

setlocale(
    category=LC_ALL,
    locale="Russian"
)
version = 'v0.95'

names = ('Лева0', 'Влад⋅', 'Дима⋅', 'Серго', 'Настя', 'Дамир', 'Коля⋅', 'Дана⋅', 'Эрик⋅', 'Фёдор', 'Лева1', 'Слава')

hm_names = len(names)
labels = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '=', '+', '@', '*', '!', '$', '%', '^')

rate = 1000  # стоимость академического часа


class RecordLesson:
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

    def __str__(self):
        rec_for_write = str(self.now_date) + ' ' + str(self.pupil) + ' ' + str(self.n_hours) + ' ' + str(
            self.cash) + ' ' + str(self.was) + ' ' + str(self.paid)
        return rec_for_write


class RecordMonth:
    def __init__(self, year, month, month_profit):
        self.year = year
        self.month = month
        self.month_profit = month_profit
        print('Начался Новый Месяц!')
        with open('SimpleMonthFinance.txt', 'a') as fm:
            print(str(year) + str(month) + ' ' + str(month_profit), file=fm)


if __name__ == "__main__":
    system(f'title SimpleFinance - Бухгалтерия на Минималках {version} - ©Rumanezzo')

    hide()
    file = 'SimpleFinance.txt'

    while True:
        now = datetime.now().strftime('%d-е, %B, %Y год')
        print(f'{now}')

        [print(f'{name} ⟶ {labels[i]}') for i, name in enumerate(names)]
        num_str = key_pressed('Вводите номер ученика:', *labels)
        if num_str in ('-', '=', '+', '@', '*', '!', '$', '%', '^'):
            number = 10
        else:
            number = int(num_str)
        cur_name = names[number]
        print(f'●●●● {cur_name} ●●●●')
        n_hours0 = int(key_pressed('Сколько часов?', '1', '2'))
        print(f'●●●● {n_hours0} ак. ч. ●●●●')
        cash0 = rate * n_hours0
        was0 = int(key_pressed('Занятие проведено? 1 - Да, 0 - Нет:', '0', '1'))
        paid0 = int(key_pressed('Занятие оплачено? 1 - Да, 0 - Нет:', '0', '1'))

        record = RecordLesson(pupil=cur_name, was=was0, paid=paid0, n_hours=n_hours0, cash=cash0)
        profit_counter = 0
        prev_month = str(int(record.month[0]) - 1)
        if len(prev_month) == 1:
            prev_month = '0' + prev_month
        try:
            with open(file, 'r', encoding='utf-8') as f:
                for x in f:
                    record_list = x.split(' ')

                    if record_list[0][2:4] == prev_month:
                        profit_counter += int(record_list[3])
                print(f'В предыдущем месяце Вы заработали {profit_counter} р')
                if record_list[0][2:4] != record.month[0]:
                    RecordMonth('22', prev_month, profit_counter)

        except FileNotFoundError:
            print('Нет файла с записями об учениках!')
            exit(1)

        with open(file, 'a', encoding='utf-8') as f:
            print(record, file=f)

        profit_counter = 0
        with open(file, 'r', encoding='utf-8') as f:
            for x in f:
                record_list = x.split(' ')
                if record_list[0][2:4] == record.month[0]:
                    profit_counter += int(record_list[3])

        print(f'Накопленная Зарплата за {record.month[1]} -> {profit_counter} р')
        #  print(new_record.__dict__)
        key = key_pressed('Еще один ученик?', '1', '0')
        system('cls')
        if key == '0':
            exit()
