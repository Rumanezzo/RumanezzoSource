def main():
    def my_sum(array_):
        if not array_:
            return 0
        else:
            return array_[0] + my_sum(array_[1:])

    array = list(map(int, input('Введите несколько целых числа через пробел -> ').split())) or [1, 2, 3]
    print('Ваш список ->', array)
    print('Сумма введенных вами чисел ->', my_sum(array))
    input('•••• Нажмите «Enter» для завершения ••••')


if __name__ == '__main__':
    main()
