import sqlite3

def db_connect():
    try:
        conn = sqlite3.connect("inventory.db", check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute(""" 
            CREATE TABLE IF NOT EXISTS inventory (
                name TEXT PRIMARY KEY,
                quantity INT
            )
        """)
        conn.commit()
        return conn, cursor
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return None, None
