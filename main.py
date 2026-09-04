from fastapi import FastAPI
from fastapi.responses import FileResponse
import mysql.connector
from fastapi.middleware.cors import CORSMiddleware
import base64

app = FastAPI()

def get_db():
    return mysql.connector.connect(
    host="localhost",
    user="root",
    password="prithivi@2407",
    database="games"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5500","http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def home():
    return FileResponse("index.html")

@app.get("/games")
def index():

    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("select * from game")
    games = cursor.fetchall()

    cursor.close()
    db.close()

    return games