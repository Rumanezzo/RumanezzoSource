def main():
    list1 = [4, 6, 3, -5, -6, 5, 11, 8, -2, 7, 9, 10, -4, -3]
    list2 = [(0 if x < 0 else x * x // 2) for x in list1 if x % 2 == 0]
    print(list(list2))


if __name__ == '__main__':
    main()
    input('«Нажмите «Enter» для завершения ••••» ')
