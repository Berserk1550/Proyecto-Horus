from conexion import obtener_cursor

def validar_usuario(correo, contrasena):
    cursor = obtener_cursor()
    cursor.execute(
        (correo, contrasena)
    )
    return cursor.fetchone