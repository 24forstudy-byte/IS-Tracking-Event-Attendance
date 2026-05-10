import sqlite3
# Импорт имени файла базы данных из конфигурационного файла
from config import DB_NAME

# Функция для подключения к базе данных
def get_connection():
    # Возвращает объект соединения с указанной базой данных
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

# Функция инициализации базы данных: создаёт все таблицы, если они ещё не существуют
def initialize_db():
    # Устанавливаем соединение с базой
    conn = get_connection()
    # Получаем объект курсора для выполнения SQL-запросов
    cursor = conn.cursor()

    # Создание таблицы "Мероприятие"
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Event (
                   EventID INTEGER PRIMARY KEY AUTOINCREMENT, -- Номер мероприятия
                   Title TEXT NOT NULL, -- Название мероприятия
                   DateTime TEXT NOT NULL, -- Дата и время
                   Status TEXT NOT NULL, -- Статус мероприятия
                   EventTypeID INTEGER, -- Номер типа мероприятия (внешний ключ)
                   PlaceID INTEGER, -- Номер места (внешний ключ)
                   FOREIGN KEY (EventTypeID) REFERENCES EventType(EventTypeID), -- Связь с таблицей типа мероприятия
                   FOREIGN KEY (PlaceID) REFERENCES Place(PlaceID) -- Связь с таблицей места
                    )
                ''')
    
    # Создание таблицы "Заявка"
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Application (
                   ApplicationID INTEGER PRIMARY KEY AUTOINCREMENT, -- Номер заявки
                   DateTime TEXT NOT NULL, -- Дата и время
                   ParticipantID INTEGER, -- Номер участника (внешний ключ)
                   EventID INTEGER, -- Номер мероприятия (внешний ключ)
                   StaffID INTEGER, -- Номер персонала (внешний ключ)
                   FOREIGN KEY (ParticipantID) REFERENCES Participant(ParticipantID), -- Связь с таблицей участника
                   FOREIGN KEY (EventID) REFERENCES Event(EventID) ON DELETE CASCADE, -- Связь с таблицей мероприятия
                   FOREIGN KEY (StaffID) REFERENCES Staff(StaffID) -- Связь с таблицей персонала
                    )
                ''')
    
    # Создание таблицы "Персонал"
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Staff (
                   StaffID INTEGER PRIMARY KEY AUTOINCREMENT, -- Номер персонала
                   FULLNAME TEXT NOT NULL, -- ФИО
                   Phone TEXT NOT NULL, -- Телефон
                   Mail TEXT NOT NULL -- Почта
                    )
                ''')
    
    # Создание таблицы "Участник"
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Participant (
                   ParticipantID INTEGER PRIMARY KEY AUTOINCREMENT, -- Номер участника
                   FULLNAME TEXT NOT NULL, -- ФИО
                   Phone TEXT NOT NULL, -- Телефон
                   Mail TEXT NOT NULL -- Почта
                    )
                ''')
    
    # Создание таблицы "Место"
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Place (
                   PlaceID INTEGER PRIMARY KEY AUTOINCREMENT, -- Номер места
                   Title TEXT NOT NULL, -- Название
                   Address TEXT NOT NULL -- Адрес
                    )
                ''')
    
    # Создание таблицы "ТипМероприятия"
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS EventType(
                   EventTypeID INTEGER PRIMARY KEY AUTOINCREMENT, -- Номер типа мероприятия
                   Title TEXT NOT NULL -- Название
                    )
                ''')
    
    # Сохраняем изменения
    conn.commit()
    # Закрываем соединение с БД
    conn.close()