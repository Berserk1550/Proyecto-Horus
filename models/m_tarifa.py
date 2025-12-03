from conexion import *

class Tarifas:

    def consultarTarifas(self, nit):
        sql = """
            SELECT id_tarifas, tipo_tarifa, horario, tipo_vehiculo,
                valor_tarifa, hora_inicio, hora_fin
            FROM tarifas
            WHERE parqueadero_nit = %s
        """

        mi_cursor.execute(sql, (nit,))
        resultado = mi_cursor.fetchall()

        # 🔥 Convertir timedelta → "6 am" / "7 pm"
        for r in resultado:
            if isinstance(r["hora_inicio"], timedelta):
                r["hora_inicio"] = (datetime.min + r["hora_inicio"]).strftime("%I %p").lstrip("0").lower()

            if isinstance(r["hora_fin"], timedelta):
                r["hora_fin"] = (datetime.min + r["hora_fin"]).strftime("%I %p").lstrip("0").lower()

        return resultado


    def consultarTarifaPorID(self, id_tarifa):
        sql = """
            SELECT id_tarifas, tipo_tarifa, horario, tipo_vehiculo, valor_tarifa,
            hora_inicio, hora_fin
            FROM tarifas
            WHERE id_tarifas = %s
        """
        mi_cursor.execute(sql, (id_tarifa,))
        resultado = mi_cursor.fetchone()

        # Formatear hora_inicio y hora_fin a 'HH:MM' para el input type="time"
        if resultado:
            # Verifica que no sea None antes de formatear
            if resultado['hora_inicio'] != '':
                resultado['hora_inicio'] = resultado['hora_inicio']
                
            if resultado['hora_fin'] != '':
                resultado['hora_fin'] = resultado['hora_fin']
        print(resultado)
        return resultado


    def crearTarifas(self,nit, tipo_tarifa, horario, tipo_vehiculo, valor_tarifa, hora_inicio, hora_fin):
        sql = """
            INSERT INTO tarifas (parqueadero_nit, tipo_tarifa, horario, tipo_vehiculo, valor_tarifa, hora_inicio, hora_fin)
            VALUES (%s,%s, %s, %s, %s, %s, %s)
            """
        valores = (nit, tipo_tarifa, horario, tipo_vehiculo, valor_tarifa, hora_inicio, hora_fin)
            
        mi_cursor.execute(sql, valores)
        mi_db.commit()

    def existeTarifaDuplicada(self, nit, tipo_tarifa, horario, tipo_vehiculo, hora_inicio, hora_fin, id_actual):
        sql = """
            SELECT id_tarifas
            FROM tarifas
            WHERE parqueadero_nit = %s
                AND tipo_tarifa = %s
                AND horario = %s
                AND tipo_vehiculo = %s
                AND hora_inicio = %s
                AND hora_fin = %s
                AND id_tarifas <> %s
        """

        valores = (nit, tipo_tarifa, horario, tipo_vehiculo, hora_inicio, hora_fin, id_actual)

        mi_cursor.execute(sql, valores)
        resultado = mi_cursor.fetchone()
        
        print(resultado)

        return resultado is not None

    def actualizarTarifa(self, id_tarifa, nit, tipo_tarifa, horario, tipo_vehiculo, valor_tarifa, hora_inicio, hora_fin):

        # Verificar duplicados
        if self.existeTarifaDuplicada(nit, tipo_tarifa, horario, tipo_vehiculo, hora_inicio, hora_fin, id_tarifa):
            return "duplicado"

        sql = """
            UPDATE tarifas
            SET tipo_tarifa = %s,
                horario = %s,
                tipo_vehiculo = %s,
                valor_tarifa = %s,
                hora_inicio = %s,
                hora_fin = %s
            WHERE id_tarifas = %s
        """

        valores = (tipo_tarifa, horario, tipo_vehiculo, valor_tarifa, hora_inicio, hora_fin, id_tarifa)

        mi_cursor.execute(sql, valores)
        mi_db.commit()

        return "ok"

mi_tarifa = Tarifas()
