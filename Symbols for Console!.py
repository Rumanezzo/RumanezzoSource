from Init_Screen import *

width, height = init_screen()


def demo(symbol_list, width_):
    for symbol in symbol_list:
        print(symbol * width_)
    key_pressed('Нажмите enter для продолжения', 'enter')


s = (('⎵', '☻', '☺', 'ᛥ', 'ᛰ', 'ᚸ', 'ᛝ', 'ᛟ', '◊', '▧', '▨', '▩', '◌', '◇', '◈', 'ℵ', '⋇', '∃', '∀', '∞', '│', '∆'),
     ('⋅', '•', '●', '∘', '⊕', '⊗', '⊙', '⊚', '⊛', '⊝', '⍟', '→', '×', '☓', '╳', '▷', '◁', '⟶', '↯', '⊡', '⊞', '⊟'),
     ('☰', '☱', '☲', '☳', '☴', '☵', '☶', '☷', '⚀', '⚁', '⚂', '⚃', '⚄', '⚅', '★', '☆', '٭', '♠', '♤', '♥', '♡', '♣'),
     ('¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹', 'ⁿ', '⁰', '₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉'),
     ('ℚ', 'ℝ', 'ℤ', '⅓', '⅔', '⅕', '⅖', '⅗', '⅘', '⅙', '⅚', '⅛', '⅜', '⅝', '⅞'),
     ('Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ', 'Ⅹ', 'Ⅺ', 'Ⅻ', '½', '¾', '¼'),
     ('♦', '♢', '⠀', '⠁', '⠂', '⠃', '⠄', '⠅', '⠆', '≻', '△', '▽', '≺', '⊠', '♧'),
     ('░', '▒', '▓', '│', '┤', '╡', '╢', '╣', '║', '╔╗', '╚╝', '╓╖', '╙╜', '╒╕', '╘╛', '┐', '└', '┴', '┬', '├', '─'),
     ('┼', '╞', '╟', '╩', '╦', '╠', '═', '╬', '╧', '╨', '╤', '╥', '╫', '╪', '┘', '┌', '█', '▄', '▌', '▐', '▀', '∟'),
     ('“”', 'ƒ', '{}', '×', '«', '»', '¤', 'µ', '°', '‘’', '‰', '†', '‡', '…', '√', '±', 'Є', 'є', '⌂'))


cursor.hide()
for symbol_list_ in s:
    demo(symbol_list_, width)
    os.system('cls')