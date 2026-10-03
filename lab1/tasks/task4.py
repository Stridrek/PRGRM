def call_limiter(limit):
    def logger(cls):
        class MyClass:
            def __init__(self, *args):
                self.obj = cls(*args)
                self.calls = {}

            def __getattr__(self, name):
                method = getattr(self.obj, name)

                if callable(method):
                    def wrapper(*args):
                        if name not in self.calls:
                            self.calls[name] = 0

                        if self.calls[name] >= limit:
                            print("Лимит вызовов исчерпан")
                            return

                        self.calls[name] += 1
                        return method(*args)

                    return wrapper

                return method

        return MyClass

    return logger


@call_limiter(2)
class Test:
    def hello(self):
        print("Привет")

    def whatsup(self):
        print("Как дела?")


obj = Test()

obj.hello()
obj.hello()
obj.hello()

obj.whatsup()
obj.whatsup()
obj.whatsup()
obj.whatsup()
