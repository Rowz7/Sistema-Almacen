import mysql.connector
from mysql.connector import Error

def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="rowz",
            password="qwerty",
            database="inventario"
        )
        if connection.is_connected():
            print("Conexión exitosa a la base de datos.")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None
