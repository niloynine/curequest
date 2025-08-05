import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost:3307',
        user='root',
        password='root',
        database='curequest'
    )
