import os
import unittest
import tempfile
from lab3.tasks.task2 import copy_file, move_rename_file_in_dirs, mrr_one_command, files_and_dirs, rmdir_and_new_files_dirs, walk_dirs


class TestFileFunctions(unittest.TestCase):

    def setUp(self):
        # Временная папка
        self.old_dir = os.getcwd()
        self.test_dir = tempfile.TemporaryDirectory()
        self.current_dir = self.test_dir.name

    def tearDown(self):
        # Зачистка
        os.chdir(self.old_dir)
        self.test_dir.cleanup()

    def test_copy_file(self):
        source_path = os.path.join(self.current_dir, "file.txt")
        copy_path = os.path.join(self.current_dir, "copy.txt")

        with open(source_path, "w") as file:
            file.write("Hello!")

        result = copy_file(source_path, copy_path)

        self.assertEqual(result, "Файл скопирован")
        self.assertTrue(os.path.exists(copy_path))

        with open(copy_path, "r") as file:
            self.assertEqual(file.read(), "Hello!")

    def test_move_rename_file_in_dirs(self):
        copy_path = os.path.join(self.current_dir, "copy.txt")

        with open(copy_path, "w") as file:
            file.write("test")

        result = move_rename_file_in_dirs(self.current_dir, copy_path)

        final_path = os.path.join(self.current_dir, "One/Two/Three/task2.txt")

        self.assertEqual(result, "Файл перемещен во вложенную директорию")

        self.assertTrue(os.path.exists(final_path))
        self.assertFalse(os.path.exists(copy_path))

    def test_mrr_one_command(self):
        os.makedirs(os.path.join(self.current_dir, "One/Two/Three"))

        result = mrr_one_command(self.current_dir)

        final_path = os.path.join(self.current_dir, "One/Two/Three/task2_004.txt")

        self.assertEqual(result, "Новый файл перемещен с помощью одной команды")

        self.assertTrue(os.path.exists(final_path))

    def test_files_and_dirs(self):
        os.makedirs(os.path.join(self.current_dir, "One/Two/Three"))

        old_dir = os.getcwd()

        try:
            os.chdir(self.current_dir)

            result = files_and_dirs(self.current_dir)

            self.assertIn("file1.txt", result)
            self.assertIn("file2.txt", result)
            self.assertIn("file3.txt", result)
            self.assertIn("Содержимое текущей папки:", result)
            self.assertIn("Содержимое вложенной директории:", result)
        finally:
            os.chdir(old_dir)

    def test_rmdir_and_new_files_dirs(self):
        result = rmdir_and_new_files_dirs(self.current_dir)

        self.assertEqual(result, "Директория создана и удалена. Созданы вложенные директории с файлами")

        self.assertFalse(os.path.exists(os.path.join(self.current_dir, "empty_folder")))

        self.assertTrue(os.path.exists(os.path.join(self.current_dir, "folder1/folder2/folder3/file3.txt")))


if __name__ == "__main__":
    unittest.main()