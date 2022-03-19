import os

import cursor
from colorama import init
from termcolor import colored

init()
cursor.hide()

width = 5  # Ширина Символа
height = 7  # Высота Символа


def set_mod(columns, lines):
    cmd = 'mode ' + str(columns) + ',' + str(lines)
    os.system(cmd)


def screen_init():
    x_, y_ = os.get_terminal_size()
    set_mod(x_, y_)
    return x_, y_


def str_kill(n):
    print('\n' * n)


font1 = '''Модифицированный шрифт для выборки по буквам 1 кусок
⋅⋅●●●●●●●⋅●●●⋅⋅●●●●⋅●●●●⋅⋅⋅●⋅⋅⋅●●●⋅●⋅⋅⋅●●⋅⋅●●⋅⋅●●●●⋅⋅⋅●●⋅⋅⋅●⋅●●●⋅●●●●●●●●●⋅⋅●●●⋅●●●●●●●⋅⋅●●⋅●⋅●⋅●●●⋅●⋅⋅●⋅●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅●
⋅●⋅⋅●●⋅⋅⋅⋅●⋅⋅●⋅●⋅⋅⋅●●⋅⋅⋅●⋅●⋅●⋅●⋅⋅⋅●●⋅⋅⋅●●⋅⋅●⋅⋅●⋅⋅●●●⋅●●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅●●⋅●⋅●⋅●⋅⋅●●⋅●⋅●●⋅●⋅●●⋅⋅●⋅⋅●⋅⋅●●⋅⋅⋅●●⋅⋅⋅●
●⋅⋅⋅●●⋅⋅⋅⋅●⋅⋅●⋅●⋅⋅⋅⋅●⋅⋅⋅⋅⋅●⋅●⋅⋅⋅⋅⋅●●⋅⋅⋅●●⋅●⋅⋅●⋅⋅⋅●●⋅●⋅●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅⋅⋅⋅●⋅⋅⋅●⋅⋅●⋅●●●⋅●⋅●⋅●●⋅⋅●⋅●⋅⋅⋅●⋅●⋅●⋅●⋅●⋅●
●⋅⋅⋅●●●●●⋅●●●●⋅●⋅⋅⋅⋅●●●⋅⋅⋅●⋅●⋅⋅⋅●●⋅●⋅⋅●●●●⋅⋅⋅●⋅⋅⋅●●⋅⋅⋅●●●●●●●⋅⋅⋅●●⋅⋅⋅●●●●●⋅●⋅⋅⋅⋅⋅⋅●⋅⋅⋅⋅●●●⋅⋅●⋅⋅⋅●●●⋅●⋅⋅●⋅⋅●●●●⋅⋅●⋅⋅●⋅●⋅●
●●●●●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅⋅●⋅⋅⋅⋅⋅●⋅●⋅⋅⋅⋅⋅●●⋅●⋅●●⋅●⋅⋅●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅⋅●⋅⋅⋅⋅⋅⋅●⋅⋅⋅⋅⋅⋅●⋅●●●⋅⋅⋅●⋅⋅●⋅⋅●⋅⋅⋅⋅⋅●⋅●⋅●⋅●⋅●⋅●
●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅⋅●⋅⋅⋅●●●●●●●⋅⋅⋅●●●⋅⋅●●⋅⋅●⋅⋅●⋅⋅●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅⋅●⋅⋅⋅●⋅⋅●⋅⋅●⋅⋅⋅●●⋅●⋅●⋅⋅●⋅⋅●●●●●⋅⋅⋅⋅●●⋅⋅⋅●●⋅●⋅●
●⋅⋅⋅●●●●●⋅●●●●●●⋅⋅⋅⋅●●●●●●⋅⋅⋅●●●●●●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅●●⋅⋅⋅●⋅●●●⋅●⋅⋅⋅●●⋅⋅⋅⋅⋅●●●⋅⋅⋅●⋅⋅⋅●●●⋅●⋅●⋅●⋅⋅●⋅⋅⋅⋅⋅⋅●⋅⋅⋅⋅●●⋅⋅⋅●●●●●●
'''

