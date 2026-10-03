import os


#1) Скопирует файл с предыдущего задания;
def copy_file(source_path, copy_path):
    if os.path.exists(source_path):
        with open(source_path, "r") as source:
            data = source.read()
        with open(copy_path, "w") as copy:
            copy.write(data)
        return "Файл скопирован"
    else:
        return "Файл из первого задания не найден"

#2) Переименует файл. Создайте несколько вложенных директорий и переместите копию файла в одну из них;
def move_rename_file_in_dirs(current_dir, copy_path):
    #переименовать
    new_path = os.path.join(current_dir, "task2.txt")
    os.rename(copy_path, new_path)
    #создать dir/dir/dir
    os.makedirs(f'{current_dir}/One/Two/Three')
    #переместить
    os.replace(new_path, f"{current_dir}/One/Two/Three/task2.txt")
    return "Файл перемещен во вложенную директорию"


#3) Создаст новый файл. Переместите и переименуйте его с помощью одной команды os;
def mrr_one_command(current_dir):
    new_path = os.path.join(current_dir, "task2_4.txt")
    open(new_path, "w").close()
    os.rename(new_path, f"{current_dir}/One/Two/Three/task2_004.txt")
    return "Новый файл перемещен с помощью одной команды"

#4) Программно создайте ещё несколько файлов. Выведите все файлы и директории, лежащие в папке,
# в которой запущен скрипт. Переместитесь во вложенную директорию в которую переместили файл.
# Выведите все, что находится в этой директории;
def files_and_dirs(current_dir):
    #создать файлы
    open("file1.txt", "w").close()
    open("file2.txt", "w").close()
    open("file3.txt", "w").close()
    #показать содержимое
    a = f'Содержимое текущей папки: {os.listdir()}\n'
    #показать содержимое след папки
    os.chdir(f"{current_dir}/One/Two/Three")
    b = f"Содержимое вложенной директории: {os.listdir()}"
    return a + b

#5) Вернитесь в папку со скриптом; Создайте пустую директорию,
# после чего удалите её. Создайте ещё несколько вложенных директорий и файлов;
def rmdir_and_new_files_dirs(current_dir):
    os.chdir(current_dir)
    os.mkdir("empty_folder")
    os.rmdir("empty_folder")

    os.makedirs("folder1/folder2/folder3")
    open("folder1/file1.txt", "w").close()
    open("folder1/folder2/file2.txt", "w").close()
    open("folder1/folder2/folder3/file3.txt", "w").close()
    return "Директория создана и удалена. Созданы вложенные директории с файлами"

#6) Обойдите текущую директорию и выведите: путь до каждой папки, список файлов в каждой папке.
def walk_dirs():
    for root, dirs, files in os.walk("."):
        print("Содержимое папки: ", root)
        for file in files:
            print("  Файл:", file)
        for directory in dirs:
            print("  Директория:", directory)

def main():
    current_dir = os.getcwd()
    source_file_name = "file.txt"
    source_path = os.path.join(current_dir, source_file_name)
    copy_path = os.path.join(current_dir, "task1_copy.txt")

    print(copy_file(source_path, copy_path))
    print(move_rename_file_in_dirs(current_dir, copy_path))
    print(mrr_one_command(current_dir))
    print(files_and_dirs(current_dir))
    print(rmdir_and_new_files_dirs(current_dir))
    walk_dirs()


if __name__ == "__main__":
    main()