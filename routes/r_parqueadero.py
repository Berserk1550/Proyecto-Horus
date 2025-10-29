from conexion import *
from routes.r_usuarios import login
from models.m_parqueadero import *

@programa.route("/parqueadero")
def parqueadero():
    # lógica aquí
    return render_template("parqueadero.html")

@programa.route("/consultar_espacios")
def consultarEspacio():
        
    nit = session["parqueadero_nit"]
    
    respuesta = mi_parqueadero.consultarParqueadero(nit)
    
    return render_template("consultar_espacios.html", datos = respuesta)

@programa.route("/espacios/modificar", methods=["GET", "POST"])
def modificar_espacios():
    if request.method == "GET":
        # solo mostrar el formulario
        return render_template("agregar_espacios.html")
    
    if request.method == "POST":
        # obtener los datos enviados desde el formulario
        nit = session.get("parqueadero_nit")
        capacidad_carro_pequeno = int(request.form["capacidad_carros_pequenos"])
        capacidad_carro_grande = int(request.form["capacidad_carros_grandes"])
        capacidad_motos = int(request.form["capacidad_motos"])

        # ejecutar función que actualiza en la base de datos
        datos = mi_parqueadero.modificarEspacios(
            nit,
            capacidad_carro_pequeno,
            capacidad_carro_grande,
            capacidad_motos
        )

    return redirect("/parqueadero")
    
