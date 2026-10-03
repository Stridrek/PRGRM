import unittest
import time
from unittest.mock import patch
from lab2.tasks.task4 import print_message, run_norm, run_threads


class TestPrintMessage(unittest.TestCase):

    @patch("lab2.tasks.task4.time.sleep")
    @patch("builtins.print")
    def test_print_message(self, mock_print, mock_sleep):
        print_message("Hello", 2)

        mock_sleep.assert_called_once_with(2)
        mock_print.assert_called_once_with("Hello")

class TestThreads(unittest.TestCase):
    def test_run_threads(self):
        start = time.perf_counter()
        run_threads(2)
        res = time.perf_counter() - start
        self.assertEqual(round(res), 2)

    def test_run_norm(self):
        start = time.perf_counter()
        run_norm(2)
        res = time.perf_counter() - start
        self.assertEqual(round(res), 6)

if __name__ == "__main__":
    unittest.main()
