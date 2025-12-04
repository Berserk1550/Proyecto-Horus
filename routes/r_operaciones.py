from conexion import *
from models.m_operaciones import mi_operacion

@programa.route("/operaciones", methods=['GET'])
def operaciones():
    if not session.get("login"):
        return redirect('/')
    parqueadero_nit = session.get("parqueadero_nit")
    activos = mi_operacion.vehiculos_activos(parqueadero_nit)
    registros = mi_operacion.registros_previos(parqueadero_nit)

    conteo_carros = len([v for v in activos if v('tipo_vehiculo') == 'carro'])
    conteo_motos = len([v for v in activos if v('tipo_vehiculo') == 'moto'])
    return render_template("operaciones.html", activos=activos, registros=registros, conteo_carros=conteo_carros, conteo_motos=conteo_motos)

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
def salida():
    if not session.get("login"):
        return redirect('/')
    vehiculo_placa = request.form['vehiculo_placa']
    mi_operacion.salida(vehiculo_placa)
    return redirect("/operaciones/vehiculos_activos")

@programa.route("/operaciones/vehiculos_activos", methods=['GET'])
def vehiculos_activos():
    if not session.get("login"):
        return redirect('/')
    parqueadero_nit = session.get("parqueadero_nit")
    operaciones = mi_operacion.vehiculos_activos(parqueadero_nit)
    return render_template("operaciones_activos.html", operaciones=operaciones)

@programa.route("/operaciones/registros_previos", methods=['GET'])
def registros_previos():
    if not session.get("login"):
        return redirect('/')
    parqueadero_nit = session.get("parqueadero_nit")
    operaciones = mi_operacion.registros_previos(parqueadero_nit)
    return render_template("operaciones_historico.html", operaciones=operaciones)