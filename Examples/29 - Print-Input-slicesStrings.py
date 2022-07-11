name = input("Привет! Как тебя зовут? --> ")
print("Я поняла! Тебя зовут", name)
print("Привет,", name)
print(name, "- неплохо рифмуется с", name.replace(name[:3], "Жук"), "?")
print("И вполне может быть заменено на", name.replace(name[:3], "Хрюн"), "?")

input('Нажми на клавишу [Enter], чтобы выйти!')
