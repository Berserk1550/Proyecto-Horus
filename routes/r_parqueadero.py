from conexion import *  # Importa la conexión y el cursor de la base de datos
from routes.r_usuarios import login  # Importa el módulo de login (no usado directamente aquí)
from models.m_parqueadero import *  # Importa la clase Parqueadero y su instancia

# -----------------------------------------
# RUTA PRINCIPAL DEL PARQUEADERO
# -----------------------------------------
@programa.route("/parqueadero")
def parqueadero():
    # Renderiza la plantilla HTML principal del parqueadero
    return render_template("parqueadero.html")

# -----------------------------------------
# RUTA PARA CONSULTAR ESPACIOS
# -----------------------------------------
@programa.route("/consultar_espacios")
def consultarEspacio():
    
    
    # Obtiene el NIT del parqueadero desde la sesión
    nit = session["parqueadero_nit"]
    
    # Llama a la función que consulta las capacidades del parqueadero en la base de datos
    respuesta = mi_parqueadero.consultarParqueadero(nit)
    
    # Renderiza la plantilla HTML con los datos obtenidos
    return render_template("consultar_espacios.html", datos=respuesta)

# -----------------------------------------
# RUTA PARA MODIFICAR/AGREGAR ESPACIOS
# -----------------------------------------
@programa.route("/espacios/modificar", methods=["GET", "POST"])
def modificar_espacios():
    if session.get("login") == True:
        if request.method == "GET":
            # Si es GET, solo muestra el formulario para agregar o modificar espacios
            return render_template("agregar_espacios.html")
        
        if request.method == "POST":
            # Si es POST, significa que se enviaron los datos del formulario
            
            # Obtiene el NIT del parqueadero desde la sesión
            nit = session.get("parqueadero_nit")
            
            # Obtiene las capacidades enviadas por el formulario y las convierte a enteros
            capacidad_carro_pequeno = int(request.form["capacidad_carros_pequenos"])
            capacidad_carro_grande = int(request.form["capacidad_carros_grandes"])
            capacidad_motos = int(request.form["capacidad_motos"])

            # Llama a la función que actualiza las capacidades en la base de datos
            datos = mi_parqueadero.modificarEspacios(
                nit,
                capacidad_carro_pequeno,
                capacidad_carro_grande,
                capacidad_motos
            )

        # Redirige de nuevo a la página principal del parqueadero después de modificar
        return redirect("/parqueadero")
    else:
        return redirect("/")
