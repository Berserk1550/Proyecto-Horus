from conexion import *
from routes.r_usuarios import login
from models.m_tarifa import *

@programa.route("/tarifas")
def tarifas():
    return render_template("tarifas.html")

@programa.route("/consultar_tarifas")
def consultarTarifas():
    
    nit = session["parqueadero_nit"]
    
    respuesta = mi_tarifa.consultarTarifas(nit)
    
    print(respuesta)
    
    return render_template("consultar_tarifas.html", tarifas = respuesta)

@programa.route("/crear_tarifas", methods=["GET", "POST"])
def crearTarifa():
    if request.method == "POST":
        
        nit = session["parqueadero_nit"]
        
        tarifa = request.form["tipo_tarifa"]
        horario_tarifa = request.form["horario"]
        vehiculo = request.form["tipo_vehiculo"]
        valor = request.form["valor_tarifa"]
        hora_comienzo = request.form["hora_inicio"]
        hora_final = request.form["hora_fin"]
        
        repuesta = mi_tarifa.crearTarifas(nit, tarifa, horario_tarifa, vehiculo, valor, hora_comienzo, hora_final)
        
    return render_template("crear_tarifas.html")
