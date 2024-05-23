from easygui import msgbox, choicebox, enterbox
import sys

# A nice welcome message
name = enterbox(title='Вводим имя...', msg='Как тебя зовут?')
if name is None:
    sys.exit()
ret_val = msgbox(f"Приветик, {name}, мы сейчас будем выбирать мороженное\nПриготовься!!",
                 title='Демонстрируем возможности EasyGUI')
if ret_val is None:  # User closed msgbox
    sys.exit(0)

msg = "Какой Твой любимый вкус мороженного?\nИли нажми на кнопочку <cancel> для выхода."
title = "Выбор Мороженного"
choices = ["Ванильное", "Шоколадное", "Крем-брюле", "Каменистая дорога"]
while True:
    choice = choicebox(msg, title, choices)
    if choice is None:
        sys.exit(0)
    msgbox(f"Ты выбрал: {choice}\nНаверно это очень вкусно!", "Результат Твоего выбора")
