import unittest
from unittest.mock import AsyncMock, patch

from lab2.tasks.task1 import mes


class TestMes(unittest.IsolatedAsyncioTestCase):
    @patch("lab2.tasks.task1.asyncio.sleep", new_callable=AsyncMock)
    @patch("builtins.print")
    async def test_mes(self, mock_print, mock_sleep):
        await mes(2, "Привет!")

        mock_sleep.assert_awaited_once_with(2)
        mock_print.assert_called_once_with("Привет!")


if __name__ == "__main__":
    unittest.main()