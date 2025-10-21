
from conexion import *


class Usuario:
    
    def loguear(self, id, contra):
        cifrada = contra
        sql = f"SELECT nombre, tipo, activo FROM usuarios WHERE cedula='{id}' AND contrasena='{cifrada}'"
        mi_cursor.execute(sql)
        resultado=mi_cursor.fetchall()
        print(resultado)
        return resultado
    
    
    
    

mi_usuario = Usuario() 