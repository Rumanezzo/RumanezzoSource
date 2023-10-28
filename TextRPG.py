from random import randint


class Player:
    hp = 100
    damage = 10


p0 = Player()


class Enemy:
    hp = randint(70, 130)
    damage = randint(6, 13)


e0 = Enemy()


def menu(p):
    while True:
        print("1) Сражаться")
        print("2) Посмотреть статистику")

        try:
            n = int(input("Введите число: "))

            if n == 1:
                menu_fight(p)
            if n == 2:
                menu_stats(p)
            else:
                print("Чего ждем?")

        except NameError:
            print("Введите число")
        except SyntaxError:
            print("Введите число")


def menu_stats(p):
    print("Статистика игрока")
    print("*****************")

    print(f"hp {p.hp}")
    print(f"Вы hp: {p.hp} damage: {p.damage}")
    print(f"damage {p.damage}.")
    input("Нажмите Enter для продолжения.")


def menu_fight(p):
    while e0.hp > 0:
        # Также, как я и сказал по последовательности списка расставляет переменные.
        print(f"Вы hp: {p.hp} damage: {p.damage}")
        print(f"Враг hp: {e0.hp} damage: {e0.damage}")
        print("**********************")
        print("1)Ударить")
        print("2)Хил 0-5")
        n = int(input("Введите число: "))
        if n == 1:

            e0.hp -= p.damage
            print(f"Вы ударили противника, у него осталось {e0.hp} hp")
        
            p.hp -= e0.damage
            print(f"Противник ударил вас, у вас осталось {p.hp} hp")

            print("*********************")

        if n == 2:
            # Рандомно от 0 до 5 добавляет хп.
            p.hp += randint(0, 5)
            # Если здоровье игрока больше, то хп игрока будет равна 100.
            if p.hp > 100:
                p.hp = 100

            print(f"Ваши хп {p.hp}")

        else:
            print("Чего ждем?")
        if p.hp < 0:
            print("Вы проиграли")
        if e0.hp < 0:
            print("Вы победили")

        print("******************")


# Вызов меню.
menu(p0)
