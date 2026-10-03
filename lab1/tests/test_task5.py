import unittest
from unittest.mock import AsyncMock, call, patch
from lab1.tasks.task5 import first_func, second_func


class TestFirstFunc(unittest.IsolatedAsyncioTestCase):

    @patch("lab1.tasks.task5.asyncio.sleep", new_callable=AsyncMock)
    @patch("builtins.print")
    async def test_first_func(self, mock_print, mock_sleep):
        await first_func()

        self.assertEqual(mock_print.call_count, 3)

        self.assertEqual(
            mock_print.call_args_list,
            [
                call("Первая функция: принт 1"),
                call("Первая функция: принт 2"),
                call("Первая функция: принт 3"),
            ],
        )

        self.assertEqual(
            mock_sleep.call_args_list,
            [
                call(1),
                call(4),
            ],
        )


class TestSecondFunc(unittest.IsolatedAsyncioTestCase):

    @patch("lab1.tasks.task5.asyncio.sleep", new_callable=AsyncMock)
    @patch("builtins.print")
    async def test_second_func(self, mock_print, mock_sleep):
        await second_func()

        self.assertEqual(mock_print.call_count, 4)

        self.assertEqual(
            mock_print.call_args_list,
            [
                call("Вторая функция: принт 1"),
                call("Вторая функция: принт 2"),
                call("Вторая функция: принт 3"),
                call("Вторая функция: принт 4"),
            ],
        )

        self.assertEqual(
            mock_sleep.call_args_list,
            [
                call(3),
                call(1),
                call(1),
            ],
        )


if __name__ == "__main__":
    unittest.main()