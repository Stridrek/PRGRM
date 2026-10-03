import unittest
from unittest.mock import patch, mock_open
import lab3.tasks.task3


class TestGetProcesses(unittest.TestCase):

    @patch("lab3.tasks.task3.psutil.pids")
    def test_get_processes(self, mock_pids):
        mock_pids.return_value = [10, 2, 5]
        result = lab3.tasks.task3.get_processes()

        self.assertEqual(result, [2, 5, 10])


class TestGetProcessName(unittest.TestCase):

    @patch("lab3.tasks.task3.psutil.Process")
    def test_get_process_name(self, mock_process):
        mock_process.return_value.name.return_value = "telegram.exe"

        result = lab3.tasks.task3.get_process_name(123)

        self.assertEqual(result, "telegram.exe")
        mock_process.assert_called_once_with(123)

    @patch("lab3.tasks.task3.psutil.Process", side_effect=lab3.tasks.task3.psutil.AccessDenied(123))
    def test_process_permission_error(self, mock_process):
        result = lab3.tasks.task3.get_process_name(123)

        self.assertEqual(result, "Нет доступа")


class TestAddEnvironmentVariable(unittest.TestCase):

    @patch("builtins.input", side_effect=["TEST_VAR", "hello"])
    @patch.dict("lab3.tasks.task3.os.environ", {}, clear=True)
    def test_add_environment_variable(self, mock_input):
        lab3.tasks.task3.add_environment_variable()

        self.assertEqual(lab3.tasks.task3.os.environ["TEST_VAR"], "hello")

    @patch("builtins.input", side_effect=["", "hello"])
    @patch("builtins.print")
    def test_empty_variable_name(self,mock_print, mock_input):
        lab3.tasks.task3.add_environment_variable()
        mock_print.assert_called_with("Имя переменной не может быть пустым")


class TestChangePriority(unittest.TestCase):

    @patch("builtins.print")
    @patch("builtins.input", side_effect=["123", "3"])
    @patch("lab3.tasks.task3.psutil.Process")
    def test_change_priority(self, mock_process, mock_input, mock_print):
        process = mock_process.return_value

        lab3.tasks.task3.change_priority()

        mock_process.assert_called_once_with(123)

        process.nice.assert_called_once_with(lab3.tasks.task3.psutil.NORMAL_PRIORITY_CLASS)

        mock_print.assert_called_with("Приоритет процесса 123 изменён")

    @patch("builtins.input", side_effect=["abc"])
    @patch("builtins.print")
    def test_change_priority_invalid_input(self, mock_print, mock_input):
        lab3.tasks.task3.change_priority()
        mock_print.assert_called_with("Ошибка: PID должен быть целым числом")

    @patch("builtins.input", side_effect=["123", "9"])
    @patch("builtins.print")
    def test_change_priority_invalid_choice(self, mock_print, mock_input):
        lab3.tasks.task3.change_priority()

        mock_print.assert_called_with("Неверный пункт")


class TestShowProcessDetails(unittest.TestCase):

    @patch("lab3.tasks.task3.get_process_info")
    @patch("builtins.input", return_value="123")
    def test_show_process_details(self, mock_input, mock_process_info):
        lab3.tasks.task3.show_process_details()
        mock_process_info.assert_called_once_with(123)


class TestShowSystemInfo(unittest.TestCase):

    @patch("lab3.tasks.task3.os.getpid", return_value=100)
    @patch("lab3.tasks.task3.os.getppid", return_value=50)
    @patch("lab3.tasks.task3.os.cpu_count", return_value=4)
    @patch("builtins.print")
    def test_show_system_info(self, mock_print, mock_cpu_count, mock_getppid, mock_getpid):
        lab3.tasks.task3.show_system_info()
        mock_print.assert_any_call("\nИнформация о системе\n")

if __name__ == "__main__":
    unittest.main()