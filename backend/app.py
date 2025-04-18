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
                outros TEXT,
                obs TEXT
            )
        """)
        conn.commit()

# Serve index.html automaticamente na raiz
@app.route("/")
@app.route('/')
def index():
    caminho = os.path.abspath("../frontend/index.html")
    print(f"===> SERVINDO ARQUIVO EM: {caminho}")
    return send_from_directory(os.path.abspath("../frontend"), "index.html")


# Serve style.css na raiz
@app.route("/style.css")
def style():
    return send_from_directory(app.static_folder, "style.css")

# Envio do formulário
@app.route("/enviar", methods=["POST"])
def enviar_checklist():
    data = request.get_json()
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO checklists (
                projeto, gerente, art_scan, bateria, bateria_qtd,
                spars, tooltray, tooltray_metros, pushpull, outros, obs
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            data.get("projeto"),
            data.get("gerente"),
            data.get("art_scan"),
            data.get("bateria"),
            data.get("bateria_qtd"),
            data.get("spars"),
            data.get("tooltray"),
            data.get("tooltray_metros"),
            data.get("pushpull"),
            data.get("outros"),
            data.get("obs")
        ))
        conn.commit()
    return jsonify({"status": "sucesso", "mensagem": "Checklist salvo com sucesso."})

# Consulta
@app.route("/listar", methods=["GET"])
def listar_checklists():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM checklists ORDER BY id DESC")
        rows = cursor.fetchall()

        result = []
        for row in rows:
            result.append({
                "id": row[0],
                "projeto": row[1],
                "gerente": row[2],
                "art_scan": row[3],
                "bateria": row[4],
                "bateria_qtd": row[5],
                "spars": row[6],
                "tooltray": row[7],
                "tooltray_metros": row[8],
                "pushpull": row[9],
                "outros": row[10],
                "obs": row[11]
            })
    return jsonify(result)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
