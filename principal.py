from conexion import *
from routes import r_parqueadero, r_usuarios


@programa.route("/")
def raiz():
    return render_template("index.html")

@programa.route("/opciones")
def opciones():
    if session.get("login")==True:
        nom = session.get("nombre")
        rol = session.get("rol")
        return render_template("opciones.html", nom=nom, rol=rol)
    else:
        return redirect("/")
    



if __name__=="__main__":
    programa.run(debug=True, port=5080)
