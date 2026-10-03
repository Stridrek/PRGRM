import unittest
from unittest.mock import patch
from lab1.tasks.task4 import Test


class TestCallLimiter(unittest.TestCase):

    def test_limit_two(self):
        obj = Test()

        with patch("builtins.print") as mock_print:
            obj.hello()
            obj.hello()
            obj.hello()

        self.assertEqual(mock_print.call_count, 3)
        self.assertEqual(
            mock_print.call_args_list,
            [
                unittest.mock.call("Привет"),
                unittest.mock.call("Привет"),
                unittest.mock.call("Лимит вызовов исчерпан"),
            ]
        )

    def test__limits_methods(self):

        obj = Test()

        with patch("builtins.print") as mock_print:
            obj.hello()
            obj.hello()
            obj.hello()

            obj.whatsup()
            obj.whatsup()
            obj.whatsup()

        self.assertEqual(mock_print.call_count, 6)

        self.assertEqual(
            mock_print.call_args_list,
            [
                unittest.mock.call("Привет"),
                unittest.mock.call("Привет"),
                unittest.mock.call("Лимит вызовов исчерпан"),

                unittest.mock.call("Как дела?"),
                unittest.mock.call("Как дела?"),
                unittest.mock.call("Лимит вызовов исчерпан"),
            ]
        )

if __name__ == "__main__":
    unittest.main()