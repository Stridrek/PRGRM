import time


def logger(cls):
    class MyClass:

        def __init__(self, *args):
            self.obj = cls(*args)

        def __getattribute__(self, name):
            if name in ("obj", "show_magic_methods", "__dict__"):
                return object.__getattribute__(self, name)

            method = getattr(self.obj, name)

            if callable(method):
                def wrapper(*args):
                    if name.startswith("__") and not self.show_magic_methods:
                        return method(*args)

                    print(f"Класс: {cls.__name__}")
                    print(f"Метод: {name}")
                    print(f"Аргументы: {args}")

                    start = time.perf_counter()
                    result = method(*args)

                    print(f"Время выполнения: {time.perf_counter() - start:.6f} сек")
                    print(f"Результат: {result}\n")

                    return result

                return wrapper

            return method

    return MyClass


@logger
class Cat:
    show_magic_methods = True

    def __init__(self, age):
        self.age = age

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age


cat = Cat(3)

cat.set_age(5)
print(cat.get_age())