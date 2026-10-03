from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base


class Database:
    def __init__(self, url="sqlite:///library.db", echo=False):
        # Создаём подключение к базе данных.
        self.engine = create_engine(url, echo=echo)
        # Настраиваем фабрику сессий.
        self.session_factory = sessionmaker(
            bind=self.engine,
            expire_on_commit=False,
        )

    def create_tables(self):
        # Создаём все отсутствующие таблицы моделей.
        Base.metadata.create_all(self.engine)

    def create_session(self):
        # Возвращаем новую сессию для работы с базой.
        return self.session_factory()
