from database.db_manager import get_connection

class Place:
    def __init__ (self, PlaceID=None, Title=None, Address=None):
        self.PlaceID = PlaceID
        self.Title = Title
        self.Address = Address

    def save(self):
        """Добавляет новое место или обновляет существующий"""
        conn = get_connection()
        cursor = conn.cursor()
        if self.PlaceID is None:
            cursor.execute(
                "INSERT INTO Place (Title, Address) VALUES (?, ?)",
                (self.Title, self.Address)
            )
            self.PlaceID = cursor.lastrowid
        else:
            cursor.execute(
                "UPDATE Place SET Title = ?, Address = ? WHERE PlaceID = ?",
                (self.Title, self.Address, self.PlaceID)
            )
        conn.commit()
        conn.close()
    
    def delete(self):
        """Удаляет место"""
        if self.PlaceID is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM Place WHERE PlaceID = ?", (self.PlaceID,)
            )
            conn.commit()
            conn.close()

# Вспомогательные функции

def get_all_places():
    """Возвращает список всех мест"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT PlaceID, Title, Address FROM Place"
    )
    rows = cursor.fetchall()
    conn.close()
    return [Place(PlaceID=row[0], Title=row[1], Address=row[2]) for row in rows]

def get_place_by_id(PlaceID):
    """Возвращает место по PlaceID"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT PlaceID, Title, Address FROM Place WHERE PlaceID = ?", (PlaceID,)
    )
    row = cursor.fetchone()
    conn.close()
    if row:
        return Place(PlaceID=row[0], Title=row[1], Address=row[2])
    return None
