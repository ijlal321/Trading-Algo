import sqlite3
import datetime

DB_PATH = "db.sqlite"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()

def store_price(price):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO prices (timestamp, price) VALUES (?, ?)", (datetime.datetime.now(), price))
    conn.commit()
    conn.close()
