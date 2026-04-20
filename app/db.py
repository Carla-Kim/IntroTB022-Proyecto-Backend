import mysql.connector
from contextlib import contextmanager
from app.config import *

pool = mysql.connector.pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    database=DB_NAME,
    **DB_CONFIG
)

def get_connection():
    return pool.get_connection()

@contextmanager
def get_cursor():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        yield cursor
        conn.commit()
    except:
        conn.rollback()
        raise
    finally:
        cursor.close()
        conn.close()
