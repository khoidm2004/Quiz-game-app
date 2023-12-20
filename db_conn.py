from pathlib import Path
import sqlite3

DB_FILEPATH = Path().joinpath("game.db")
DB_CONN = sqlite3.connect(DB_FILEPATH)
