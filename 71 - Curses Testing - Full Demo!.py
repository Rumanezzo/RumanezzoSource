import curses
import os


def set_mod(columns, lines):
    cmd = 'mode ' + str(columns) + ',' + str(lines)
    os.system(cmd)


def draw_menu(std_scr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    std_scr.clear()
    std_scr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_MAGENTA, curses.COLOR_RED)
    curses.init_pair(5, curses.COLOR_BLUE, curses.COLOR_GREEN)
    curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # Loop where k is the last character pressed
    while k != curses.KEY_F1:  # 265 - код клавиши F1

        # Initialization
        std_scr.clear()
        height, width = std_scr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width - 1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height - 2, cursor_y)

        # Declaration of strings
        title = "Пример использования модуля Curses"[:width - 1]
        subtitle = "Программа написана Clay McLeod"[:width - 1]

        key_str = f"Код нажатой клавиши: {k}"
        status_bar_str = f"Нажмите F1 для выхода! | ♦Это настоящая статусная строка♦ | Позиция курсора:\
         x = {cursor_x}, y = {cursor_y}"
        status_bar_str = status_bar_str.center(width - 1, ' ')

        if k == 0:
            key_str = "Пока ничего не нажато..."[:width - 1]

        # Centering calculations
        start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_subtitle = int((width // 2) - (len(subtitle) // 2) - len(subtitle) % 2)
        start_x_key_str = int((width // 2) - (len(key_str) // 2) - len(key_str) % 2)
        start_y = int((height // 2) - 2)

        # Rendering some text
        param_str = f"Ширина: {width}, Высота: {height} - вывели размеры экрана, определенным цветом, да еще и по " \
                    f"центру!".center(width, ' ')
        for _ in range(1, 7):
            std_scr.addstr(_, 0, param_str, curses.color_pair(_))

        # Render status bar
        std_scr.attron(curses.color_pair(3))
        std_scr.addstr(height - 1, (width - len(status_bar_str)) // 2, status_bar_str)
        # std_scr.add_str(height - 1, len(status_bar_str), " " * (width - len(status_bar_str) - 1))
        std_scr.attroff(curses.color_pair(3))

        # Turning on attributes for title
        std_scr.attron(curses.color_pair(2))
        std_scr.attron(curses.A_BOLD)

        # Rendering title
        std_scr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        std_scr.attroff(curses.color_pair(2))
        std_scr.attroff(curses.A_BOLD)

        # Print rest of text
        std_scr.attron(curses.color_pair(6))
        std_scr.attron(curses.A_BOLD)
        std_scr.addstr(start_y + 1, start_x_subtitle, subtitle)
        std_scr.attroff(curses.color_pair(6))
        std_scr.attroff(curses.A_BOLD)
        str_decor = '⋅' * 4 + '٭' * 4 + '×' * 3 + '☆' * 6 + '☓' * 4 + '╳'
        str_decor += str_decor[::-1]
        std_scr.addstr(start_y + 3, (width // 2) - len(str_decor) // 2, str_decor)
        std_scr.addstr(start_y + 5, start_x_key_str, key_str)
        std_scr.move(cursor_y, cursor_x)

        # Refresh the screen
        std_scr.refresh()

        # Wait for next input
        k = std_scr.getch()


def main():
    set_mod(106, 32)
    curses.wrapper(draw_menu)


if __name__ == "__main__":
    main()
