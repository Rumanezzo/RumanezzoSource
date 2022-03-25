import curses

scr = curses.initscr()

curses.curs_set(0)  # прячем курсор
scr.border(0)  # рисуем рамочку

y, x = scr.getmaxyx()

for i in range(1, 1000):
    txt1 = f"Смотри на Curses, Curses {i} раз(а) работают!"
    scr.addstr(y // 2, (x - len(txt1)) // 2, txt1)

    txt2 = f"Ведь точно Работают Curses №{i}!"
    scr.addstr(y // 2 + 1, (x - len(txt2)) // 2, txt2)
    curses.napms(15)
    scr.refresh()

scr.getch()
curses.endwin()
