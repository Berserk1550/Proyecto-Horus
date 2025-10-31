from conexion import *

class Parqueadero:

    def consultarEspacios(self, nit):
        sql = "SELECT  tipo, dimension, ocupado FROM espacios WHERE parqueadero_nit = %s"
        mi_cursor.execute(sql, (nit,))  
        resultado = mi_cursor.fetchall()
        print(f"espacios recogidos = ${resultado}")
        return resultado

    
    def modificarEspacios(self,nit,capacidad_carro_pqnos,capacidad_carro_grdes,capacidad_motos):
        # Define el SQL para actualizar las capacidades del parqueadero
        sql = "UPDATE parqueadero SET capacidad_carros_pequenos =%s, capacidad_carros_grandes = %s, capacidad_motos =%s WHERE nit = %s"
        
        # Ejecuta el UPDATE en la base de datos con los valores recibidos
        mi_cursor.execute(sql, (capacidad_carro_pqnos, capacidad_carro_grdes, capacidad_motos, nit))
        # Confirma los cambios en la base de datos
        mi_db.commit()
        
        # Si la capacidad de carros pequeños no es cero, inserta registros en la tabla espacios
        if capacidad_carro_pqnos != 0:
            for i in range(capacidad_carro_pqnos):
                # SQL para insertar un espacio
                sql = "INSERT INTO espacios (parqueadero_nit, tipo, dimension, ocupado) VALUES (%s, %s, %s, %s)"
                # Ejecuta el INSERT con los valores para carros pequeños
                mi_cursor.execute(sql, (nit, 'carro', 'pequeno', 'disponible'))
                
        # Si la capacidad de carros grandes no es cero, inserta registros en la tabla espacios
        if capacidad_carro_grdes != 0:
            for _ in range(capacidad_carro_grdes):
                sql = "INSERT INTO espacios (parqueadero_nit, tipo, dimension, ocupado) VALUES (%s, %s, %s, %s)"
                mi_cursor.execute(sql, (nit, 'carro', 'grande', 'disponible'))
                        
        # Si la capacidad de motos no es cero, inserta registros en la tabla espacios
        if capacidad_motos != 0:
            for _ in range(capacidad_motos):
                sql = "INSERT INTO espacios (parqueadero_nit, tipo, dimension, ocupado) VALUES (%s, %s, %s, %s)"
                mi_cursor.execute(sql, (nit, 'moto', 'pequeno', 'disponible'))
        
        # Confirma todos los inserts en la base de datos
        mi_db.commit()

mi_parqueadero = Parqueadero()