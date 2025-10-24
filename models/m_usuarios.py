
from conexion import *


class Usuario:
    
    def loguear(self, id, contra):
        cifrada = contra
        sql = f"SELECT nombre, tipo, activo FROM usuarios WHERE cedula='{id}' AND contrasena='{cifrada}'"
        mi_cursor.execute(sql)
        resultado=mi_cursor.fetchall()
        print(resultado)
        return resultado
    
    def ingresar_usuario(cedula,nombres, apellidos, correo, telefono, tel_emergencia, contrasena, rol):

        sentencia="INSERT INTO usuarios (cedula,nombres, apellidos, correo, telefono, tel_emergencia, contrasena, rol, parqueadero_nit) VALUES (%S,%S,%S,%S,%S,%S,%S,%S,%S)"
        mi_cursor.execute(sentencia,(cedula,nombres, apellidos, correo, telefono, tel_emergencia, contrasena, rol, parqueadero_nit))
        mi_cursor.commit()
        mi_cursor.close()
        conexion.close()
    
    
    

mi_usuario = Usuario() 