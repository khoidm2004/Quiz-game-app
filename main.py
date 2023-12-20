from db_conn import DB_CONN
from menu import Menu

LEADERBOARD_TABLE_STATEMENT = """
CREATE TABLE IF NOT EXISTS leaderboard(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    score NUMBER NOT NULL
);
"""
class Main:
    def __init__(self) -> None:
        self.initDatabase()
        menu = Menu()
        menu.display_menu()
        DB_CONN.commit()
    def initDatabase(self)->None:
        cursor = DB_CONN.cursor()
        cursor.execute(LEADERBOARD_TABLE_STATEMENT)
        DB_CONN.commit()
        cursor.close()

if __name__ == "__main__":
    app = Main()
