from random import randint
from os import system


class Player:
    hp = 10  # Текущее Здоровье
    max_hp = 10  # Максимальное Здоровье
    pw = 2  # Сила
    level = 0
    sp = 5  # очки навыка
    xp = 0  # Текущий опыт
    max_xp = 100  # Граница уровня
    heal_hp = 5  # Запас лечения
    status = 0  # Текущий статус игрока: 0 - играем, -1 - проиграли, 1 - выиграли


def menu_upgrade(player):
    system('cls')
    while player.sp > 0:
        print(f"Выберите что необходимо повысить, у Вас всего очков навыков -> {player.sp}")
        print()
        print(f"1. Увеличить Здоровье (HP) +5 за 1 очко навыков {player.hp} из {player.max_hp}")
        print(f"2. Увеличить Силу (PW) +1 за 1 очко навыков {player.pw}")
        print(f"3. Увеличить силу лечения + 1HP за 1 очко навыков: {player.heal_hp}")
        n = input("Сделай выбор -> ")
        if n == "1":
            player.hp += 5
            player.max_hp += 5
        elif n == "2":
            player.pw += 1
        elif n == "3":
            player.heal_hp += 1
        player.sp -= 1
        system('cls')


def menu_simple(player):
    while True:
        if player.status == -1:
            print('Вы проиграли...')
            exit()
        print("Ваши действия:")
        print("1. Идти сражаться")
        print("2. Проверить характеристики")
        n = input("Что выбираем: ")
        if n == "1":
            menu_fight(player)
        if n == "2":
            menu_stats(player)


def menu_stats(player):
    system('cls')
    print("Характеристики Игрока:")
    print("У Вас сейчас:")
    print(f"Уровень (LV) {player.level}")
    print(f"Нераспределенных очков навыков (SP) {player.sp}")
    print(f"Здоровье (HP) -> {player.hp} из {player.max_hp}")
    print(f"Сила (PW) {player.pw}")
    print(f"Сила Лечения +{player.heal_hp}")
    input("Нажмите на Enter для продолжения.")
    system('cls')


def enemy():
    hp = 5 * randint(4, 20)
    power = 2 * randint(1, 5)
    return hp, power


def battle(player: Player, enemy_hp, enemy_power):
    print(f"Враг Здоровье -> {enemy_hp} Сила -> {enemy_power}")
    print(f"Ваше Здоровье -> {player.hp} Сила -> {player.pw}")
    print()
    print(f"1. Бьём с силой -> {player.pw}")
    print(f"2. Лечимся -> +{player.heal_hp}")
    print("3. Убегаем!")
    answer = input("Ваш выбор: ")
    if answer == "1":
        r = randint(1, 2)
        if r == 1:
            enemy_hp -= player.pw
            print("Вы наносите урон врагу!")
        else:
            player.hp -= enemy_power
            print("Враг наносит урон Вам...")
            if player.hp < 0:
                print("Вы проиграли!...")
                player.status = -1
    return answer, player, enemy_hp


def menu_fight(player):
    enemy_hp0, enemy_power0 = enemy()

    while enemy_hp0 > 0:
        n, player, enemy_hp0 = battle(player, enemy_hp0, enemy_power0)
        if n == "2":
            player.hp += player.heal_hp
            if player.hp > player.max_hp:
                player.hp = player.max_hp
            print(f"Лечимся... {player.hp}")
        elif n == "3":
            if randint(1, 3) == 3:
                print("Удалось сбежать!")
                return True
            else:
                print("Сбежать не удалось...")
    player.xp += 1
    if player.xp >= player.max_xp:
        player.xp = 0
        player.max_xp *= 5
        player.level += 1
        player.sp += 5
        menu_upgrade(player)


player0 = Player()
menu_upgrade(player0)
menu_simple(player0)
