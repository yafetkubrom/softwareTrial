from flask import Flask, render_template, request
import sqlite3
from sqlite3 import Error

def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except Error as e:
        print(e)
    return conn

app = Flask(__name__)

foods = []
@app.route("/")
def index():
    database = "restaurant.db"
    conn = create_connection(database)
    sql = ''' SELECT name from foods '''
    cur = conn.cursor()
    cur.execute(sql)
    
    foods=[rows[0] for rows in cur.fetchall()]
    return render_template("index.html", foods=foods)

@app.route("/menu", methods=["POST"])
def menu():
    return render_template("menu.html")

@app.route("/deals", methods=["POST"])
def deals():
    return render_template("deals.html")

@app.route("/signin", methods=["POST"])
def signin():
    return render_template("signin.html")
