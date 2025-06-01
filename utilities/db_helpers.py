import sqlite3
from typing import List, Tuple

class DatabaseHelper:
    def __init__(self, db_name="data.db"):
        self.conn = sqlite3.connect(db_name)
        self._create_tables()

    def _create_tables(self):
        query = """
        CREATE TABLE IF NOT EXISTS weather_data (
            city TEXT PRIMARY KEY,
            temperature_web REAL,
            feels_like_web REAL,
            temperature_api REAL,
            feels_like_api REAL,
            avg_temperature REAL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_weather_data(self, city: str, temp_web: float, feel_web: float,
                             temp_api: float, feel_api: float):
        avg_temp = (temp_web + temp_api) / 2
        query = """
        INSERT OR REPLACE INTO weather_data 
        (city, temperature_web, feels_like_web, temperature_api, feels_like_api, avg_temperature)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        self.conn.execute(query, (city, temp_web, feel_web, temp_api, feel_api, avg_temp))
        self.conn.commit()

    def fetch_all_data(self) -> List[Tuple]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM weather_data")
        return cursor.fetchall()