#  Очень короткая функция с использованием тернарного оператора if внутри f-строки
def percentage_changed(old, new):
    old, new = int(old), int(new)
    return f"{'рост' if new > old else 'падение'} на {abs(old - new) / old:.0%}"


old0 = input('Вводи старый ценник (целое число!!!) -> ')
new0 = input('Вводи новый ценник -> ')
res = percentage_changed(old0, new0)

print(res)
