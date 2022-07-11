filename = input("Введите Имя Файла -> ")
f = open(filename, 'w')
f.write('Hello -> ')
f.write('World\n')
f.write('Перешли на Другую Строку и на Ней Остановились...')
f.close()
print('Открыли Файл для Записи', filename, 'и Записали в Него...')

f = open(filename, 'r')
text = f.read()
print('\n[*begin of text*]\n', text, '\n[*end of text*]', sep='')

input("\nНажмите на Enter для завершения ->")
