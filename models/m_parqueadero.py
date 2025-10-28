from conexion import *

class Parqueadero:

    def consultarParqueadero(self,nit):
        sql = "SELECT capacidad_carros_pequenos, capacidad_carros_grandes, capacidad_motos WHERE nit = %s AND estado = %s"
        mi_cursor.execute(sql(nit))
        resultado = mi_cursor.fetchall()
        return resultado
    
    def modificarEspacios(self,capacidad_carro_pqnos,capacidad_carro_grdes,capacidad_motos):
        sql = "UPDATE parqueadero SET capacidad_carros_pequenos =%s capacidad_carros_grandes = %s capacidacidad_motos %s"
        mi_cursor.execute(sql(capacidad_carro_pqnos,capacidad_carro_grdes,capacidad_motos))
        mi_db.commit()


mi_parqueadero = Parqueadero()