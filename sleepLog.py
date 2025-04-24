import sqlite3
from datetime import datetime

def createDb():
    conn = sqlite3.connect("sleep_data.db")
    c = conn.cursor()
    
    c.execute("DROP TABLE IF EXISTS sleep_log")
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS sleep_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            date TEXT,
            duration REAL
        )
    ''')
    conn.commit()
    conn.close()

def logSleep(userName, duration):
    conn = sqlite3.connect("sleep_data.db")
    c = conn.cursor()
    date = datetime.now().strftime("%Y-%m-%d")
    c.execute("INSERT INTO sleep_log (username, date, duration) VALUES (?, ?, ?)",
              (userName, date, duration))
    conn.commit()
    conn.close()
    print(f"Logged {duration} hours for {date}.")

def getLastSleep(userName):
    conn = sqlite3.connect("sleep_data.db")
    c = conn.cursor()
    c.execute("SELECT duration FROM sleep_log WHERE username = ? ORDER BY id DESC LIMIT 1", (userName,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0
