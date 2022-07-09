import curses as cur
import os


def set_mod(columns, lines):
    cmd = 'mode ' + str(columns) + ',' + str(lines)
    os.system(cmd)
    os.system('title Curses demo Text and Color')


def styles_output():
    # Change style: bold, highlighted, and underlined text
    screen.addstr("Regular text\n")
    screen.addstr("Bold text\n", cur.A_BOLD)
    screen.addstr("Highlighted text\n", cur.A_STANDOUT)
    screen.addstr("Underline text\n", cur.A_UNDERLINE)


screen = cur.initscr()
# Initialize color in a separate step
cur.start_color()
cur.curs_set(0)


# Create a custom color set that you might re-use frequently
# Assign it a number (1-255), a foreground, and background color.
cur.init_pair(1, cur.COLOR_RED, cur.COLOR_CYAN)
cur.init_pair(2, cur.COLOR_GREEN, cur.COLOR_BLUE)
cur.init_pair(3, cur.COLOR_YELLOW, cur.COLOR_WHITE)
cur.init_pair(4, cur.COLOR_BLACK, cur.COLOR_MAGENTA)
cur.init_pair(5, cur.COLOR_BLUE, cur.COLOR_GREEN)
cur.init_pair(21, cur.COLOR_CYAN, cur.COLOR_RED)
cur.init_pair(6, cur.COLOR_RED, cur.COLOR_CYAN)
cur.init_pair(7, cur.COLOR_WHITE, cur.COLOR_BLACK)
cur.init_pair(8, cur.COLOR_BLACK, cur.COLOR_WHITE)
cur.init_pair(9, cur.COLOR_MAGENTA, cur.COLOR_BLACK)
cur.init_pair(10, cur.COLOR_WHITE, cur.COLOR_YELLOW)
cur.init_pair(11, cur.COLOR_RED, cur.COLOR_BLACK)
cur.init_pair(12, cur.COLOR_GREEN, cur.COLOR_BLACK)
cur.init_pair(13, cur.COLOR_YELLOW, cur.COLOR_BLACK)
cur.init_pair(14, cur.COLOR_BLACK, cur.COLOR_MAGENTA)
cur.init_pair(15, cur.COLOR_BLUE, cur.COLOR_BLACK)
cur.init_pair(16, cur.COLOR_CYAN, cur.COLOR_BLACK)
cur.init_pair(17, cur.COLOR_RED, cur.COLOR_YELLOW)
cur.init_pair(18, cur.COLOR_WHITE, cur.COLOR_GREEN)
cur.init_pair(19, cur.COLOR_BLACK, cur.COLOR_RED)
cur.init_pair(20, cur.COLOR_MAGENTA, cur.COLOR_BLACK)
cur.init_pair(21, cur.COLOR_WHITE, cur.COLOR_BLUE)

try:
    set_mod(106, 32)
    styles_output()
    for i in range(1, 22):
        screen.addstr("Red Alert!\n", cur.color_pair(i))
    styles_output()
    screen.refresh()
    screen.getch()
except OSError:
    print('Вы пытаетесь запускать программу в IDE')
