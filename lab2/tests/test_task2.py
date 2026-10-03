import unittest
from unittest.mock import patch, AsyncMock

from lab2.tasks.task2 import main


class TestMain(unittest.IsolatedAsyncioTestCase):

    @patch("builtins.print")
    async def test_main(self, mock_print):
        await main()

        self.assertEqual(
            mock_print.call_args_list,
            [
                unittest.mock.call("2"),
                unittest.mock.call("1"),
                unittest.mock.call("3"),
            ]
        )