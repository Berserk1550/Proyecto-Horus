import mysql.connector

# Conexión directa a la base de datos 'horus'
conexion = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="horus"
)

# Cursor con resultados en formato diccionario
cursor = conexion.cursor(dictionary=True)
