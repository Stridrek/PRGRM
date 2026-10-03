from datetime import date

from sqlalchemy.exc import SQLAlchemyError

from models import Book, Booking, User


class LibraryService:
    def __init__(self, session):
        self.session = session

    def add_user(self, name, email):
        # Проверяем данные пользователя
        if not name or not email:
            raise ValueError("User name and email must not be empty")

        # Создаём нового пользователя
        user = User(name=name, email=email)
        try:
            # Сохраняем в базе
            self.session.add(user)
            self.session.commit()
            self.session.refresh(user)
        except SQLAlchemyError:
            # Отменяем при ошибке
            self.session.rollback()
            raise

        return user

    def add_book(self, title, author, copies_available):
        # Проверяем данные книги
        if not title or not author:
            raise ValueError("Book title and author must not be empty")
        # Проверка на отрицательное количество
        if not isinstance(copies_available, int) or copies_available < 0:
            raise ValueError("Number of available copies must be non-negative")

        # Новая книга
        book = Book(
            title=title,
            author=author,
            copies_available=copies_available,
        )
        try:
            # Сохраняем книгу
            self.session.add(book)
            self.session.commit()
            self.session.refresh(book)
        except SQLAlchemyError:
            # Отмена при ошибке.
            self.session.rollback()
            raise

        return book

    def create_booking(self, user_id, book_id):
        # Проверяем существование пользователя
        user = self.session.get(User, user_id)
        if user is None:
            raise ValueError(f"User with id={user_id} does not exist")

        # Проверяем существование и доступность книги
        book = self.session.get(Book, book_id)
        if book is None:
            raise ValueError(f"Book with id={book_id} does not exist")
        if book.copies_available <= 0:
            raise ValueError("No copies of this book are available")

        # Создаём бронирование с датой
        booking = Booking(
            user_id=user.id,
            book_id=book.id,
            booking_date=date.today(),
        )
        # Уменьшаем количество экземпляров
        book.copies_available -= 1
        try:
            # Сохраняем бронирование и остаток
            self.session.add(booking)
            self.session.commit()
            self.session.refresh(booking)
        except SQLAlchemyError:
            # Отменяем при ошибке
            self.session.rollback()
            raise

        return booking

    def delete_booking(self, booking_id):
        # Находим удаляемое бронирование
        booking = self.session.get(Booking, booking_id)
        if booking is None:
            raise ValueError(f"Booking with id={booking_id} does not exist")

        # Находим связанную с бронированием книгу
        book = self.session.get(Book, booking.book_id)
        if book is None:
            raise ValueError(f"Book with id={booking.book_id} does not exist")

        # Возвращаем экземпляр книги в доступные
        book.copies_available += 1
        try:
            # Удаляем бронирование и сохраняем
            self.session.delete(booking)
            self.session.commit()
        except SQLAlchemyError:
            # Отменяем при ошибке.
            self.session.rollback()
            raise

        return booking_id
