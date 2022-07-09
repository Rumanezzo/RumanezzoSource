import curses
from Init_Screen import init_screen

init_screen()
screen = curses.initscr()

curses.curs_set(0)  # прячем курсор
screen.border(0)  # рисуем рамочку

y, x = screen.getmaxyx()
i = 0
while i < 100:
    txt1 = f"Смотри на Curses, Curses {i} раз(а) работают!"
    screen.addstr(y // 2, (x - len(txt1)) // 2, txt1)

    txt2 = f"{i}² по прежнему равно {i ** 2}!"
    screen.addstr(y // 2 + 1, (x - len(txt2)) // 2, txt2)
    curses.napms(30)
    i += 1
    screen.refresh()

screen.getch()
curses.endwin()
