import unittest
from lab1.tasks.task2 import retry, pl


class TestRetry(unittest.TestCase):

    def test_success(self):
        #res ф-ии
        self.assertEqual(pl(10, 2), 5)

    def test_zero_division(self):
        #Ошибка ZeroDivisionError
        self.assertEqual(pl(10, 0),"Ошибка division by zero не была устранена")

    def test_unexpected_exception(self):
        #Ошибка не из exceptions
        @retry(3, 1, ZeroDivisionError)
        def func():
            raise ValueError("ошибка")

        self.assertEqual(func(),"Ошибка ошибка не предусмотрена списком")

    def test_retry(self):
        #Проеврка повторов ф-ии
        attempts = 0

        @retry(3, 1, ZeroDivisionError)
        def func():
            nonlocal attempts
            attempts += 1
            if attempts < 3:
                raise ZeroDivisionError("ошибка")
            return "success"

        self.assertEqual(func(), "success")
        self.assertEqual(attempts, 3)


if __name__ == "__main__":
    unittest.main()