font2 = '''Модифицированный шрифт для выборки по буквам 2 кусок
⋅●●●⋅⋅●●●●●⋅⋅●⋅●⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅●●●⋅⋅●●●⋅●⋅⋅⋅●⋅⋅⋅⋅⋅
●⋅⋅⋅●●⋅⋅⋅●●⋅●⋅●●⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅●●●⋅●⋅⋅⋅●●⋅⋅⋅●⋅⋅⋅⋅⋅
⋅⋅⋅⋅●●⋅⋅⋅●●⋅●⋅●●⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅●●●⋅●⋅⋅⋅●●⋅⋅⋅●⋅⋅⋅⋅⋅
⋅⋅●●●⋅●●●●●●●⋅●●●●●⋅⋅●●●⋅⋅⋅●⋅⋅⋅●●●⋅●●⋅⋅●⋅⋅⋅⋅⋅
⋅⋅⋅⋅●⋅⋅⋅●●●⋅●⋅●●⋅⋅⋅●⋅⋅⋅⋅⋅⋅⋅⋅⋅⋅●⋅⋅⋅●●⋅●⋅●⋅⋅⋅⋅⋅
●⋅⋅⋅●⋅⋅●⋅●●⋅●⋅●●⋅⋅⋅●⋅⋅⋅⋅⋅⋅●●●⋅●⋅⋅⋅●●⋅●⋅●⋅⋅⋅⋅⋅
⋅●●●⋅●●⋅⋅●●⋅⋅●⋅⋅●●●⋅⋅⋅⋅⋅⋅⋅●●●⋅⋅●●●⋅●●●⋅●⋅⋅⋅⋅⋅
'''

# try:
#     fi = open('29 - Big Letters Alphabet.txt', 'r')
# except FileNotFoundError:
#     fi = open('29 - Big Letters Alphabet.txt', 'w')
# fi.close()

letter_strings1 = font1.split('\n')
letter_strings2 = font2.split('\n')
letter_strings = []
pair_letter_strings = list(zip(letter_strings1, letter_strings2))
for word in pair_letter_strings:
    letter_strings.append(word[0] + word[1])

_ = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'е': 5, 'д': 6, 'з': 7, 'и': 8, 'к': 9, 'л': 10, 'м': 11, 'н': 12, 'о': 13,
     'п': 14, 'р': 15, 'с': 16, 'т': 17, 'у': 18, 'ж': 19, 'ф': 20, 'ц': 21, 'ч': 22, 'х': 23, 'ш': 24, 'э': 25,
     'я': 26, 'ю': 27, 'ь': 28, '-': 29, '!': 30, '8': 31, 'ы': 32, ' ': 33}


def str_out(code_, color_, x_):
    res = len(code_) * ['']
    for i_ in range(1, len(letter_strings)):
        for j_ in range(len(code_)):
            res[j_] = letter_strings[i_][(code_[j_] - 1) * width:(code_[j_]) * width] + ' '

        res_lst = ''.join(res)
        print(colored(res_lst.center(x_ - 1), color_))


def txt_str_to_dict_str(txt_str):
    if len(txt_str) > 18:
        txt_str = txt_str[0:18]

    str_code_ = [int] * len(txt_str)
    i_ = 0
    for char in txt_str:
        str_code_[i_] = _[char]
        i_ += 1
    return str_code_


try:
    x0, y0 = screen_init()
except OSError:
    print('Похоже вы запускаете скрипт в IDE, а это нехорошо...')
    x0, y0 = 106, 32

txt = ('прорвемся!', 'ведь у нас нет', 'другого выхода!')
color = ('green', 'red', 'yellow')

for i in range(len(txt)):
    code = txt_str_to_dict_str(txt[i])
    str_kill(2)
    str_out(code, color[i], x0)

input()
