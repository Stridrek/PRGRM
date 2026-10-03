import time


def retry(attempts, delay, exceptions=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                try:
                    res = func(*args, **kwargs)
                    return res
                except Exception as er:
                    if exceptions is None or type(er) not in [exceptions]:
                        otv = f'Ошибка {er} не предусмотрена списком'
                        return otv
                    print(f'Попытка №{i+1}')
                    time.sleep(delay)
                    if i == attempts - 1:
                        otv = f'Ошибка {er} не была устранена'
                        return otv
            return None
        return wrapper
    return decorator


@retry(3, 1, ZeroDivisionError)
def pl(a,b):
    res = a/b
    return res

print(pl(10,2))