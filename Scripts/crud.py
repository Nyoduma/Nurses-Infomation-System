from flask import *  # This imports the entire flask module
import sqlite3 # This imports sqlite3

app = Flask(__name__,template_folder='templates')
@app.route('/')
def index():
    return render_template("index.html");

@app.route('/add')
def add():
    return render_template("add.html")