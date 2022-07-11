from time import sleep, localtime, strftime
import locale
import calendar
from Init_Screen import hide, system, init_screen, key_pressed

system('title Выводим точное время и текущую дату')
init_screen()
hide()

d = ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье')
m = ('', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября',
     'октября', 'ноября', 'декабря')

t = localtime()

print('Выводим время и дату с "ручным" форматированием:')
print(f'{t[2]:02d}.{t[1]:02d}.{t[0]:02d}\n{d[t[6]]}, {t[2]} {m[t[1]]} {t[0]} года,'
      f' {t[3]:02d}:{t[4]:02d}:{t[5]:02d}')

print('\nАвтоматический вывод без локализации:')
t_str = strftime('День недели - %A, Месяц - %B, Время: %H:%M:%S Дата: %d.%m.%Y, Пояс: %z')
print(t_str)

print('\nАвтоматический вывод - локализованный см. в заголовке окна!!!')
locale.setlocale(locale.LC_ALL, 'Russian_Russia.1251')
sleep(5)
count = 20
while count > 0:
    t_str = strftime('[День недели] - %A, [Месяц] - %B, [Время] - %H:%M:%S')
    sleep(1)
    count -= 1
    system(f'title {t_str} - обновление экрана через - {count} с.')

system('cls')
system('title Выводим календарь 3-х ближайших месяцев: предыдущий, текущий, следующий!')
calendar = calendar.LocaleTextCalendar(0, ('Russian_Russia.1251', None))
print()
for _ in (-1, 0, 1):
    print(calendar.formatmonth(t[0], t[1] + _))

key_pressed('\nДля продолжения - нажмите Shift!', 'shift')
system('cls')
system(f'title Выводим календарь на текущий {t[0]} год!')
print(calendar.formatyear(t[0], 0, 0, 0, 4))

key_pressed('\nДля завершения - нажмите Shift!', 'shift')
