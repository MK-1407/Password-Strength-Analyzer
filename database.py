import sqlite3
from sqlite3 import connect
import hashlib

create_table_sql = """
CREATE TABLE IF NOT EXISTS PASSWORDS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    password_hash TEXT NOT NULL UNIQUE
);
"""

def _create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = connect(db_file)
        return conn
    except Exception as e:
        print(e)

    return conn

def _create_table(conn: sqlite3.Connection, create_table_sql: str):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)

def check_previous_password(password):
    conn = _create_connection("passwords.db")
    _create_table(conn, create_table_sql)
    
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    cur = conn.cursor()
    cur.execute(
    "SELECT 1 FROM PASSWORDS WHERE password_hash = ?",
    (password_hash,)
)
    if cur.fetchone() is None:
        print("Password Never Used before")
        cur.execute(
            f"INSERT INTO PASSWORDS(password_hash) VALUES('{password_hash}')"
        )
        conn.commit()
    else:
        print("This Password has already been used once")
    