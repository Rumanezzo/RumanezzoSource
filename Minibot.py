name = input('Как тебя зовуть? ')
print(f'Очень рад с тобою познакомиться, {name}')
print('Давай пообщаемся...Если хочешь ответить "нет" - просто нажми на "ENTER"...')
age = input('Сколько тебе лет? -> ')
gender = input('Женщинка или Мужчинка? (введи "м" или "ж") -> ').lower()
gender0 = 'мужчинкой' if gender == 'м' else 'женщинкой'
gender_add1 = '*м' if gender == 'м' else 'ой'
gender_add2 = '*й' if gender == 'м' else 'ая'
fat = bool(input('Ты толст' + gender_add2 + '? -> '))
fat0 = 'толстеньк' if fat else 'худосочн'
beauty = bool(input('Ты красив' + gender_add2 + '? -> '))
beauty0 = 'симпатюлькой' if beauty else 'страшилкой'
print('Вот, что я узнал...')
print(f'Разговариваю я с {gender0} по имени {name}, {age}-летним {fat0}{gender_add1} {beauty0}')