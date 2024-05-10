import sqlite3 as sql


def add_new_user(user_id, user_fullname):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (id, full_name, balance, num_invitations) VALUES (?,?,?,?)', (user_id, user_fullname, 0, 0))
    connection.commit()
    

def add_shells(user_id, shells):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Users SET balance = balance + ? WHERE id = ?', (shells, user_id))
    connection.commit()

    
def add_invitation(user_id):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Users SET num_invitations = num_invitations + 1 WHERE id = ?', (user_id,s))
    connection.commit()


def get_balance(user_id):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute("SELECT balance FROM Users WHERE id =?", (user_id,))
    user_balance = cursor.fetchone()
    connection.commit()
    user_balance = str(user_balance).replace('(', '').replace(')', '').replace(',', '')
    return user_balance


def get_invitation(user_id):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute("SELECT num_invitations FROM Users WHERE id =?", (user_id,))
    user_invitations = cursor.fetchone()
    connection.commit()
    user_invitations = str(user_invitations).replace('(', '').replace(')', '').replace(',', '')
    return user_invitations


def is_old(user_id):
    connection = sql.connect('./db/User_db.db')
    cursor = connection.cursor()
    cursor.execute("SELECT 1 FROM users WHERE id =?", (user_id,))
    result  = cursor.fetchone()
    connection.commit()
    return bool(result)