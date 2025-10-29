from conexion import *

class Parqueadero:

    def consultarParqueadero(self,nit):
        sql = "SELECT capacidad_carros_pequenos, capacidad_carros_grandes, capacidad_motos WHERE nit = %s AND estado = %s"
        mi_cursor.execute(sql(nit))
        resultado = mi_cursor.fetchall()
        return resultado
    
    def modificarEspacios(self,nit,capacidad_carro_pqnos,capacidad_carro_grdes,capacidad_motos):
        
        sql = "UPDATE parqueadero SET capacidad_carros_pequenos =%s, capacidad_carros_grandes = %s, capacidad_motos = %s WHERE nit = %s"
        
        mi_cursor.execute(sql, (capacidad_carro_pqnos, capacidad_carro_grdes, capacidad_motos, nit))
        mi_db.commit()
        
        if capacidad_carro_pqnos != 0:
            
            for i in range(capacidad_carro_pqnos):
                sql = "INSERT INTO espacios (parqueadero_nit, tipo, dimension, ocupado) VALUES (%s, %s, %s, %s)"
                mi_cursor.execute(sql, (nit, 'carro', 'pequeno', 'disponible'))
                
        if capacidad_carro_grdes != 0:
            for _ in range(capacidad_carro_grdes):
                sql = "INSERT INTO espacios (parqueadero_nit, tipo, dimension, ocupado) VALUES (%s, %s, %s, %s)"
                mi_cursor.execute(sql, (nit, 'carro', 'grande', 'disponible'))
                        
        if capacidad_motos != 0:
                            
            for _ in range(capacidad_motos):
                sql = "INSERT INTO espacios (parqueadero_nit, tipo, dimension, ocupado) VALUES (%s, %s, %s, %s)"
                mi_cursor.execute(sql, (nit, 'moto', 'pequeno', 'disponible'))
        mi_db.commit()
        
    
    


mi_parqueadero = Parqueadero()