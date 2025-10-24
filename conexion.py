import mysql.connector
from flask import Flask, redirect, render_template, request, send_from_directory, session
import hashlib

# Nombre del programa
programa = Flask(__name__)

# Conexión directa a la base de datos 'horus'
conexion = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="bd_parqueo"
)

programa.secret_key = "super_segura"

# Cursor con resultados en formato diccionario
mi_cursor = conexion.cursor(dictionary=True)
