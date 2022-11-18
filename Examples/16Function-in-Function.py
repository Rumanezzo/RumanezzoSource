def sq_sum():
    def get_n():
        n1 = int(input("Слагаемых в сумме: n="))
        return n1

    def find_sq_sum():
        s_ = 0
        for i in range(1, n_ + 1):
            s_ += i ** 2
        return s_, n_

    n_ = get_n()
    return find_sq_sum


s, n = sq_sum()()
print("Сумма квадратов от 1 до", n, "равна:", s)

input("Нажмите на Enter для завершения -> ")
