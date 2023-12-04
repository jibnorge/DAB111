import pandas as pd
from sqlalchemy import create_engine
import sqlite3

df = pd.read_csv('books_updated.csv')

engine = create_engine('sqlite:///books.db')

df.to_sql('table_name', engine, index = False, if_exists = 'replace')