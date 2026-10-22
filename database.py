import mysql.connector
import os

def get_connection():
    conn=mysql.connector.connect(
        host="localhost",
        user=os.getenv("MYSQL_USER","root"),
        password=os.getenv("MYSQL_PASSWORD")
        database="Placement_db"
    )
    return conn
    