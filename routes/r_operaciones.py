from conexion import *
from models.m_operaciones import mi_operacion

@programa.route("/operaciones/ingreso", methods=['POST'])
def ingreso():
    if not session.get("login"):
        return redirect('/')
        vehiculo_placa = request.form['vehiculo_placa']
        usuario_cedula = session.get('usuario_cedula')
        parqueadero_nit = session.get('parqueadero_nit')
        mi_operacion.ingreso(vehiculo_placa, usuario_cedula, parqueadero_nit)
        return redirect("/operaciones/vehiculos_activos")

@programa.route("/operaciones/salida", methods=['POST'])
def saluda():
    if not session.get("login"):
        return redirect('/')
        vehiculo_placa = request.form['vehiculo_placa']
        mi_operacion.salida(vehiculo_placa)
        return redirect("/operaciones/vehiculos_activos")

@programa.route("/operaciones/vehiculos_activos", methods=['GET'])
def vehiculos_activos()