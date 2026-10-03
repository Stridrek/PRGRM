import time

def logger(func):
    def wrapper(*args, **kwargs):
        print(f'Название функции: {func.__name__}')
        print(f'Аргументы функции: {args}')
        start = time.perf_counter()
        a = func(*args, **kwargs)
        print(f'Время выполнения функции: {time.perf_counter() - start}')
        print(f'Результат функции: {a}')
        return a
    return wrapper

@logger
def pl(x, y):
    time.sleep(1)
    a=x+y
    return a

pl(1,5)