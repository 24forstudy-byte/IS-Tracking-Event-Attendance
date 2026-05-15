from database.db_manager import get_connection

class Application:
    def __init__(self, ApplicationID=None, ParticipantID=None, EventID=None, StaffID=None, DateTime=None):
        self.ApplicationID = ApplicationID
        self.ParticipantID = ParticipantID
        self.EventID = EventID
        self.StaffID = StaffID
        self.DateTime = DateTime

    def register(self):
        """Регистрирует заявку"""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                        INSERT INTO Application (ParticipantID, EventID, StaffID, DateTime)
                        VALUES (?, ?, ?, ?)
                         """, (self.ParticipantID, self.EventID, self.StaffID, self.DateTime))
        self.ApplicationID = cursor.lastrowid
        conn.commit()
        conn.close()

    # Вспомогательные функции


def get_all_applications():
    """Возвращает все заявки"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT ApplicationID, ParticipantID, EventID, StaffID, DateTime FROM Application
                    """)
    rows = cursor.fetchall()
    conn.close()
    return [
        Application (
            ApplicationID=row[0], ParticipantID=row[1], EventID=row[2], StaffID=row[3], DateTime=row[4]
        )
        for row in rows
    ]
    

def get_application_by_id(ApplicationID):
    """Возвращает заявку по ApplicationID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
                    SELECT ApplicationID, ParticipantID, EventID, StaffID, DateTime FROM Application
                    WHERE ApplicationID = ?
                    """, (ApplicationID,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return Application(
            ApplicationID=row[0], ParticipantID=row[1], EventID=row[2], StaffID=row[3], DateTime=row[4]
        )
    return None
