from random import randint
from os import system
from time import sleep


class Player:
    hp = 10  # Текущее Здоровье
    max_hp = 10  # Максимальное Здоровье
    pw = 2  # Сила
    level = 0
    money = 100
    sp = 5  # очки навыков
    xp = 0  # Текущий опыт
    max_xp = 10  # Граница уровня
    heal_pw = 5  # Сила Лечения
    n_heal = 5  # Число Лечащих Зарядов
    status = 0  # Текущий статус игрока: 0 - играем, -1 - проиграли, 1 - сбежал
    name = ''

    def __init__(self):
        system('cls')
        self.name = input('Как Вас величать? -> ') or 'Михрютка'
        print(f'Очень приятно, {self.name}, начнем нашу мини-ролевую игру!')
        system('pause')


def menu_upgrade(player):
    system('cls')
    while player.sp > 0:
        print(f"{player.name}! У Вас свободных очков навыков -> {player.sp}")
        print("Вы можете:")
        print(f"1. Увеличить Максимум Здоровья (HP) +5 за 1 очко навыков, сейчас у Вас: {player.hp} из {player.max_hp}")
        print(f"2. Увеличить Силу (PW) +1 за 1 очко навыков, сейчас у Вас: {player.pw}")
        print(f"3. Увеличить Силу Лечения (PH) +1 за 1 очко навыков, сейчас у Вас: +{player.heal_pw}")
        n, m = map(int, input("Нажмите 1 пробел 2, чтобы потратить 2 очка на Здоровье -> ").split(' '))
        if n == 1:
            player.hp += 5 * m
            player.max_hp += 5 * m
        elif n == 2:
            player.pw += m
        elif n == 3:
            player.heal_pw += m
        player.sp -= m
        system('cls')


def menu_main(player):
    while True:
        if player.status == -1:
            if randint(1, 10) == 7:
                print('Вы чудесным образом спаслись от смерти, в результате Ваш Максимум Здоровья вырос на 5 ед.')
                player.max_hp += 5
            else:
                print(f'{player.name}, Вы проиграли...')
                exit()
        print("Ваши действия:")
        print("1. Идти сражаться")
        print("2. Проверить характеристики")
        print("3. Свалить на Хрен!")
        n = input("Что выбираем: ")
        if n == "1":
            menu_fight(player)
        elif n == "2":
            menu_stats(player)
        elif n == "3":
            print('Было приятно поработать немного вместе! Пока!')
            system('pause')
            exit()


def menu_stats(player):
    system('cls')
    print(f"{player.name}! Ниже приведены Ваши Характеристики:")
    print("У Вас сейчас:")
    print(f"Уровень (LV): {player.level}")
    print(f'Сбережения (GP): {player.money}')
    print(f'Заработано очков опыта (XP): {player.xp}')
    print(f"Нераспределенных очков навыков (SP): {player.sp}")
    print(f"Здоровье (HP): {player.hp} из {player.max_hp}")
    print(f"Сила (PW): {player.pw}")
    print(f"Сила Лечения (PH): +{player.heal_pw} ед. здоровья")
    print(f'Количество Зарядов Лечения (PO): {player.n_heal} шт.')

    system('pause')
    system('cls')


def enemy():
    hp = 5 * randint(1, 5)
    power = 2 * randint(1, 2)
    return hp, power


def attack(player: Player, enemy_hp, enemy_power):
    r = randint(0, 3)
    if r == 1 or r == 0:
        enemy_hp -= (player.pw + player.pw * r)
        print("Вы наносите урон врагу!")
    else:
        player.hp -= (enemy_power + enemy_power * (r - 2))
        print("Враг наносит урон Вам...")
        if player.hp < 0:
            print("Вы проиграли!...Но, возможно, ещё не всё потеряно...")
            player.status = -1
    return enemy_hp


def healing(player: Player):
    if player.n_heal:
        player.n_heal -= 1
        player.hp += player.heal_pw
        print(f"Лечимся...на {player.heal_pw} ед.")
        sleep(2)
        print(f'В итоге {player.name} имеет {player.hp} ед. здоровья')
    else:
        print('Нечем лечиться...')

    if player.hp > player.max_hp:
        player.hp = player.max_hp


def battle_stage(player: Player, enemy_hp, enemy_power):
    system('cls')
    print(f"Враг: Здоровье -> {enemy_hp} Сила -> {enemy_power}")
    print(f"{player.name}: Здоровье -> {player.hp} Сила -> {player.pw}")
    print()
    print(f"1. Бьём с силой -> {player.pw}")
    print(f"2. Лечимся -> +{player.heal_pw} ед. здоровья")
    print("3. Убегаем!")
    answer = input("Ваш выбор: ")

    if answer == "1":
        enemy_hp = attack(player, enemy_hp, enemy_power)
    elif answer == "2":
        healing(player)
    elif answer == "3":
        if randint(1, 3) == 3:
            print("Удалось сбежать!")
            player.status = 2
        else:
            print("Сбежать не удалось...")
            player.hp -= 5
            sleep(2)
    return enemy_hp


def menu_fight(player):
    enemy_hp0, enemy_power0 = enemy()

    while enemy_hp0 > 0 and player.hp > 0 and player.status != 2:
        enemy_hp0 = battle_stage(player, enemy_hp0, enemy_power0)
        system('pause')
        system('cls')

    if player.hp > 0:
        player.xp += randint(4, 6)
        print(f'Этот бой Вы выиграли! Всего заработано очков опыта -> ({player.xp})')
        add = randint(5, 25)
        player.money += add
        print(f'На теле врага Вы нашли золотые монеты: {add} шт.')
    else:
        player.status = -1
        return

    if player.xp >= player.max_xp:
        player.xp = 0
        player.max_xp *= 2
        player.level += 1
        player.sp += 5
        menu_upgrade(player)


player0 = Player()
menu_upgrade(player0)
menu_main(player0)
