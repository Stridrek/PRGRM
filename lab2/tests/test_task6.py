import unittest
from lab2.tasks.task6 import run_threads

class TestTask1(unittest.TestCase):

    def test_counter(self):
        result = run_threads()
        self.assertEqual(result, 50_000)

if __name__ == "__main__":
    unittest.main()