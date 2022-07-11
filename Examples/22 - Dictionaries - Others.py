birthdays = {'Алиса': '1 Апр', 'Боб': '12 Дек', 'Марина': '26 Окт', 'Яна': '10 Мая'}
print('Я знаю дни рождения следующих персоналий:')
print(', '.join(birthdays.keys()))
while True:
    name = input('Введите Имя, необязательно из списка или просто Enter, чтобы выйти -> ')

    if name == '':
        break

    if name in birthdays:
        print(name + ' родился (родилась) ' + birthdays[name])
    else:
        print('У меня нет информации о дне рождения ' + name)
        birthday = input(f'Введите день рождения для {name} в формате 31 янв -> ')

        birthdays[name] = birthday
        print('База дней рождений было обновлена!')
        print('Теперь мы знаем информацию о:')
        print(', '.join(birthdays.keys()))

input('Работа закончена - нажмите Enter!')
