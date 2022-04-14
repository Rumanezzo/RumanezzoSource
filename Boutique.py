# Не запускать в IDE!
import curses
from math import log
from random import random

from Init_Screen import *


def game(std_scr):
    screen = curses.initscr()
    height, width = std_scr.getmaxyx()

    # Очистка и обновление экрана, сокрытие курсора
    screen.clear()
    screen.refresh()
    curses.curs_set(0)

    # Инициализируем цветовые пары для модуля curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_RED)
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_GREEN)
    curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Строки с текстом - подготовка
    title = "Модный Магазин - модель Теории Массового обслуживания"[:width - 1]
    subtitle = "по мотивам программы из книги Коснёвски"[:width - 1]

    status_bar_str = f"│Нажми клавишу для продолжения! │◊◊◊Игровая Модель - Модный Магазин◊◊◊│ Резервное место        │"
    status_bar_str = status_bar_str.center(width - 1, ' ')

    # Вычисления по центровке текста
    start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
    start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
    start_y = int((height // 2) - 2)

    # Выводим статусную строку
    screen.attron(curses.color_pair(3))
    screen.addstr(height - 1, (width - len(status_bar_str)) // 2, status_bar_str)
    screen.attroff(curses.color_pair(3))

    # Активируем атрибуты заголовка
    screen.attron(curses.color_pair(2))
    screen.attron(curses.A_BOLD)

    # Выводим заголовок
    screen.addstr(start_y, start_x_title, title)

    # Деактивируем атрибуты заголовка
    screen.attroff(curses.color_pair(2))
    screen.attroff(curses.A_BOLD)

    # Распечатываем на экране подготовленный текст
    screen.attron(curses.color_pair(6))
    screen.attron(curses.A_BOLD)
    screen.addstr(start_y + 1, start_x_subtitle, subtitle)
    screen.attroff(curses.color_pair(6))
    screen.attroff(curses.A_BOLD)

    # Обновление экрана
    screen.refresh()

    # Ждем нажатия на клавишу
    screen.getch()

    # Начальная установка - начало дня - начало текста оригинальной игры "Модный Магазин"
    employee_work = []
    profit_week = [0, 0, 0, 0, 0, 0]  # Прибыль по дням
    client_arrive_speed = 0.1  # Скорость поступления клиентов
    client_service_speed = 0.15  # Скорость обслуживания клиентов

    profit_total = 0  # Прибыль за неделю, накопленная
    queue = 0  # Длина очереди
    current_time = 0  # Время в минутах
    lost_clients = 0

    def client_arriving_moment():
        """Вычисляем момент появления следующего клиента"""
        nonlocal current_time, time_arriving, queue, max_queue, lost_clients, client_arrive_speed

        queue += 1
        time_arriving = current_time - log(random() / client_arrive_speed)

        if queue < max_queue:
            return

        queue = max_queue
        lost_clients += 1
        screen.addstr(height - 2, 5, f'Длинная очередь... {lost_clients}-й клиент потерян!')

        client_arrive_speed = 0.1 + (client_arrive_speed - 0.1) * 0.9
    for day in range(3):
        total_revenue = 0  # Общая выручка за день
        working_time = 6  # Длина рабочего дня
        lost_clients = 0  # Потерянные за день клиенты
        client_arrive_speed = 0.1  # Скорость поступления клиентов
        time_arriving = 0  # Время прибытия следующего клиента
        current_time = 0  # Время в минутах

        screen.clear()
        screen.addstr(1, 5, 'Модный Магазин')
        screen.addstr(2, 5, f'День {day + 1}-й')
        screen.addstr(3, 5, f'Базовая скорость поступления клиентов = {int(600 * client_arrive_speed / 10)} чел. в час')
        screen.addstr(4, 5, f'100$ на рекламу? Нажмите Y⃣- да или N⃣- нет')
        key = screen.getkey()

        advert = 0

        if key == 'y' or key == 'Y':
            client_arrive_speed += 0.1
            advert = 1

        screen.addstr(6, 5, f'Новая скорость поступления = {int(600 * client_arrive_speed / 10)} чел. в час')
        discount = 1
        screen.addstr(7, 5, f'Скидка 10%? Нажмите Y⃣- да или N⃣- нет')
        key = screen.getkey()

        if key == 'y' or key == 'Y':
            discount = 0.9
            client_arrive_speed += 0.1

        screen.addstr(6, 5, f'Новая скорость поступления = {int(600 * client_arrive_speed / 10)} чел. в час')

        screen.addstr(9, 5, 'Скорость обслуживания - 9 чел. в час')
        screen.addstr(10, 5, 'Число продавцов по 200$? 1 - 9')
        key = screen.getkey()
        screen.addstr(11, 5, f'Нанятых продавцов - {key} чел.')

        employees = int(key)
        max_queue = 2 + employees // 4
        screen.addstr(13, 5, f'Максимальная длина очереди - {max_queue}')
        for _ in range(employees):
            employee_work.append(0)

        screen.addstr(height - 2, 5, 'Для продолжения нажмите на любую клавишу')
        screen.getch()

        # События за день
        screen.clear()

        screen.addstr(1, 5, 'Модный магазин')
        screen.addstr(2, 5, f'День {day + 1}. Открыто 10.00-{10 + working_time}.00')
        screen.addstr(3, 5, f'Продавцов: {employees}')

        client_arriving_moment()

        #  Моделирование с шагом в 1 минуту
        for current_time in range(working_time * 60):
            if current_time > time_arriving:
                client_arriving_moment()
            busy_employees = 0
            for _ in range(employees):
                if (queue > 0) and (employee_work[_] <= current_time):
                    queue -= 1
                    service_time = log(random()) // client_service_speed
                    employee_work[_] = current_time - service_time
                    total_revenue -= int(service_time * (1 + random()) * discount)
                if employee_work[_] > time_arriving:
                    busy_employees += 1

            screen.addstr(4, 5, f'Время: {1000 + current_time + 40 * int(current_time / 60)}')
            screen.addstr(5, 5, f'Скорость поступления: {int(600 * client_arrive_speed) / 10}')
            screen.addstr(6, 5, f'Ждущих клиентов: {queue}')
            screen.addstr(7, 5, f'Обслуживающих продавцов: {busy_employees}')
            screen.addstr(9, 5, f'Потеряно клиентов: {lost_clients}')
            screen.addstr(11, 5, f'Выручка: {total_revenue}')
            curses.napms(100)
            screen.refresh()

        profit_week[day] = int(total_revenue - 200 * employees - 100 * advert + 0.5)
        profit_total += profit_week[day]
        lost_clients += lost_clients + queue
        employee_work.clear()

        screen.clear()
        screen.addstr(1, 5, 'Модный Магазин')
        screen.addstr(3, 5, f'Итог за {day + 1}-й день')
        screen.addstr(5, 5, f'Скорость поступления: {int(600 * client_arrive_speed) / 10}')
        screen.addstr(7, 5, f'Скорость обслуживания - 9 клиентов в час')
        screen.addstr(9, 5, f'Продавцов: {employees}')
        screen.addstr(11, 5, f'Потеряно клиентов: {lost_clients}')
        screen.addstr(12, 5, f'Выручка: {total_revenue}')
        screen.addstr(14, 5, f'Прибыль: {profit_week[day]}')
        screen.addstr(height - 2, 5, 'Для продолжения нажмите любую клавишу')
        screen.getch()

    screen.clear()
    screen.addstr(1, 5, 'Модный Магазин')
    screen.addstr(3, 5, 'Итог за неделю')
    screen.addstr(5, 5, 'День   Прибыль')
    for i in range(6):
        screen.addstr(2 * i + 7, 5, f'   {i + 1}    {profit_week[i]}')
    screen.addstr(19, 5, f'Итого: {profit_total}')

    screen.addstr(height - 2, 5, 'Для продолжения нажмите любую клавишу')
    screen.getch()


def main():
    init_screen()
    curses.wrapper(game)


if __name__ == "__main__":
    main()
