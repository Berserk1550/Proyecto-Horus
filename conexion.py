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
    database="horus"
)

programa.secret_key = "una_clave_super_secreta_y_unica_123"

# Cursor con resultados en formato diccionario
mi_cursor = conexion.cursor(dictionary=True)
