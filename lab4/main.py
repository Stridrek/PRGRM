from database import Database
from library_service import LibraryService

if __name__ == "__main__":
    # Подключаемся базе SQLite
    database = Database()
    # Создаём таблицы
    database.create_tables()

    # Открываем сессию и создаём сервис
    with database.create_session() as session:
        service = LibraryService(session)
        # Сообщаем о готовности
        print("Сервис готов к использованию. ")
