from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing/demo purposes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    conn = sqlite3.connect('campaigns.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/campaigns")
def read_campaigns(status: str = None):
    conn = get_db_connection()
    query = "SELECT * FROM campaigns"
    params = ()
    if status:
        query += " WHERE status=?"
        params = (status.capitalize(),)
    cursor = conn.execute(query, params)
    items = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return items
