import curses
from Init_Screen import *


def draw_console(std_scr):
    screen = curses.initscr()
    height, width = std_scr.getmaxyx()
    curses.curs_set(0)

    for i in range(1, height - 20):
        fstr1 = f"This string gets printed at position ({i}, {i})"
        screen.addstr(i, i, fstr1)
        screen.addstr(i, width - len(fstr1) - i, fstr1)
        fstr2 = f"Стандартный Экран -> {width, height} Привет №{i}"
        screen.addstr(i + 10, i, fstr2)  # Python 3 required for unicode
        screen.addstr(i + 10, width - len(fstr2) - i, fstr2)
        fstr3 = f"☺{i}☻" * i
        screen.addstr(i + 20, i, fstr3)
        screen.addstr(i + 20, width - len(fstr3) - i, fstr3)
        screen.refresh()
        curses.napms(500)

    screen.getkey()
    curses.endwin()


init_screen()
curses.wrapper(draw_console)
