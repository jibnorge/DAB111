import pandas as pd
from sqlalchemy import create_engine
import sqlite3

df_books = pd.read_csv('books_updated.csv')

df_features = pd.read_csv('features.csv')

engine = create_engine('sqlite:///books.db')

df_books.to_sql('book_table', engine, index = False, if_exists = 'replace')

df_features.to_sql('feature_table', engine, index = False, if_exists = 'replace')