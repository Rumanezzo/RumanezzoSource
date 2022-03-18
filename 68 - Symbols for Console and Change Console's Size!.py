# Не запускать в IDE!!!
import os


def demo(s, width):
    for i in s:
        print(i * (width - 1))
    input('•••• Нажмите Enter для завершения ••••')
    os.system('cls')


def set_mod(columns, lines):
    cmd = 'mode ' + str(columns) + ',' + str(lines)
    os.system(cmd)
    print(f'Размеры экрана -> {cmd}')


s0 = ['⎵', '☻', '☺', 'ᛥ', 'ᛰ', 'ᚸ', 'ᛝ', 'ᛟ', '◊', '▧', '▨', '▩', '◌', '◇', '◈', 'ℵ', '⋇', '∃', '∀', '∞', '|', '∆', '≺']
s1 = ['⋅', '•', '●', '∘', '⊕', '⊗', '⊙', '⊚', '⊛', '⊝', '⍟', '→', '×', '☓', '╳', '▷', '◁', '⟶', '↯', '⊡', '⊞', '⊟', '⊠']
s2 = ['☰', '☱', '☲', '☳', '☴', '☵', '☶', '☷', '⚀', '⚁', '⚂', '⚃', '⚄', '⚅', '★', '☆', '٭', '♠', '♤', '♥', '♡', '♣', '♧']
s3 = ['¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹', 'ⁿ', '⁰', '₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉', '₏']
s4 = ['ℼ', 'ℚ', 'ℝ', 'ℤ', '⅀', 'ⅇ', 'ⅈ', 'ⅉ', '⅓', '⅔', '⅕', '⅖', '⅗', '⅘', '⅙', '⅚', '⅛', '⅜', '⅝', '⅞', 'ₖ', 'ₛ', 'ₜ']
s5 = ['Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ', 'Ⅹ', 'Ⅺ', 'Ⅻ', '½', '¾', '¼']
s6 = ['♦', '♢', '⠀', '⠁', '⠂', '⠃', '⠄', '⠅', '⠆', '≻', '△', '▽']

x0, y0 = os.get_terminal_size()
set_mod(x0, y0)

print(f'Ширина (Columns) - {x0}; Высота (Lines) - {y0}')

x1, y1 = map(int, input('Меняем размер окна на Ваш ☻: [ширина]⎵[высота] ⟶ ').split() or (106, 32))

set_mod(x1, y1)

ans = input('А теперь можно вернуть как было (1)... Или оставить как есть? (0) ⟶ ')

if ans == '1':
    x1, y1 = x0, y0
    set_mod(x0, y0)

demo(s1, x1)
demo(s2, x1)
