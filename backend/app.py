from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

DB_PATH = os.path.join(os.path.dirname(__file__), '../database/gl.db')

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
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
