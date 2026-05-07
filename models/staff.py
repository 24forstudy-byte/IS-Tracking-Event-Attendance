from database.db_manager import get_connection

class Staff:
    def __init__ (self, StaffID=None, FullName=None, Phone=None, Mail=None):
        self.StaffID = StaffID
        self.FullName = FullName
        self.Phone = Phone
        self.Mail = Mail

    def save(self):
        """Добавляет новый персонал или обновляет существующий"""
        conn = get_connection()
        cursor = conn.cursor()
        if self.StaffID is None:
            cursor.execute(
                "INSERT INTO Staff (FullName, Phone, Mail) VALUES (?, ?, ?)",
                (self.FullName, self.Phone, self.Mail)
            )
            self.StaffID = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE Staff SET FullName = ?, Phone = ?, Mail = ? WHERE StaffID = ?",
                (self.FullName, self.Phone, self.Mail, self.StaffID)
            )
        conn.commit()
        conn.close()
    
    def delete(self):
        """Удаляет персонал"""
        if self.StaffID is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM Staff WHERE StaffID = ?", (self.StaffID,)
            )
            conn.commit()
            conn.close()

# Вспомогательные функции

def get_all_staffs():
    """Возвращает список всего персонала"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT StaffID, FullName, Phone, Mail FROM Staff"
    )
    rows = cursor.fetchall()
    conn.close()
    return [Staff(StaffID=row[0], FullName=row[1], Phone=row[2], Mail=row[3]) for row in rows]

def get_staff_by_id(StaffID):
    """Возвращает персонал по StaffID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT StaffID, FullName, Phone, Mail FROM Staff WHERE StaffID = ?", (StaffID,)
    )
    row = cursor.fetchone()
    conn.close()
    if row:
        return Staff(StaffID=row[0], FullName=row[1], Phone=row[2], Mail=row[3])
    return None
