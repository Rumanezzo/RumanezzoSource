from Init_Screen import hide, key_pressed, system

# Произвольное число позиционных параметров

hide()
continue_str = 'Для продолжения нажмите Shift!'


def print_them_all_v1(*args):
    print('Запускаем версию "print_them_all_v1"')
    print('Тип args', type(args))
    print(args)
    for i, args in enumerate(args):
        print(f'{i}-ый позиционный параметр -⟶', args)


print_them_all_v1(2, 'привет', 5.6, (5, 'Вася'), 455)

# Распаковка
my_favorite_pets = ['lion', 'elephant', 'monkey', 'cat', 'horse']
print_them_all_v1(my_favorite_pets)  # Здесь специально забыли поставить *
print_them_all_v1(*my_favorite_pets)
key_pressed(continue_str, 'shift')
system('cls')


def print_them_all_v2(**kwargs):
    print('Запускаем версию "print_them_all_v2"')
    print('Тип args', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(f'Позиционный параметр: {key} -⟶', value)


print_them_all_v2(name='Вася', address='Moscow', age=25, home=42)
my_friend = {'name': 'Вася', 'address': 'Moscow', 'age': 25, 'home': 42}

# Распаковка
print_them_all_v2(**my_friend)
key_pressed(continue_str, 'shift')
system('cls')


def print_them_all_v3(*args, **kwargs):
    print('Запускаем версию "print_them_all_v3"')
    print('тип args:', type(args))
    print(args)
    for i, args in enumerate(args):
        print(f'{i}-ый позиционный параметр -⟶', args)
    print('Тип kwargs', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(f'Позиционный параметр: {key} -⟶', value)


print('Позиционные аргументы:')
print_them_all_v3('Вася', 'Moscow', 25)
print('Именованные аргументы:')
print_them_all_v3(name='Петя', address='Paris', home=82)
print('Оба типа аргументов - позиционные и именованные (именно в таком порядке!):')
print_them_all_v3('Вася', 'Moscow', 25, name='Петя', address='Paris', home=82)
key_pressed(continue_str, 'shift')
system('cls')


def print_them_all_v4(a, b=5, *args, **kwargs):
    print('Запускаем версию "print_them_all_v4"')
    print('a и b - фиксированный ввод -⟶', a, b)
    print('тип args:', type(args))
    print(args)
    for i, args in enumerate(args):
        print(f'{i}-ый позиционный параметр -⟶', args)
    print('Тип kwargs', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(f'Позиционный параметр: {key} -⟶', value)


print_them_all_v4(15121968, 31415926, 'Вася', 'Moscow', 25)
print_them_all_v4(5, b=10, name='Петя', address='Paris', home=82)
print_them_all_v4(5, name='Петя', address='Paris', home=82)
key_pressed('Для завершения нажмите Enter!', 'enter')
