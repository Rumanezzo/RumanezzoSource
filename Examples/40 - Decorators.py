def decorate(func):
    print('Декорируем с помощью декоратора функцию с именем ->', func.__name__)

    def wrapper_func(*args):
        print('Исполняется ->', func.__name__)
        return func(*args)

    return wrapper_func


@decorate
def my_function(params):
    print('Мы внутри функции', my_function.__name__)
    print('Печатаем переданные параметры', params)


if __name__ == '__main__':
    my_function('Привет! Мы - переданные данные!')
