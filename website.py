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
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type ='table';")
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
    conn = dbConnection()
    table_names = get_table_names(conn)

    if not table_names:
        return "No tables found in the database."

    table_name = table_names[0]

    query = f'SELECT * FROM {table_name} WHERE Category = "Nonfiction"'
    nonfiction_data = conn.execute(query).fetchall()

    return render_template("non_fiction.html", nonfiction_data = nonfiction_data, table_name = table_name)

@app.route('/seq_art')
def SeqArt():
    conn = dbConnection()
    table_names = get_table_names(conn)

    if not table_names:
        return "No tables found in the database."

    table_name = table_names[0]

    query = f'SELECT * FROM {table_name} WHERE Category = "Sequential Art"'
    seqart_data = conn.execute(query).fetchall()

    return render_template("seq_art.html", seqart_data = seqart_data, table_name = table_name)

@app.route('/fiction')
def Fiction():
    conn = dbConnection()
    table_names = get_table_names(conn)

    if not table_names:
        return "No tables found in the database"
    
    table_name = table_names[0]

    query = f'SELECT * FROM {table_name} WHERE Category = "Fiction"'
    fiction_data = conn.execute(query).fetchall()

    return render_template("fiction.html", fiction_data = fiction_data, table_name = table_name)

@app.route('/young_adult')
def YoungAdult():
    conn = dbConnection()
    table_names = get_table_names(conn)

    if not table_names:
        return "No tables found in the database."

    table_name = table_names[0]

    query = f'SELECT * FROM {table_name} WHERE Category = "Young Adult"'
    young_data = conn.execute(query).fetchall()

    return render_template("young_adult.html", young_data = young_data, table_name = table_name)

@app.route('/fantasy')
def Fantasy():
    conn = dbConnection()
    table_names = get_table_names(conn)

    if not table_names:
        return "No tables found in the database."

    table_name = table_names[0]

    query = f'SELECT * FROM {table_name} WHERE Category = "Fantasy"'
    fantasy_data = conn.execute(query).fetchall()

    return render_template("fantasy.html", fantasy_data = fantasy_data, table_name = table_name)

@app.route('/romance')
def Romance():
    conn = dbConnection()
    table_names = get_table_names(conn)

    if not table_names:
        return "No tables found in the database."

    table_name = table_names[0]

    query = f'SELECT * FROM {table_name} WHERE Category = "Romance"'
    romance_data = conn.execute(query).fetchall()

    return render_template("romance.html", romance_data = romance_data, table_name = table_name)

@app.route('/mystery')
def Mystery():
    conn = dbConnection()
    table_names = get_table_names(conn)

    if not table_names:
        return "No tables found in the database."

    table_name = table_names[0]

    query = f'SELECT * FROM {table_name} WHERE Category = "Mystery"'
    mystery_data = conn.execute(query).fetchall()

    return render_template("mystery.html", mystery_data = mystery_data, table_name = table_name)

@app.route('/food_and_drink')
def FoodAndDrink():
    conn = dbConnection()
    table_names = get_table_names(conn)

    if not table_names:
        return "No tables found in the database."

    table_name = table_names[0]

    query = f'SELECT * FROM {table_name} WHERE Category = "Food and Drink"'
    food_and_drink_data = conn.execute(query).fetchall()

    return render_template("food_and_drink.html", food_and_drink_data = food_and_drink_data, table_name = table_name)

if __name__ == '__main__':
    app.run(debug = True)