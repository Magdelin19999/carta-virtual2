from flask import *
from controllers.empresas import manipulacionUsuarios as USUARIOS
from config import mensaje
app = Flask(__name__)
@app.get('/')
def home():
    mensaje.mensaje()
    return render_template('productos/index.html')
    
@app.get('/inicio-sesion/')
def inicioSesion():
    return render_template('empresas/sing.html')
@app.get('/registro-empresa/')
def registroEmpresa():
    return render_template('empresas/registro.html')
@app.post('/registro-empresa/')
def registroEmpresaForm():
    print('holaaa')
    nombreEmpresa = request.form.get('nombreEmpresa')
    descEmpresa = request.form.get('descEmpresa')
    celularEmpresa = request.form.get('celularEmpresa')
    direccionEmpresa = request.form.get('direccionEmpresa')
    correo = request.form.get('correo')
    contrasenia = request.form.get('contrasenia')
    USUARIOS.datosFormulario(nombreEmpresa,descEmpresa,celularEmpresa,
          direccionEmpresa,correo,contrasenia)
    
    return render_template('empresas/sing.html')
app.run(debug=True)