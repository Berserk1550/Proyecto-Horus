from datetime import datetime
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
        if usuario["activo"] != "inactivo": #<-- se valida si el usuario esta activo
            session["login"] = True
            session["nombres"] = usuario["nombres"]
            session["rol"] = usuario["rol"]
            session["activo"] = usuario["activo"]
            session["parqueadero_nit"] = usuario["parqueadero_nit"]
            return redirect ("/opciones")
        else:
            return render_template("index.html",msg="El usuario no esta activo") #<-- si el usuario no esta activo se devuelve un mesensaje informando

@programa.route('/admin/agregar_usuario', methods=['GET', 'POST'])
def crear_usuario():                            #iniciamos registro del usuario/portero a traves de un admin
    if not session.get("login") or session.get("rol") != "admin":
        return redirect('/')
    
    mensaje=None
    if request.method=='POST':
        cedula=request.form['cedula']
        nombres=request.form['nombres']
        apellidos=request.form['apellidos']
        correo=request.form['correo']
        telefono=request.form['telefono']
        tel_emergencia=request.form['tel_emergencia']
        contrasena=request.form['contrasena']
        rol=request.form['rol']
        parqueadero_nit = session.get("parqueadero_nit")
        fecha_registro = datetime.today().strftime('%Y-%m-%d')


        mi_usuario.ingresar_usuario(cedula, nombres, apellidos, correo, telefono, tel_emergencia, contrasena, rol, parqueadero_nit, fecha_registro)
        return redirect("/opciones")
    return render_template("reg_portero.html")  # ← muestra el formulario si no se ha enviado # si no es POST, es GET → mostrar el formulario
