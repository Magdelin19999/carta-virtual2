from flask import *
from controllers.empresas import manipulacionUsuarios as USUARIOS

# from models.empresas import mensaje
app = Flask(__name__)
app.secret_key = "magdelinpai"


@app.get("/")
def home():
    return render_template("productos/index.html")


@app.get("/registro-empresa")
def registroEmpresa():
    return render_template("empresas/registro.html")


@app.post("/registro-empresa/")
def registroEmpresaForm():
    ''' 
    form = request.form
    print('data formulario')
    print(form)
    #imagen = request.files.get('inputImagen')

    #f = request.files['file']
    
    
    return redirect(url_for("home")) '''
    nombreEmpresa = request.form.get("nombreEmpresa")
    descEmpresa = request.form.get("descEmpresa")
    celularEmpresa = request.form.get("celularEmpresa")
    direccionEmpresa = request.form.get("direccionEmpresa")
    correo = request.form.get("correo")
    contrasenia = request.form.get("contrasenia")
    logoEmpresa = request.files['logoEmpresa']
    print('\n\n\n\n\n\n\n\n\n\n',)
    USUARIOS.datosFormulario(
        nombreEmpresa,
        descEmpresa,
        celularEmpresa,
        direccionEmpresa,
        correo,
        contrasenia,
        logoEmpresa,
    )
    flash('Usuario registrado.... Revisa tu correo Para completar el registro')
    return redirect(url_for("home"))
    #return render_template("empresas/sing.html")

@app.get("/administracion/editarEmpresa")
def editarEmpresa():
    return render_template("empresas/editarEmpresa.html")



@app.get("/activar-empresa/<token>")
def activarEmpresa(token):
    
    resultadiActivacion =  USUARIOS.returnID(token)
    print(resultadiActivacion)
    id = resultadiActivacion["id"]
    if resultadiActivacion['resultado']:
        result = USUARIOS.activacion(id)
        flash(result['mensaje'],result['category'])
        if result['estado']:
            return render_template('empresas/sing.html')
        else:
            return render_template('empresas/resgistro.html') 
    else:
        flash("Finalizo tiempo de activacion","warning")
        USUARIOS.eliminarNoActivo(id)
        return redirect(url_for("home"))
        
        #return render_template('empresas/resgistro.html') 
    

""" parte del inicio de sesion y cerrar sesion """


@app.get("/inicio-sesion")
def inicioSesion():

    return render_template("empresas/sing.html")


@app.post("/inicio-sesion")
def inicioSesionForm():
    correo = request.form.get("correo")
    contrasenia = request.form.get("contrasenia")
    resultadoInicio = USUARIOS.inicioSesion(correo, contrasenia)
    print(resultadoInicio)
    # mensaje de estado de sesion 
    flash(resultadoInicio['mensaje'])
    
    if(resultadoInicio['estado']):
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

@app.get("/administracion/mis-productos")
def misProductos():
    return render_template("productos/empresa-producto.html")


@app.get("/administracion/registro-producto")
def registroProducto():
    return render_template("productos/empresa-registro-prod.html")

@app.route("/reestablecer/form")
def reestablecer():
    if request.method == 'POST':
            print("recuperar")
            return redirect(url_for('home'))
    return render_template("empresas/cambioContra.html")
   
app.run(debug=True)

