import sys
from pathlib import Path

# Добавляем корень проекта
project_root = Path(__file__).resolve().parents[1]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from database import Database
from library_service import LibraryService

# Создаём временную SQLite-базу для примера
database = Database("sqlite:///:memory:")
# Создаём таблицы пользователей, книг и бронирований
database.create_tables()

# Открываем сессию
with database.create_session() as session:
    # Создаём и добавляем данные
    library = LibraryService(session)
    user = library.add_user("Анна", "anna@example.com")
    book = library.add_book("Мастер и Маргарита", "М. А. Булгаков", 2)
    # Бронируем книгу, удаляем бронирование
    booking = library.create_booking(user.id, book.id)
    library.delete_booking(booking.id)

    print("Пример успешно выполнен.")
