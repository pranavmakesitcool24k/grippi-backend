import sqlite3

def create_table():
    conn = sqlite3.connect('campaigns.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS campaigns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        status TEXT NOT NULL,
        clicks INTEGER,
        cost REAL,
        impressions INTEGER
    );
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()
