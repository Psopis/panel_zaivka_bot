import sqlite3


def create_db():
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    userid TEXT NOT NULL,
    username TEXT NOT NULL,
    role_ TEXT NOT NULL,
    profit INT
    
    )
    ''')

    connection.commit()
    connection.close()


def add_user(user_id, username):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (userid, role_, username) VALUES (?, ?, ?)', (str(user_id), 'member', username))
    connection.commit()
    connection.close()


def get_id_from_name(user):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM USERS WHERE username = (?)', (str(user)))
    user_id = cursor.fetchone()
    connection.close()
    return user_id


def role_update(username, role):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Users set  role_ = ? WHERE username = ?', (role, str(username)))
    connection.commit()
    connection.close()


def check_user(user_id):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT userid FROM USERS WHERE userid = {str(user_id)}")
    user = cursor.fetchone()
    connection.close()
    return user


def check_admin(user_id):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT role_ FROM USERS WHERE userid = {str(user_id)}")
    user = cursor.fetchone()
    connection.close()
    return user


def profit_update(username, profit):
    connection = sqlite3.connect('Users.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE Users set profit = ? WHERE username = ?', (int(profit), str(username)))

    connection.commit()
    connection.close()
