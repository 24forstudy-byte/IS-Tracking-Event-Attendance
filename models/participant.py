from database.db_manager import get_connection

class Participant:
    def __init__(self, ParticipantID=None, FullName=None, Phone=None, Mail=None):
        self.ParticipantID = ParticipantID
        self.FullName = FullName
        self.Phone = Phone
        self.Mail = Mail

    def save(self):
        """Добавляет нового участника или обновляет существующего"""
        conn = get_connection()
        cursor = conn.cursor()
        if self.ParticipantID is None:
            cursor.execute(
                "INSERT INTO Participant (FullName, Phone, Mail) VALUES (?, ?, ?)",
                (self.FullName, self.Phone, self.Mail)
            )
            self.ParticipantID = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE Participant SET FullName = ?, Phone = ?, Mail = ? WHERE ParticipantID = ?",
                (self.FullName, self.Phone, self.Mail, self.ParticipantID)
            )
        conn.commit()
        conn.close()
    
    def delete(self):
        """Удаляет участника"""
        if self.ParticipantID is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM Participant WHERE ParticipantID = ?", (self.ParticipantID,)
            )
            conn.commit()
            conn.close()

# Вспомогательные функции


def get_all_participants():
    """Возвращает список всех участников"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT ParticipantID, FullName, Phone, Mail FROM Participant"
    )
    rows = cursor.fetchall()
    conn.close()
    return [Participant(ParticipantID=row[0], FullName=row[1], Phone=row[2], Mail=row[3]) for row in rows]


def get_participant_by_id(ParticipantID):
    """Возвращает участника по ParticipantID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT ParticipantID, FullName, Phone, Mail FROM Participant WHERE ParticipantID = ?", (ParticipantID,)
    )
    row = cursor.fetchone()
    conn.close()
    if row:
        return Participant(ParticipantID=row[0], FullName=row[1], Phone=row[2], Mail=row[3])
    return None
