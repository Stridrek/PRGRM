import unittest
from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
import sys
from pathlib import Path

# Добавляем корень проекта
project_root = Path(__file__).resolve().parents[1]
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))
from library_service import LibraryService
from models import Base, Book, Booking, User


class LibraryServiceTestCase(unittest.TestCase):
    def setUp(self):
        # Создаём отдельную базу в памяти для каждого теста
        self.engine = create_engine("sqlite:///:memory:")
        # Создаём таблицы и тестовую сессию.
        Base.metadata.create_all(self.engine)
        session_factory = sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
        )
        self.session = session_factory()
        # Передаём тестовую сессию сервису
        self.service = LibraryService(self.session)

    def tearDown(self):
        # Закрываем сессию и освобождаем
        self.session.close()
        self.engine.dispose()

    def test_add_user(self):
        # Добавляем пользователя
        user = self.service.add_user("Anna", "anna@example.com")

        # Проверяем сохранённые данные
        self.assertIsNotNone(user.id)
        self.assertEqual(self.session.get(User, user.id).name, "Anna")
        self.assertEqual(
            self.session.get(User, user.id).email,
            "anna@example.com",
        )

    def test_user_email_must_be_unique(self):
        # Добавляем пользователя с первым email
        self.service.add_user("Anna", "reader@example.com")

        # Проверяем запрет повторного email
        with self.assertRaises(IntegrityError):
            self.service.add_user("Boris", "reader@example.com")

    def test_add_book(self):
        # Добавляем книгу
        book = self.service.add_book(
            "The Hobbit",
            "J. R. R. Tolkien",
            3,
        )

        # Проверяем сохранённые данные книги
        stored_book = self.session.get(Book, book.id)
        self.assertEqual(stored_book.title, "The Hobbit")
        self.assertEqual(stored_book.author, "J. R. R. Tolkien")
        self.assertEqual(stored_book.copies_available, 3)

    def test_book_copies_cannot_be_negative(self):
        # Проверяем запрет отрицательного кол-ва книг
        with self.assertRaisesRegex(ValueError, "non-negative"):
            self.service.add_book(
                "The Hobbit",
                "J. R. R. Tolkien",
                -1,
            )

    def test_create_booking_reduces_available_copies(self):
        # Подготавливаем пользователя и книгу
        user = self.service.add_user("Anna", "anna@example.com")
        book = self.service.add_book(
            "The Hobbit",
            "J. R. R. Tolkien",
            2,
        )

        # Создаём бронирование
        booking = self.service.create_booking(user.id, book.id)

        # Проверяем запись и уменьшение остатка
        self.assertEqual(booking.booking_date, date.today())
        self.assertIsNotNone(self.session.get(Booking, booking.id))
        self.assertEqual(
            self.session.get(Book, book.id).copies_available,
            1,
        )

    def test_cannot_book_unavailable_book(self):
        # Подготавливаем книгу без доступных экземпляров
        user = self.service.add_user("Anna", "anna@example.com")
        book = self.service.add_book(
            "The Hobbit",
            "J. R. R. Tolkien",
            0,
        )

        # Проверяем отказ в бронировании
        with self.assertRaisesRegex(ValueError, "No copies"):
            self.service.create_booking(user.id, book.id)

    def test_cannot_book_for_unknown_user(self):
        # Добавляем книгу без создания пользователя
        book = self.service.add_book(
            "The Hobbit",
            "J. R. R. Tolkien",
            1,
        )

        # Проверяем отказ для неизвестного пользователя
        with self.assertRaisesRegex(ValueError, "User"):
            self.service.create_booking(999, book.id)

    def test_delete_booking_restores_available_copy(self):
        # Создаём данные и бронирование
        user = self.service.add_user("Anna", "anna@example.com")
        book = self.service.add_book(
            "The Hobbit",
            "J. R. R. Tolkien",
            1,
        )
        booking = self.service.create_booking(user.id, book.id)

        # Удаляем бронирование
        deleted_id = self.service.delete_booking(booking.id)

        # Проверяем удаление и возврат книги
        self.assertEqual(deleted_id, booking.id)
        self.assertIsNone(self.session.get(Booking, booking.id))
        self.assertEqual(
            self.session.get(Book, book.id).copies_available,
            1,
        )

    def test_cannot_delete_unknown_booking(self):
        # Проверяем ошибку для неизвестного бронирования
        with self.assertRaisesRegex(ValueError, "Booking"):
            self.service.delete_booking(999)


if __name__ == "__main__":
    unittest.main()
