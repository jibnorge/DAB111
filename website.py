from flask import Flask, render_template
import sqlite3
import os

def get_database_path(database_filename):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    database_path = os.path.join(current_directory, database_filename)
    return database_path

app = Flask(__name__)

database_filename = "books.db"
database_path = get_database_path(database_filename)

def dbConnection():
    try:
        conn = sqlite3.connect(database_path)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print("SQLite Error:", e)
        return None

def get_table_names(conn):
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [table[0] for table in cursor.fetchall()]

@app.route('/')
def createMain():
    conn = dbConnection()
    table_names = get_table_names(conn)

    if not table_names:
        return "No tables found in the database."

    table_name = table_names[0]

    query = f'SELECT * FROM {table_name}'
    book_data = conn.execute(query).fetchall()

    return render_template("index.html", book_data = book_data, table_name = table_name)

@app.route('/about')
def about():
    conn = dbConnection()
    table_names = get_table_names(conn)

    if not table_names:
        return "No tables found in the database."

    table_name = table_names[1]

    query = f'SELECT * FROM {table_name}'
    feature_data = conn.execute(query).fetchall()

    return render_template("about.html", feature_data = feature_data, table_name = table_name)

@app.route('/non_fiction')
def NonFiction():
    # conn = dbConnection()
    # table_names = get_table_names(conn)

    # if not table_names:
    #     return "No tables found in the database."

    # table_name = table_names[1]

    # query = f'SELECT * FROM {table_name}'
    # feature_data = conn.execute(query).fetchall()

    return render_template("non_fiction.html")

if __name__ == '__main__':
    app.run(debug=True)