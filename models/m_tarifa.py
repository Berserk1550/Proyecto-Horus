from conexion import *

class Tarifas:

    def consultarTarifas(self, nit):
        sql= "SELECT tipo_tarifa, horario, tipo_vehiculo, hora_inicio, hora_fin FROM tarifas WHERE parqueadero_nit = %s"
        
        mi_cursor.execute(sql,(nit,))
        resultado = mi_cursor.fetchall()
        return resultado

    def crearTarifas(self,nit, tipo_tarifa, horario, tipo_vehiculo, valor_tarifa, hora_inicio, hora_fin):
        sql = """
            INSERT INTO tarifas (parqueadero_nit, tipo_tarifa, horario, tipo_vehiculo, valor_tarifa, hora_inicio, hora_fin)
            VALUES (%s,%s, %s, %s, %s, %s, %s)
        """
        valores = (nit, tipo_tarifa, horario, tipo_vehiculo, valor_tarifa, hora_inicio, hora_fin)
        
        mi_cursor.execute(sql, valores)
        mi_db.commit()
        mi_cursor.close()
        
mi_tarifa = Tarifas()