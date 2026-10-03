import unittest
from unittest.mock import patch
from lab1.tasks.task1 import pl


class TestLogger(unittest.TestCase):

    def test_pl_result(self):
        result = pl(1, 5)
        self.assertEqual(result, 6)

    @patch("builtins.print")
    def test_logger_output(self, mock_print):
        result = pl(1, 5)
        mock_print.assert_any_call("Название функции: pl")
        mock_print.assert_any_call("Аргументы функции: (1, 5)")
        mock_print.assert_any_call("Результат функции: 6")


if __name__ == '__main__':
    unittest.main()