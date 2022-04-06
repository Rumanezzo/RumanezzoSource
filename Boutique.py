# Не запускать в IDE!
import curses
from Init_Screen import *


def main_loop(std_scr):
    key = 0

    # Очистка и обновление экрана, сокрытие курсора
    std_scr.clear()
    std_scr.refresh()
    curses.curs_set(0)

    # Инициализируем цветовые пары для модуля curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_RED)
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_GREEN)
    curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Основной цикл
    while key != curses.KEY_F1:  # 265 - код клавиши F1, 27 - код клавиши ESC

        # Инициализация
        std_scr.clear()
        height, width = std_scr.getmaxyx()

        # Строки с текстом - подготовка
        title = "Модный Магазин - модель Теории Массового обслуживания"[:width - 1]
        subtitle = "по мотивам программы из книги Коснёвски"[:width - 1]

        key_str = f"Код нажатой клавиши: {key}"
        status_bar_str = f"Нажмите F1 для выхода! | ♦Игровая Модель - Модный Магазин♦ | Нажата клавиша с кодом {key}"
        status_bar_str = status_bar_str.center(width - 1, ' ')

        if key == 0:
            key_str = "Пока ничего не нажато..."[:width - 1]

        # Вычисления по центровке текста
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_key_str = int((width // 2) - (len(key_str) // 2) - len(key_str) % 2)
        start_y = int((height // 2) - 2)

        # Выводим текст сверху
        param_str = f"Ширина: {width}, Высота: {height} - вывели размеры экрана, определенным цветом, да еще и по " \
                    f"центру!".center(width, ' ')
        std_scr.addstr(1, 0, param_str, curses.color_pair(1))

        # Выводим статусную строку
        std_scr.attron(curses.color_pair(3))
        std_scr.addstr(height - 1, (width - len(status_bar_str)) // 2, status_bar_str)
        std_scr.attroff(curses.color_pair(3))

        # Активируем атрибуты заголовка
        std_scr.attron(curses.color_pair(2))
        std_scr.attron(curses.A_BOLD)

        # Выводим заголовок
        std_scr.addstr(start_y, start_x_title, title)

        # Деактивируем атрибуты заголовка
        std_scr.attroff(curses.color_pair(2))
        std_scr.attroff(curses.A_BOLD)

        # Распечатываем на экране подготовленный текст
        std_scr.attron(curses.color_pair(6))
        std_scr.attron(curses.A_BOLD)
        std_scr.addstr(start_y + 1, start_x_subtitle, subtitle)
        std_scr.attroff(curses.color_pair(6))
        std_scr.attroff(curses.A_BOLD)

        std_scr.addstr(start_y + 5, start_x_key_str, key_str)

        # Обновление экрана
        std_scr.refresh()

        # Ждем нажатия на клавишу
        key = std_scr.getch()


def main():
    init_screen()
    curses.wrapper(main_loop)


if __name__ == "__main__":
    main()
