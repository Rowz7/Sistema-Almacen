from db_config import create_connection

def mostrar_productos():
    connection = create_connection()  
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Productos")
        productos = cursor.fetchall()
        print("Productos disponibles:")
        for producto in productos:
            print(producto)
        cursor.close()
        connection.close()

if __name__ == "__main__":
    mostrar_productos()
