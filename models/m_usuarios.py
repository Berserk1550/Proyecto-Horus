import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from conexion import *

import hashlib

class Usuario:
    
    def loguear(self, cedula, contrasena):
        #cifrada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()
        cifrada=contrasena
        sql = """SELECT nombres, apellidos, rol, activo, parqueadero_nit FROM usuarios WHERE cedula = %s AND contrasena = %s"""
        mi_cursor.execute(sql, (cedula, cifrada))
        resultado = mi_cursor.fetchall()
        return resultado

    def ingresar_usuario(self, cedula, nombres, apellidos, correo, telefono, tel_emergencia, contrasena, rol, parqueadero_nit, fecha_registro):
        contrasena_cifrada = hashlib.sha512(contrasena.encode("utf-8")).hexdigest()
        sql="INSERT INTO usuarios (cedula, nombres, apellidos, correo, telefono, tel_emergencia, contrasena, rol, parqueadero_nit, fecha_registro) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mi_cursor.execute(sql,(cedula, nombres, apellidos, correo, telefono, tel_emergencia, contrasena, rol, parqueadero_nit, fecha_registro))
        mi_db.commit()
    

mi_usuario = Usuario()

#if __name__ == "__main__":
#    print("Importación exitosa. Conexión establecida.")
