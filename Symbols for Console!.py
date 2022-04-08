from Init_Screen import *

width, height = init_screen()


def demo(symbol_list, width_):
    for symbol in symbol_list:
        print(symbol * width_)
    key_pressed('Нажмите enter для продолжения', 'enter')


s = (('⎵', '☻', '☺', 'ᛥ', 'ᛰ', 'ᚸ', 'ᛝ', 'ᛟ', '◊', '▧', '▨', '▩', '◌', '◇', '◈', 'ℵ', '⋇', '∃', '∀', '∞', '│', '∆'),
     ('⋅', '•', '●', '∘', '⊕', '⊗', '⊙', '⊚', '⊛', '⊝', '⍟', '→', '×', '☓', '╳', '▷', '◁', '⟶', '↯', '⊡', '⊞', '⊟'),
     ('☰', '☱', '☲', '☳', '☴', '☵', '☶', '☷', '⚀', '⚁', '⚂', '⚃', '⚄', '⚅', '★', '☆', '٭', '♠', '♤', '♥', '♡', '♣'),
     ('¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹', 'ⁿ', '⁰', '₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉', '₊'),
     ('ℕ', 'ℚ', 'ℝ', 'ℤ', 'ℂ', '⅓', '⅔', '⅕', '⅖', '⅗', '⅘', '⅙', '⅚', '⅛', '⅜', '⅝', '⅞', '½', '¾', '¼', '♧', 'ℹ'),
     ('Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ', 'Ⅹ', 'Ⅺ', 'Ⅻ', '5⃝', '5⃞', '5⃠', '5⃟', '5⃣', '5⃢', '≠', '⊂', '⌘'),
     ('♦', '♢', '⠀', '⠁', '⠂', '⠃', '⠄', '⠅', '⠆', '≻', '△', '▽', '≺', '⊠', '∧', '∨', '∪', '∩', '∠', '∫', '∮', '≡'),
     ('░', '▒', '▓', '│', '┤', '╡', '╢', '╣', '║', '╔╗', '╚╝', '╓╖', '╙╜', '╒╕', '╘╛', '┐', '└', '┴', '┬', '├', '─'),
     ('┼', '╞', '╟', '╩', '╦', '╠', '═', '╬', '╧', '╨', '╤', '╥', '╫', '╪', '┘', '┌', '█', '▄', '▌', '▐', '▀', '∟'),
     ('“”', 'ƒ', '{}', '×', '«', '»', '¤', '°', '‘’', '‰', '†', '‡', '…', '√', '∛', '∜', '±', 'є', '⌂', 'χ', 'ψ', 'ω'),
     ('α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'ς', 'σ', 'τ', 'υ', 'φ'))


cursor.hide()
for symbol_list_ in s:
    demo(symbol_list_, width)
    os.system('cls')
