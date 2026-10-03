import os
import psutil


def get_processes():
    #Возвращает список PID запущенных процессов
    return sorted(psutil.pids())


def get_process_name(pid):
    try:
        process = psutil.Process(pid)
        return process.name()

    except psutil.NoSuchProcess:
        return "Процесс не найден"

    except psutil.AccessDenied:
        return "Нет доступа"


def get_process_info(pid):
    #Выводит подробную информацию о процессе
    try:
        process = psutil.Process(pid)

        print(f"\nИнформация о процессе PID {pid}\n")

        print(f"Имя: {process.name()}")
        print(f"Командная строка: {process.cmdline()}")
        print(f"Статус: {process.status()}")
        print(f"Родительский PID: {process.ppid()}")
        print(f"Количество потоков: {process.num_threads()}")

    except psutil.NoSuchProcess:
        print("Процесс не найден")

    except psutil.AccessDenied:
        print("Нет доступа")

    except psutil.Error as error:
        print(f"Ошибка: {error}")


def show_processes():
    #Показывает список процессов
    processes = get_processes()

    if not processes:
        return

    print("\nСписок запущенных процессов:\n")

    for pid in processes:
        name = get_process_name(pid)
        print(f"PID: {pid:<8} Имя: {name}")


def terminate_process():
    #Завершает процесс по PID
    try:
        pid = int(input("Введите PID процесса: "))

        if pid <= 0:
            print("PID должен быть положительным числом")
            return

        process = psutil.Process(pid)
        process.terminate()

        print(f"Сигнал завершения отправлен процессу {pid}")

    except ValueError:
        print("Ошибка: PID должен быть целым числом")

    except psutil.NoSuchProcess:
        print("Ошибка: процесс с таким PID не существует")

    except psutil.AccessDenied:
        print("Ошибка: недостаточно прав для завершения процесса")

    except psutil.Error as error:
        print(f"Ошибка: {error}")


def show_environment():
    #Показывает переменные окружения
    print("\nПеременные окружения:\n")

    for key, value in sorted(os.environ.items()):
        print(f"{key}={value}")


def add_environment_variable():
    #Добавляет переменную окружения
    key = input("Введите имя переменной: ").strip()
    value = input("Введите значение переменной: ")

    if not key:
        print("Имя переменной не может быть пустым")
        return

    try:
        os.environ[key] = value
        print(f"Переменная {key} успешно добавлена/изменена")

        print(
            "Примечание: изменение os.environ действует только "
            "для текущего процесса Python и его дочерних процессов"
        )

    except Exception as error:
        print(f"Ошибка при изменении окружения: {error}")


def environment_menu():
    #Меню работы с переменными
    while True:
        print("\n Переменные окружения ")
        print("1. Показать переменные")
        print("2. Добавить/изменить переменную")
        print("3. Назад")

        choice = input("Выберите действие: ")

        if choice == "1":
            show_environment()

        elif choice == "2":
            add_environment_variable()

        elif choice == "3":
            break

        else:
            print("Неверный пункт меню")


def change_priority():
    try:
        pid = int(input("Введите PID процесса: "))

        print("\nВыберите приоритет:")
        print("1. Высокий")
        print("2. Выше обычного")
        print("3. Обычный")
        print("4. Ниже обычного")
        print("5. Низкий")

        choice = input("Выберите приоритет: ")

        priorities = {
            "1": psutil.HIGH_PRIORITY_CLASS,
            "2": psutil.ABOVE_NORMAL_PRIORITY_CLASS,
            "3": psutil.NORMAL_PRIORITY_CLASS,
            "4": psutil.BELOW_NORMAL_PRIORITY_CLASS,
            "5": psutil.IDLE_PRIORITY_CLASS
        }

        if choice not in priorities:
            print("Неверный пункт")
            return

        process = psutil.Process(pid)
        process.nice(priorities[choice])

        print(f"Приоритет процесса {pid} изменён")

    except ValueError:
        print("Ошибка: PID должен быть целым числом")

    except psutil.NoSuchProcess:
        print("Ошибка: процесс с таким PID не существует")

    except psutil.AccessDenied:
        print("Ошибка: недостаточно прав")

    except psutil.Error as error:
        print(f"Ошибка: {error}")


def show_system_info():
    print("\nИнформация о системе\n")

    print(f"Операционная система: {os.name}")
    print(f"Платформа: {os.sys.platform}")
    print(f"Текущий каталог: {os.getcwd()}")
    print(f"Домашний каталог: {os.path.expanduser('~')}")
    print(f"PID текущего процесса: {os.getpid()}")
    print(f"PID родительского процесса: {os.getppid()}")
    print(f"Количество CPU: {os.cpu_count()}")
    print(f"Разделитель каталогов: {os.sep}")
    print(f"Разделитель PATH: {os.pathsep}")


def show_process_details():
    #Запрашивает PID и показывает информацию
    try:
        pid = int(input("Введите PID процесса: "))

        if pid <= 0:
            print("PID должен быть положительным числом")
            return

        get_process_info(pid)

    except ValueError:
        print("Ошибка: PID должен быть целым числом")


def main():

    while True:
        print("   УПРАВЛЕНИЕ СИСТЕМНЫМИ ПРОЦЕССАМИ   ")
        print("a) Показать список всех запущенных процессов")
        print("b) Показать информацию о процессе")
        print("c) Завершить процесс по PID")
        print("d) Показать/добавить переменные окружения")
        print("e) Изменить приоритет процесса")
        print("f) Показать информацию о системе")
        print("g) Выход")

        choice = input("Выберите пункт: ").lower().strip()

        if choice == "a":
            show_processes()

        elif choice == "b":
            show_process_details()

        elif choice == "c":
            terminate_process()

        elif choice == "d":
            environment_menu()

        elif choice == "e":
            change_priority()

        elif choice == "f":
            show_system_info()

        elif choice == "g":
            print("Программа завершена")
            break

        else:
            print("Ошибка: такого пункта меню нет")


if __name__ == "__main__":
    main()