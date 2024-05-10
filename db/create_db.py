import sqlite3 as sql


connection = sql.connect('./db/User_db.db')
cursor = connection.cursor()

cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            full_name TEXT,
            balance INTEGER,
            ton_link TEXT,
            invitations INTEGER
        )
        ''')

connection.commit()