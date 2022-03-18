from flask import *
from controllers.empresas import manipulacionUsuarios as USUARIOS

# from models.empresas import mensaje
app = Flask(__name__)
app.secret_key = "magdelinpai"


@app.get("/")
def home():
    # mensaje.mensaje()
    if "loggedin" in session:
        print(session["usuario"])
        return render_template("productos/empresa-producto.html")

    else:
        print("nada")
        return render_template("productos/index.html")


"""
    registro y activacion de empresa 
"""


@app.get("/registro-empresa/")
def registroEmpresa():
    return render_template("empresas/registro.html")


@app.post("/registro-empresa/")
def registroEmpresaForm():
    print("holaaa")
    nombreEmpresa = request.form.get("nombreEmpresa")
    descEmpresa = request.form.get("descEmpresa")
    celularEmpresa = request.form.get("celularEmpresa")
    direccionEmpresa = request.form.get("direccionEmpresa")
    correo = request.form.get("correo")
    contrasenia = request.form.get("contrasenia")
    USUARIOS.datosFormulario(
        nombreEmpresa,
        descEmpresa,
        celularEmpresa,
        direccionEmpresa,
        correo,
        contrasenia,
    )

    return render_template("empresas/sing.html")


@app.get("/activar-empresa/<int:id>")
def activarEmpresa(id):
    print(f"activacion {id}")

    return USUARIOS.activacion(id)


""" parte del inicio de sesion y cerrar sesion """


@app.get("/inicio-sesion/")
def inicioSesion():

    return render_template("empresas/sing.html")


@app.post("/inicio-sesion/")
def inicioSesionForm():
    correo = request.form.get("correo")
    contrasenia = request.form.get("contrasenia")
    estado, mensaje = USUARIOS.inicioSesion(correo, contrasenia)
    if(estado):
        print('Ya se inicio de sesion activa')
        return render_template("productos/empresa-producto.html")
        
    else:
        print('aun no esta iniciadaa ')
        return render_template("empresas/sing.html")


@app.get("/inicio-sesion/out")
def logout():
    USUARIOS.cerrarSesion()
    return redirect(url_for("home"))


""" manipulacion productos """


@app.get("/administracion/")
def registroProducto():
    return render_template("productos/empresa-registro-prod.html",nombre='jeison')


app.run(app.run(debug=True, host="localhost", port=1000))
