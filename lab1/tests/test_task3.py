import unittest
from unittest.mock import patch
from lab1.tasks.task3 import Cat


class TestCat(unittest.TestCase):

    @patch("builtins.print")
    def test_method_logging(self, mock_print):
        cat = Cat(3)
        cat.set_age(5)

        output = [str(call.args[0]).rstrip() for call in mock_print.call_args_list]

        self.assertIn("Класс: Cat", output)
        self.assertIn("Метод: set_age", output)
        self.assertIn("Аргументы: (5,)", output)
        self.assertIn("Результат: None", output)

    @patch("builtins.print")
    def test_get_age_logging(self, mock_print):
        cat = Cat(3)

        result = cat.get_age()

        self.assertEqual(result, 3)

        output = [str(call.args[0]).rstrip() for call in mock_print.call_args_list]

        self.assertIn("Класс: Cat", output)
        self.assertIn("Метод: get_age", output)
        self.assertIn("Результат: 3", output)


if __name__ == "__main__":
    unittest.main()