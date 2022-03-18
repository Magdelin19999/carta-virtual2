from flask import *
from controllers.empresas import manipulacionUsuarios as USUARIOS
#from models.empresas import mensaje
app = Flask(__name__)
app.secret_key = 'magdelinpai'
@app.get('/')
def home():
    #mensaje.mensaje()
    if 'loggedin' in session:
        print(session['usuario'] )
    else:
        print('nada')
    return render_template('productos/index.html')
    
@app.get('/inicio-sesion/')
def inicioSesion():
    '''  session['loggedin'] = True
        session['id'] = empresa['id']
        session['usuario'] = empresa['nombreEmpresa'] '''
    
    return render_template('empresas/sing.html')

@app.post('/inicio-sesion/')
def inicioSesionForm():
    correo = request.form.get('correo')
    contrasenia = request.form.get('contrasenia')
    USUARIOS.inicioSesion(correo,contrasenia)
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


@app.get('/activar-empresa/<int:id>')
def activarEmpresa(id):
    print(f'activacion {id}')
    
    return USUARIOS.activacion(id)

app.run(app.run(
        debug=True,
        host='localhost',
        port=1000
        ))