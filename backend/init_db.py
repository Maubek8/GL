import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '../database/gl.db')

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS checklists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        projeto TEXT,
        gerente TEXT,
        art_scan TEXT,
        bateria TEXT,
        bateria_qtd INTEGER,
        spars TEXT,
        tooltray TEXT,
        tooltray_metros INTEGER,
        pushpull INTEGER,
        outros TEXT,
        obs TEXT
    )
""")

conn.commit()
conn.close()
print("Banco de dados criado com sucesso.")
