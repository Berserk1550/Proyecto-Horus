import hashlib
from conexion import conexion
from flask import session

def validar_credenciales(idusuario, contrasena):
    conexion=conexion()
    cursor=conexion.cursor(dictionary=True)

    cursor.execute("""SELECT rol, nombre, contrasena, nit FROM usuario WHERE idusuario=%s """, (idusuario,))
    