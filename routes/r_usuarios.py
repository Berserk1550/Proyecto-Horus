from conexion import *
from models.m_usuarios import mi_usuario

#este metodo se encarga de dar ingreso al programa al usuaurio
@programa.route("/login", methods = ['POST'])
def login():
    id = request.form['idusuario']
    contra = request.form['contra']
    resultado = mi_usuario.loguear(id,contra)
    if len(resultado)==0: #<--- si el tamaño de la respuesta es 0 == usuario no existente 
        return render_template("index.html",msg="Credenciales incorrectas")
    else:
        usuario = resultado[0]
        session["login"] = True
        session["nombre"] = usuario["nombre"]
        session["rol"] = usuario["tipo"]
        session["activo"] = usuario["activo"]
        return redirect ("/opciones")