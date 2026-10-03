import os
from datetime import datetime

#1) Создает файл в текущей директории;
#2) Запишет в него любые адекватные данные. С помощью библиотеки os проверьте,
# что файл существует, при этом запрещается писать пути руками (но дописывать пути разрешается);
def create_file(current_dir, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        for i in range(100):
            file.write(f"{i}\n")

    if os.path.exists(file_path):
        return "Файл создан и существует"
    else:
        return "Файл существует"


#3) Выведет размер файла в байтах, дату последнего изменения, дату последнего доступа к этому файлу;
def get_file_info(file_path):
    stat = os.stat(file_path)
    mod_date = datetime.fromtimestamp(stat.st_mtime)
    access_date = datetime.fromtimestamp(stat.st_atime)
    return (
        f"Размер файла: {stat.st_size}\n"
        f"Дата последнего изменения: {mod_date.strftime('%d.%m.%Y %H:%M:%S')}\n"
        f"Дата последнего доступа к этому файлу: {access_date.strftime('%d.%m.%Y %H:%M:%S')}"
    )


#4) Выведет текущего пользователя;
def get_user_info():
    uinfo= os.getlogin()
    return f"Пользователь: {uinfo}"


#5) Посмотрите уровень доступа к этому файлу. Поменяйте права доступа к нему. Проверьте, что у вас всё получилось.
def change_access_rights(file_path):
    mode = os.stat(file_path).st_mode
    print("Права до изменения:", oct(mode & 0o777))

    os.chmod(file_path, 0o644)

    mode = os.stat(file_path).st_mode
    print("Права после изменения:", oct(mode & 0o777))


if __name__ == "__main__":
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, "file.txt")
    print(create_file(current_dir, file_path))
    print(get_file_info(file_path))
    print(get_user_info())
    os.chmod(file_path, 0o664)
    change_access_rights(file_path)
