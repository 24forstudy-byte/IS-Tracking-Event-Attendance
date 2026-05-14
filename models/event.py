from database.db_manager import get_connection

class Event:
    def __init__(self, EventID=None, EventTypeID=None, PlaceID=None, Title=None, DateTime=None, Status=None):
        self.EventID = EventID
        self.EventTypeID = EventTypeID
        self.PlaceID = PlaceID
        self.Title = Title
        self.DateTime = DateTime
        self.Status = Status

    def save(self):
        """Добавляет новое мероприятие или обновляет существующее"""
        conn = get_connection()
        cursor = conn.cursor()
        if self.EventID is None:
            cursor.execute("""
                           INSERT INTO Event (EventTypeID, PlaceID, Title, DateTime, Status)
                           VALUES (?, ?, ?, ?, ?)
                           """, (self.EventTypeID, self.PlaceID, self.Title, self.DateTime, self.Status))
            self.EventID = cursor.lastrowid
        else:
            cursor.execute("""
                           UPDATE Event SET EventTypeID = ?, PlaceID = ?, Title = ?, DateTime = ?, Status = ?
                           WHERE EventID = ?
                           """, (self.EventTypeID, self.PlaceID, self.Title, self.DateTime, self.Status, self.EventID))
        conn.commit()
        conn.close()
    
    def delete(self):
        """Удаляет мероприятие"""
        if self.EventID is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM Event WHERE EventID = ? 
                           """, (self.EventID,))
            conn.commit()
            conn.close()

    def archive(self):
        """Архивирует мероприятие"""
        self.Status = "Архивировано"
        self.save()

# Вспомогательные функции

def get_all_events():
    """Возвращает все мероприятия"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT EventID, EventTypeID, PlaceID, Title, DateTime, Status FROM Event
                    ORDER BY Status = "Архивировано", DateTime DESC
                    """)
    rows = cursor.fetchall()
    conn.close()
    return [
        Event (
            EventID=row[0], EventTypeID=row[1], PlaceID=row[2], Title=row[3], DateTime=row[4], Status=row[5]
        )
        for row in rows
    ]
    
def get_event_by_id(EventID):
    """Возвращает мероприятие по ID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT EventID, EventTypeID, PlaceID, Title, DateTime, Status FROM Event
                    WHERE EventID = ?
                    """, (EventID,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Event(
            EventID=row[0], EventTypeID=row[1], PlaceID=row[2], Title=row[3], DateTime=row[4], Status=row[5]
        )
    return None
                           