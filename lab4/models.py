from datetime import date

from sqlalchemy import Date, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, mapped_column, relationship

# Создаём класс для всех моделей
Base = declarative_base()


class User(Base):
    # Связываем модель с таблицей пользователей
    __tablename__ = "users"

    # Описываем поля пользователя.
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String, nullable=False)
    email = mapped_column(String, nullable=False, unique=True)

    # Получаем все бронирования пользователя
    bookings = relationship(
        "Booking",
        back_populates="user",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        # Формируем строку для отладки
        return (
            f"User(id={self.id!r}, name={self.name!r}, "
            f"email={self.email!r})"
        )


class Book(Base):
    # Связываем модель с таблицей книг
    __tablename__ = "books"

    # Описываем книги
    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String, nullable=False)
    author = mapped_column(String, nullable=False)
    copies_available = mapped_column(Integer, nullable=False, default=0)

    # Получаем все бронирования книги
    bookings = relationship(
        "Booking",
        back_populates="book",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        # Формируем строку для отладки
        return (
            f"Book(id={self.id!r}, title={self.title!r}, "
            f"author={self.author!r}, "
            f"copies_available={self.copies_available!r})"
        )


class Booking(Base):
    # Связываем модель с таблицей бронирований
    __tablename__ = "bookings"

    # Храним ссылки на пользователя, книгу и дату
    id = mapped_column(Integer, primary_key=True)
    user_id = mapped_column(ForeignKey("users.id"), nullable=False)
    book_id = mapped_column(ForeignKey("books.id"), nullable=False)
    booking_date = mapped_column(Date, nullable=False, default=date.today)

    # Настраиваем связи с пользователем и книгой
    user = relationship("User", back_populates="bookings")
    book = relationship("Book", back_populates="bookings")

    def __repr__(self):
        # Формируем строку для отладки
        return (
            f"Booking(id={self.id!r}, user_id={self.user_id!r}, "
            f"book_id={self.book_id!r}, booking_date={self.booking_date!r})"
        )
