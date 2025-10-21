from conexion import *
from models.m_usuarios import mi_usuario

#este metodo se encarga de dar ingreso al programa al usuaurio
@programa.route("/login", methods = ['POST'])
def login():
    id = request.form['idusuario']
    contra = request.form['contrausuario']
    resultado = mi_usuario.loguear(id,contra)
    if len(resultado)==0: #<--- si el tamaño de la respuesta es 0 == usuario no existente 
        return render_template("inicio_sesion.html",msg="Credenciales incorrectas")
    else:
        session["login"] = True #<--- si resultado != 0 usuario es existente y se asignan variables de sesion 
        session["nombre"] = resultado[0][1]
        session["rol"]=resultado[0][3]
        return redirect("/opciones")