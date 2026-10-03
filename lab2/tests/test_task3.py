import unittest
from unittest.mock import patch, MagicMock, call

import lab2.tasks.task3


class TestRequests(unittest.TestCase):

    @patch("lab2.tasks.task3.requests.get")
    def test_norm_request(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200)

        lab2.tasks.task3.norm_request()

        self.assertEqual(mock_get.call_count, len(lab2.tasks.task3.urls))

        expected_calls = [
            call(url)
            for url in lab2.tasks.task3.urls
        ]


class TestAsyncRequests(unittest.IsolatedAsyncioTestCase):

    @patch("lab2.tasks.task3.requests.get")
    async def test_async_request(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200)

        await lab2.tasks.task3.async_request(lab2.tasks.task3.urls[0])

        mock_get.assert_called_once_with(lab2.tasks.task3.urls[0])

    @patch("lab2.tasks.task3.requests.get")
    async def test_asynchronous(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200)

        await lab2.tasks.task3.asynchronous()

        self.assertEqual(
            mock_get.call_count,
            len(lab2.tasks.task3.urls)
        )


if __name__ == "__main__":
    unittest.main()