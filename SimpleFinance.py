# Для тестирования - запускаем в Терминале IDE ->.\SimpleFinance.py


from datetime import datetime
from os import system
from InitScreen import key_pressed, hide

from locale import setlocale, LC_ALL

setlocale(
    category=LC_ALL,
    locale="Russian"
)
version = 'v0.993'

names = ('Влад⋅', 'Коля⋅', 'Дана⋅', 'Даня⋅', 'Свят⋅', 'Ника⋅', 'Макс⋅')

hm_names = len(names)
labels = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '=', '!', '@', '#', '$', '%', '^', '&', '*', '+',)

rate = 250  # Стоимость "тика" (7.5 минут реального времени - 6 тиков = 1 ак.ч.) 5 тиков - 1250р, 9 тиков - 2250р


class RecordLesson:
    def __init__(self, now_date=None, pupil=None, n_ticks=9, cash=2250, was=0, paid=0):
        if now_date:
            self.now_date = now_date
        else:
            self.now_date = datetime.now().strftime('%y%m%d%H%M%S')

        self.month = datetime.now().strftime('%m %B').split(' ')  # Список: Номер месяца - Название месяца
        self.pupil = pupil
        self.n_ticks = n_ticks
        self.cash = cash
        self.was = was
        self.paid = paid

    def __str__(self):
        rec_for_write = str(self.now_date) + ' ' + str(self.pupil) + ' ' + str(self.n_ticks) + ' ' + str(
            self.cash) + ' ' + str(self.was) + ' ' + str(self.paid)
        return rec_for_write


class RecordMonth:
    def __init__(self, month, month_profit):
        self.year = datetime.now().strftime('%y')
        self.month = month
        self.month_profit = month_profit
        print('Начался Новый Месяц...')
        with open('SimpleMonthFinance.txt', 'a') as fm:
            print(str(self.year) + str(month) + ' ' + str(month_profit), file=fm)


if __name__ == "__main__":
    now = datetime.now().strftime('%d-е, %B, %Y год')
    system(f'title {now} - SimpleFinance - Бухгалтерия на Минималках {version} - ©Rumanezzo')
    hide()
    start = True
    file = 'SimpleFinance.txt'
    [print(f'{name} ⟶ {labels[i]}') for i, name in enumerate(names)]
    num_str = key_pressed('Вводите номер ученика:', *labels)

    while start:
        number = labels.index(num_str)
        cur_name = names[number]
        print(f'●●●● {cur_name} ●●●●')
        n_ticks0 = int(key_pressed('Сколько тиков?', '4', '5', '6', '8', '9', '0'))
        if n_ticks0 == 0:
            n_ticks0 = 10
        print(f'●●●● {n_ticks0} тиков ●●●●')
        cash0 = rate * n_ticks0
        was0 = int(key_pressed('Занятие проведено? 1 - Да, 0 - Нет:', '0', '1'))
        paid0 = int(key_pressed('Занятие оплачено? 1 - Да, 0 - Нет:', '0', '1'))
        if n_ticks0 == 10:
            n_ticks0 = 0
        record = RecordLesson(pupil=cur_name, was=was0, paid=paid0, n_ticks=n_ticks0, cash=cash0)
        print(record)
        profit_counter = 0
        n_month = int(record.month[0])
        prev_month = str(n_month - 1) if n_month > 1 else '12'
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
                    RecordMonth(prev_month, profit_counter)

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
        num_str = key_pressed('Еще один ученик? ... или 0 для выхода', 'r', *labels, '0')
        #  system('cls')

        if num_str == 'r':
            profit_counter = 0
            with open(file, 'r', encoding='utf-8') as f:
                for x in f:
                    record_list = x.split(' ')
                    profit_counter += int(record_list[3])
            print(f'Накопленная Зарплата за весь год -> {profit_counter} р')
            key = key_pressed('Выходим?', '1', '0')
            if key == '1':
                exit()

        elif num_str == '0':
            exit()
