def main():

    tpl = (300, 200, 450, 1000, 750, 650, 500)

    if any(number > 600 for number in tpl):
        print('Есть дорогие ( > 600$) товары')
    if all(number % 10 == 0 for number in tpl):
        print('Все цены оканчиваются на 0')


if __name__ == '__main__':
    main()
