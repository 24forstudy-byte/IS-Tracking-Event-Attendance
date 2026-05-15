from database.db_manager import get_connection

class EventType:
    def __init__(self, EventTypeID=None, Title=None):
        self.EventTypeID = EventTypeID
        self.Title = Title

    def save(self):
        """Добавляет новый тип мероприятия или обновляет существующий"""
        conn = get_connection()
        cursor = conn.cursor()
        if self.EventTypeID is None:
            cursor.execute(
                "INSERT INTO EventType (Title) VALUES (?)",
                (self.Title,)
            )
            self.EventTypeID = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE EventType SET Title = ? WHERE EventTypeID = ?",
                (self.Title, self.EventTypeID)
            )
        conn.commit()
        conn.close()
    
    def delete(self):
        """Удаляет тип мероприятия"""
        if self.EventTypeID is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM EventType WHERE EventTypeID = ?", (self.EventTypeID,)
            )
            conn.commit()
            conn.close()

# Вспомогательные функции


def get_all_event_types():
    """Возвращает список всех типов мероприятий"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT EventTypeID, Title FROM EventType"
    )
    rows = cursor.fetchall()
    conn.close()
    return [EventType(EventTypeID=row[0], Title=row[1]) for row in rows]


def get_event_type_by_id(EventTypeID):
    """Возвращает тип мероприятия по EventTypeID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT EventTypeID, Title FROM EventType WHERE EventTypeID = ?", (EventTypeID,)
    )
    row = cursor.fetchone()
    conn.close()
    if row:
        return EventType(EventTypeID=row[0], Title=row[1])
    return None
