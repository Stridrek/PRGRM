import os
import unittest
import tempfile
from lab3.tasks.task1 import create_file, get_file_info, get_user_info, change_access_rights


class TestFileFunc(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file_path = os.path.join(self.temp_dir.name, "test.txt")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_create_file(self):
        result = create_file(self.temp_dir.name, self.file_path)

        self.assertTrue(os.path.exists(self.file_path))
        self.assertEqual(result, "Файл создан и существует")

    def test_get_file_info(self):
        create_file(self.temp_dir.name, self.file_path)

        res = get_file_info(self.file_path)

        self.assertIn("Размер файла:", res)
        self.assertIn("Дата последнего изменения:", res)
        self.assertIn("Дата последнего доступа к этому файлу:", res)

    def test_get_user_info(self):
        create_file(self.temp_dir.name, self.file_path)

        res = get_user_info()

        self.assertIn("Пользователь:", res)

    def test_change_access_rights(self):
        create_file(self.temp_dir.name, self.file_path)

        change_access_rights(self.file_path)

        mode = os.stat(self.file_path).st_mode & 0o777
        self.assertEqual(mode, 0o644)


if __name__ == "__main__":
    unittest.main()